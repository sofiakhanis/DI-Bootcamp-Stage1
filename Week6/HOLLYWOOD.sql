-- CREATE TABLE actors (
-- actor_id SERIAL PRIMARY KEY,
-- first_name VARCHAR (50) NOT NULL,
-- second_name VARCHAR (100) NOT NULL,
-- age DATE NOT NULL,
-- number_oscars SMALLINT NOT NULL
-- )

-- How to add info (need to comment everything before or it will duplicate!)

-- INSERT INTO actors (first_name, second_name, age, number_oscars)
-- VALUES ('Matt', 'Damon', '06/05/1961', '2')

-- INSERT INTO actors (first_name, second_name, age, number_oscars)
-- VALUES ('Jack', 'Nickolson', '04/06/1954', '3')

-- INSERT INTO actors (first_name, second_name, age, number_oscars)
-- VALUES ('Norra', 'Medn', '10/03/1983', '2');

-- SELECT * FROM actors 

-- SELECT age FROM actors;
-- SELECT * FROM actors WHERE number_oscars > 2;

-- SELECT first_name, second_name FROM actors WHERE first_name = 'Matt'  AND second_name = 'Damon'

--SELECT * FROM actors WHERE second_name LIKE '%mon%';

SELECT * FROM actors LIMIT 3;

SELECT * FROM actors WHERE age > '1960-01-01' LIMIT 3 OFFSET 2