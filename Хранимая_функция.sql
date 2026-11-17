Создайте хранимую функцию calc_factorial, которая принимает параметр n типа INT
и возвращает его факториал типа BIGINT — произведение чисел от 1 до n. Для 0 функция возвращает 1.

CREATE FUNCTION calc_factorial(n INT)
RETURNS BIGINT
BEGIN
     DECLARE fact BIGINT DEFAULT 1;
     DECLARE i INT DEFAULT 1;

     WHILE i <= n DO
         SET fact = fact *i;
         SET i = i + 1;
     END WHILE;
     
     RETURN fact;
END

