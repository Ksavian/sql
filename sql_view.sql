#создайте представление.вывести информацию о клиенте и номере фильма, 
а также фильм, который он приобрел последним . посчитайте размер среднего платежа
 

CREATE VIEW task AS
  SELECT c.customer_id,f.film_id,CONCAT(c.last_name,' ',c.first_name),c.email
  FROM Customer c
  JOIN( 
       SELECT *, ROW_NUMBER() OVER(PARRITITION BY customer_id ORDER BY rental_date DESC)
       FROM Rental r) r ON c.customer_id = r.customer_id
  JOIN Inventiry i ON i.inventory_id  = r.customer_id
  JOIN Film f ON f.film_id = i.film_id
  WHERE row_number = 1


SELECT task.*,p.avg
FROM task
JOIN (
      SELECT customer_id,AVG(amount)
      FROM Payment 
      GROUP BY 1) p ON task.customer_id = p.customer_id
