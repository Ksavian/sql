В качестве результирующей выборки выведите идентификаторы компаний (в поле company), 
время вылета их рейсов (в поле time_out) и время (в поле time_diff), прошедшее с предыдущего вылета в формате ЧЧ:ММ:СС.
Если это был первый рейс компании, то в поле time_diff нужно вывести "00:00:00".

WITH flights AS(
SELECT company,time_out,
LAG(time_out) OVER(PARITITION BY company ORDER BY time_out) as prev_time
FROM Trip)
SELECT company,time_out,
COALESCE(SEC_TO_TIME(TIMESTAMPDIFF(SECOND,prev_time,time_out)),"00:00:00") AS time_diff
FROM flights
ORDER BY company,time_out

