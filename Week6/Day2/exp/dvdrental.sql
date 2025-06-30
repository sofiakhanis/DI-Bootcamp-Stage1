SELECT * FROM customer;
SELECT first_name || ' ' || last_name AS full_name FROM customer;
SELECT DISTINCT create_date FROM customer;
SELECT * FROM customer ORDER BY first_name DESC;

SELECT film_id, title, description, release_year, rental_rate
FROM film
ORDER BY rental_rate ASC;

SELECT address, phone 
FROM address
WHERE district = 'Texas';

SELECT * 
FROM film
WHERE film_id IN (15, 150);

SELECT film_id, title, description, length, rental_rate
FROM film
WHERE title = 'FAVORITE_MOVIE';

SELECT film_id, title, description, length, rental_rate
FROM film
WHERE title ILIKE 'SH%';

SELECT *
FROM film
ORDER BY rental_rate ASC
LIMIT 10;

SELECT * FROM film ORDER BY rental_rate ASC OFFSET 10 LIMIT 10;

SELECT *
FROM film
WHERE film_id NOT IN (
    SELECT film_id
    FROM film
    ORDER BY rental_rate ASC
    LIMIT 10
)
ORDER BY rental_rate ASC
LIMIT 10;

SELECT c.first_name, c.last_name, p.amount, p.payment_date
FROM customer c
JOIN payment p ON c.customer_id = p.customer_id
ORDER BY c.customer_id;

SELECT * 
FROM film
WHERE film_id NOT IN (
    SELECT DISTINCT film_id
    FROM inventory
);

SELECT ci.city, co.country
FROM city ci
JOIN country co ON ci.country_id = co.country_id;

SELECT c.customer_id, c.first_name, c.last_name, p.amount, p.payment_date, p.staff_id
FROM customer c
JOIN payment p ON c.customer_id = p.customer_id
ORDER BY p.staff_id;
