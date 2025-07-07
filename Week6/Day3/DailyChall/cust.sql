-- CREATE TABLE Customer (
--     id SERIAL PRIMARY KEY,
--     first_name VARCHAR(50) NOT NULL,
--     last_name VARCHAR(50) NOT NULL
-- );

-- CREATE TABLE CustomerProfile (
--     id SERIAL PRIMARY KEY,
--     isLoggedIn BOOLEAN DEFAULT false,
--     customer_id INTEGER UNIQUE REFERENCES Customer(id) ON DELETE CASCADE
-- );

-- INSERT INTO Customer (first_name, last_name) VALUES
-- ('John', 'Doe'),
-- ('Jerome', 'Lalu'),
-- ('Lea', 'Rive');

-- SELECT * FROM Customer

-- INSERT INTO CustomerProfile (isLoggedIn, customer_id) VALUES
-- (true, (SELECT id FROM Customer WHERE first_name = 'John')),
-- (false, (SELECT id FROM Customer WHERE first_name = 'Jerome'));

-- SELECT c.first_name
-- FROM Customer c
-- JOIN CustomerProfile cp ON c.id = cp.customer_id
-- WHERE cp.isLoggedIn = true;

-- SELECT c.first_name, cp.isLoggedIn
-- FROM Customer c
-- LEFT JOIN CustomerProfile cp ON c.id = cp.customer_id;

-- SELECT COUNT(*)
-- FROM Customer c
-- JOIN CustomerProfile cp ON c.id = cp.customer_id
-- WHERE cp.isLoggedIn = false;