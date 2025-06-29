-- CREATE TABLE actors (
-- actor_id SERIAL PRIMARY KEY,
-- first_name VARCHAR (50) NOT NULL,
-- second_name VARCHAR (100) NOT NULL,
-- age DATE NOT NULL,
-- number_oscars SMALLINT NOT NULL
-- )

-- INSERT INTO actors (first_name, second_name, age, number_oscars)
-- VALUES ('Matt', 'Damon', '06/05/1961', '2'),
-- ('Jack', 'Nickolson', '04/06/1954', '3'),
-- ('Norra', 'Medn', '10/03/1983', '2'),
-- ('Anjelina', 'Jolie', '06/04/1975', '5')

--SELECT * FROM actors
SELECT COUNT(*) FROM actors;

-- INSERT INTO actors (first_name, second_name, age, number_oscars)
-- VALUES ('', NULL, NULL, '');

INSERT INTO actors (first_name, second_name, age, number_oscars)
VALUES ('Test', NULL, NULL, 0);

-- shows error ERROR:  null value in column "second_name" of relation "actors" violates not-null constraint
-- Failing row contains (5, Test, null, null, 0). 
