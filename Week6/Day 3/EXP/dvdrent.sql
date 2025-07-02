-- SELECT * FROM language;

-- SELECT f.title, f.description, l.name AS language
-- FROM film f
-- JOIN language l ON f.language_id = l.language_id;

-- SELECT f.title, f.description, l.name AS language
-- FROM language l
-- LEFT JOIN film f ON l.language_id = f.language_id;

-- CREATE TABLE new_film (
--     id SERIAL PRIMARY KEY,
--     name VARCHAR(100) NOT NULL
-- );

-- INSERT INTO new_film (name) VALUES
-- ('Epic Sumo Showdown'),
-- ('Mystery Boat Hunt');

-- CREATE TABLE customer_review (
--     review_id SERIAL PRIMARY KEY,
--     film_id INT REFERENCES new_film(id) ON DELETE CASCADE,
--     language_id INT REFERENCES language(language_id),
--     title VARCHAR(255),
--     score INT CHECK (score BETWEEN 1 AND 10),
--     review_text TEXT,
--     last_update TIMESTAMP DEFAULT CURRENT_TIMESTAMP
-- );

-- INSERT INTO customer_review (film_id, language_id, title, score, review_text)
-- VALUES
-- ((SELECT id FROM new_film WHERE name = 'Epic Sumo Showdown'),
--  (SELECT language_id FROM language WHERE name = 'English'),
--  'Intense battles', 9, 'Really enjoyed the sumo matches!'),

-- ((SELECT id FROM new_film WHERE name = 'Mystery Boat Hunt'),
--  (SELECT language_id FROM language WHERE name = 'French'),
--  'Thrilling adventure', 8, 'A deep mystery at sea...');

-- DELETE FROM new_film WHERE name = 'Epic Sumo Showdown';

