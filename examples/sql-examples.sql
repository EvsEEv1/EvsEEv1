-- =====================================================
-- Мои примеры SQL-запросов
-- Евсей Евсеев
-- Уровень: базовый (SELECT, JOIN, GROUP BY, агрегация)
-- =====================================================

-- 1. Агрегация с GROUP BY: мин, макс, средняя цена по автору
-- Использую: SELECT, MIN, MAX, AVG, GROUP BY
SELECT 
    author, 
    MIN(price) AS Минимальная_цена, 
    MAX(price) AS Максимальная_цена, 
    AVG(price) AS Средняя_цена
FROM book
GROUP BY author;

-- 2. JOIN двух таблиц с фильтром и сортировкой
-- Использую: SELECT, JOIN, WHERE, ORDER BY
SELECT 
    title, 
    name_genre, 
    price
FROM book
JOIN genre ON genre.genre_id = book.genre_id
WHERE amount > 8
ORDER BY price DESC;

-- 3. Логика внутри запроса: IF (условное изменение цены)
-- Использую: SELECT, IF, ROUND
SELECT 
    author, 
    title, 
    ROUND(
        IF(author = "Булгаков М.А.", price * 1.1,
            IF(author = "Есенин С.А.", price * 1.05, price)
        ), 2
    ) AS new_price
FROM book;