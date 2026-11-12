import numpy as np
from scipy import stats
import scipy.stats as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("c:/happines_corruption.csv")
#print(df.info())
#print("\n",df.describe())
"""
Страна - Название страны.
happiness_score - Среднее значение ответов на основной вопрос оценки жизни из Gallup World Poll (GWP). 0-10
gdp_per_capita - Насколько ВВП (валовой внутренний продукт) способствует расчету индекса счастья.
family - Насколько семья способствует расчету индекса счастья.
health - Насколько продолжительность жизни способствует расчету индекса счастья.
freedom - Насколько свобода способствует расчету индекса счастья.
generosity - Числовое значение, рассчитанное на основе восприятия участниками опроса щедрости в своей стране.
government_trust - Насколько восприятие коррупции способствует расчету индекса счастья.
dystopia_residual - Оценка, основанная на гипотетическом сравнении с самой несчастной страной в мире.
continent - Континент, к которому относится страна.
"""
#Верно ли, что чем выше ВВП, тем выше и уровень счастья?
df_compare  = df[["happiness_score","gdp_per_capita"]]
#print(df_compare.head())

#проверяю на нормальность распределения данных
statistics,p_value = stats.shapiro(df_compare)
alpha = 0.05
print(f"statistics = {statistics:.2f}")
print(f"p_value = {p_value:.2f}")

if p_value< alpha:
    print("данные распределены не нормально")
else:
    print("Данные распределены нормально")

# --- Корреляционный анализ (вместо Манна-Уитни) ---
# Так как данные, скорее всего, распределены ненормально, использую Спирмена
var1 = "happiness_score"
var2 = "gdp_per_capita"
spearman_corr, spearman_p = stats.spearmanr(df[var1],df[var2])

print(f"\n--- Результаты корреляции Спирмена между '{var1}' и '{var2}' ---")
print(f"Коэффициент корреляции Спирмена: {spearman_corr:.3f}")
print(f"P-значение: {spearman_p:.7f}")
if spearman_p < alpha:
    print(f"Существует статистически значимая монотонная связь между '{var1}' и '{var2}' (p < {alpha}).")
    if spearman_corr > 0:
        print("Связь положительная: чем выше ВВП, тем выше уровень счастья.")
    elif spearman_corr < 0:
        print("Связь отрицательная: чем выше ВВП, тем ниже уровень счастья.")
    else:
        print("Связь отсутствует.")
else:
    print(f"Нет статистически значимой монотонной связи между '{var1}' и '{var2}' (p >= {alpha}).")
# визуализация
plt.figure(figsize=(12, 8))
sns.scatterplot(data=df, x=var2, y=var1, hue="continent", alpha=0.6)
plt.title(f'Диаграмма рассеяния: {var1} vs {var2} по континентам')
plt.xlabel(f'{var2.replace("_", " ").title()}')
plt.ylabel(f'{var1.replace("_", " ").title()}')
plt.grid(True, linestyle='--', alpha=0.5)
plt.legend(title="Continent", bbox_to_anchor=(1.05, 1), loc='upper left') 
plt.tight_layout() 
plt.show()

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

df = pd.read_csv("c:/gas_sales_data.csv")
#print(df.head())

#В этом задании нужно окончательно ответить на вопрос:
#Есть ли связь между среднемесячной температурой и потреблением газа в Южной Корее?
#Для этого:
#Оставьте только два столбца:'Temperature' и 'Sum'.
#Постройте диаграмму рассеяния.
#Постройте модель линейной регрессии для выбранных признаков.
#ассчитайте точность модели на тестовой выборке.
#Выведите график остатков

df_t_s = df[["Temperature","Sum"]]
#print(df_t_s.head())
#2

plt.figure(figsize=(10,6))
sns.scatterplot(df_t_s,x="Temperature",y="Sum")
plt.title("связь между среднемесячной температурой и газом")
plt.xlabel("сколько градусов")
plt.ylabel("сумма")
plt.grid()
plt.show()

# 3. Постройте модель линейной регрессии для выбранных признаков
# Разделяю данные на обучающую и тестовую выборки
# X - независимая переменная (температура)
# y - зависимая переменная (потребление газа)
X = df_t_s[['Temperature']]
y = df_t_s['Sum']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42) # test_size=0.2 означает 20% данных для тестирования

#инициализирую и обучаю модель линейной регрессии
model = LinearRegression()
model.fit(X_train,y_train)
print("\nПараметры модели линейной регрессии:")
print(f"Коэффициент наклона (slope): {model.coef_[0]:.4f}")
print(f"Свободный член (intercept): {model.intercept_:.4f}")

# 4. Рассчитываю точность модели на тестовой выборке.
y_pred = model.predict(X_test)

# Оцениваю модель
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("\nОценка модели на тестовой выборке:")
print(f"Среднеквадратичная ошибка (MSE): {mse:.4f}")
print(f"Коэффициент детерминации (R^2): {r2:.4f}")

# Интерпретация R^2:
# R^2 показывает, какую долю дисперсии зависимой переменной (потребления газа)
# объясняет модель. Значение от 0 до 1. Чем ближе к 1, тем лучше модель объясняет данные.
# 5. Выведите график остатков.

# Остатки - это разница между фактическими значениями y_test и предсказанными y_pred
residuals = y_test - y_pred

plt.figure(figsize=(10, 6))
sns.scatterplot(x=y_pred, y=residuals)
plt.axhline(y=0, color='r', linestyle='--')
plt.title('График остатков')
plt.xlabel('Предсказанное значение потребления газа')
plt.ylabel('Остатки')
plt.grid(True)
plt.show()

# Дополнительно: Нанесу линию регрессии на диаграмму рассеяния
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df_t_s , x='Temperature', y='Sum', label='Фактические данные')
plt.plot(X, model.predict(X), color='red', linewidth=2, label='Линия регрессии')
plt.title('Диаграмма рассеяния с линией регрессии')
plt.xlabel('Среднемесячная температура (°C)')
plt.ylabel('Потребление газа (единицы)')
plt.legend()
plt.grid(True)
plt.show()
