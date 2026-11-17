Для каждого жилья из таблицы Rooms выведите id, price
и количество объявлений не дороже текущего — not_more_expensive. Объявления с той же ценой тоже считаются.

SELECT id,price,
COUNT(*) OVER(
ORDER BY price  
RANGE BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW ) as not_more_expensive
FROM Rooms



