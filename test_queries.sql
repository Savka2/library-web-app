-- Тестовые запросы к БД «Библиотека»
-- 1. Количество выдач и выручка по жанрам
SELECT b.Genre, COUNT(i.Issue_ID) AS Issues, SUM(i.Rental_Price) AS Revenue
FROM Issues AS i JOIN Books AS b ON i.Book_ID = b.Book_ID
GROUP BY b.Genre ORDER BY Revenue DESC;

-- 2. Читатели с фамилией на «К»
SELECT Reader_ID, Surname, Name, Phone FROM Readers
WHERE Surname LIKE 'К%' ORDER BY Surname;

-- 3. Авторы, книги которых выдавались более двух раз
SELECT b.Author, COUNT(*) AS Issues
FROM Issues AS i JOIN Books AS b ON i.Book_ID = b.Book_ID
GROUP BY b.Author HAVING COUNT(*) > 2;
