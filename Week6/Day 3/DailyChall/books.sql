
-- CREATE TABLE Book (
--     book_id SERIAL PRIMARY KEY,
--     title VARCHAR(100) NOT NULL,
--     author VARCHAR(100) NOT NULL
-- );

-- INSERT INTO Book (title, author) VALUES
-- ('Alice In Wonderland', 'Lewis Carroll'),
-- ('Harry Potter', 'J.K Rowling'),
-- ('To kill a mockingbird', 'Harper Lee');

-- CREATE TABLE Student (
--     student_id SERIAL PRIMARY KEY,
--     name VARCHAR(100) NOT NULL UNIQUE,
--     age INTEGER CHECK (age <= 15)
-- );

-- INSERT INTO Student (name, age) VALUES
-- ('John', 12),
-- ('Lera', 11),
-- ('Patrick', 10),
-- ('Bob', 14);

-- CREATE TABLE Library (
--     book_fk_id INTEGER REFERENCES Book(book_id) ON DELETE CASCADE ON UPDATE CASCADE,
--     student_fk_id INTEGER REFERENCES Student(student_id) ON DELETE CASCADE ON UPDATE CASCADE,
--     borrowed_date DATE,
--     PRIMARY KEY (book_fk_id, student_fk_id, borrowed_date)
-- );

-- INSERT INTO Library (book_fk_id, student_fk_id, borrowed_date) VALUES
-- ((SELECT book_id FROM Book WHERE title = 'Alice In Wonderland'),
--  (SELECT student_id FROM Student WHERE name = 'John'),
--  '2022-02-15'),

-- ((SELECT book_id FROM Book WHERE title = 'To kill a mockingbird'),
--  (SELECT student_id FROM Student WHERE name = 'Bob'),
--  '2021-03-03'),

-- ((SELECT book_id FROM Book WHERE title = 'Alice In Wonderland'),
--  (SELECT student_id FROM Student WHERE name = 'Lera'),
--  '2021-05-23'),

-- ((SELECT book_id FROM Book WHERE title = 'Harry Potter'),
--  (SELECT student_id FROM Student WHERE name = 'Bob'),
--  '2021-08-12');

--SELECT * FROM Library;

-- SELECT s.name, b.title
-- FROM Library l
-- JOIN Student s ON l.student_fk_id = s.student_id
-- JOIN Book b ON l.book_fk_id = b.book_id;

-- SELECT AVG(s.age) AS average_age
-- FROM Library l
-- JOIN Student s ON l.student_fk_id = s.student_id
-- JOIN Book b ON l.book_fk_id = b.book_id
-- WHERE b.title = 'Alice In Wonderland';

-- DELETE FROM Student WHERE name = 'Bob';

-- SELECT * FROM Student
