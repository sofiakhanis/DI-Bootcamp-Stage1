-- CREATE TABLE items (
-- item_id SERIAL PRIMARY KEY,
-- item VARCHAR (100) NOT NULL,
-- price SMALLINT NOT NULL
-- )

-- INSERT INTO items (item, price)
-- VALUES ('Small Desk', 100),
-- ('Large desk', 300),
-- ('Fan', 80);

-- SELECT * FROM items 

-- CREATE TABLE customers (
-- name_cust VARCHAR NOT NULL,
-- surname_cust VARCHAR NOT NULL
-- )

-- INSERT INTO customers (name_cust, surname_cust)
-- VALUES ('Greg', 'Jones'),
-- ('Sandra', 'Jones'),
-- ('Scott', 'Scott'),
-- ('Trevor', 'Green'),
-- ('Melanie', 'Johnson');

-- SELECT * FROM customers 

SELECT * FROM items WHERE price > 80;

SELECT * FROM items WHERE price <= 300;

SELECT * FROM customers WHERE surname_cust = 'Smith';

SELECT * FROM customers WHERE surname_cust = 'Jones';

SELECT * FROM customers WHERE name_cust != 'Scott';


