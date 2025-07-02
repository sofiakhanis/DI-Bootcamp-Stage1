-- UPDATE film
-- SET language_id = (SELECT language_id FROM language WHERE name = 'Italian')
-- WHERE film_id IN (1, 2, 3);

-- customer.address_id → references address(address_id)
-- customer.store_id → references store(store_id)

-- DROP TABLE customer_review;

-- SELECT COUNT(*) 
-- FROM rental 
-- WHERE return_date IS NULL;

-- SELECT f.title, i.inventory_id, f.replacement_cost
-- FROM rental r
-- JOIN inventory i ON r.inventory_id = i.inventory_id
-- JOIN film f ON i.film_id = f.film_id
-- WHERE r.return_date IS NULL
-- ORDER BY f.replacement_cost DESC
-- LIMIT 30;

-- SELECT f.title
-- FROM film f
-- JOIN film_actor fa ON f.film_id = fa.film_id
-- JOIN actor a ON fa.actor_id = a.actor_id
-- WHERE f.description ILIKE '%sumo%'
--   AND a.first_name = 'Penelope' AND a.last_name = 'Monroe';

-- SELECT title
-- FROM film
-- WHERE length < 60
--   AND rating = 'R';

-- SELECT f.title
-- FROM payment p
-- JOIN rental r ON p.rental_id = r.rental_id
-- JOIN inventory i ON r.inventory_id = i.inventory_id
-- JOIN film f ON i.film_id = f.film_id
-- JOIN customer c ON p.customer_id = c.customer_id
-- WHERE c.first_name = 'Matthew' AND c.last_name = 'Mahan'
--   AND p.amount > 4
--   AND r.return_date BETWEEN '2005-07-28' AND '2005-08-01';

-- SELECT f.title
-- FROM film f
-- JOIN inventory i ON f.film_id = i.film_id
-- JOIN rental r ON i.inventory_id = r.inventory_id
-- JOIN customer c ON r.customer_id = c.customer_id
-- WHERE c.first_name = 'Matthew' AND c.last_name = 'Mahan'
--   AND (f.title ILIKE '%boat%' OR f.description ILIKE '%boat%')
-- ORDER BY f.replacement_cost DESC
-- LIMIT 1;