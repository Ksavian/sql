Создайте хранимую функцию get_user_status, которая принимает параметр input_user_id типа INT 
и возвращает статус пользователя: "VIP" если у него больше 3 резерваций,
"Regular" если от 1 до 3 резерваций, "New" если резерваций нет. Используйте оператор IF.

CREATE FUNCTION get_user_status(
    input_user_id INT
)
RETURNS VARCHAR(10) -- Указываю максимальную длину для VARCHAR
BEGIN
    DECLARE num_reservations INT DEFAULT 0; -- Переменная для хранения количества резерваций
    DECLARE status_user VARCHAR(10); -- Переменная для статуса пользователя

    -- Подсчитываю количество резерваций для указанного пользователя
    SELECT COUNT(r.id)
    INTO num_reservations -- Сохраняю результат в переменную
    FROM Users u
    INNER JOIN Reservations r ON r.user_id = u.id
    WHERE u.id = input_user_id;

    -- Использую IF для определения статуса на основе количества резерваций
    IF num_reservations > 3 THEN
        SET status_user = 'VIP';
    ELSEIF num_reservations BETWEEN 1 AND 3 THEN
        SET status_user = 'Regular';
    ELSE -- Если num_reservations равно 0
        SET status_user = 'New';
    END IF;

    -- Возвращаю рассчитанный статус
    RETURN status_user;
END

