-- exercise 1

-- SELECT
--     g.genre_name,
--     m.title,
--     RANK() OVER (PARTITION BY g.genre_name ORDER BY m.popularity DESC) AS popularity_rank
-- FROM movie m
-- JOIN movie_genres mg ON m.movie_id = mg.movie_id
-- JOIN genre g ON mg.genre_id = g.genre_id;

-- SELECT
--     c.company_name,
--     m.title,
--     m.revenue,
--     NTILE(4) OVER (PARTITION BY c.company_name ORDER BY m.revenue DESC) AS revenue_quartile
-- FROM movie m
-- JOIN movie_company mc ON m.movie_id = mc.movie_id
-- JOIN company c ON mc.company_id = c.company_id;

-- SELECT
--     g.genre_name,
--     m.title,
--     m.budget,
--     SUM(m.budget) OVER (
--         PARTITION BY g.genre_name 
--         ORDER BY m.release_date
--         ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
--     ) AS running_budget
-- FROM movie m
-- JOIN movie_genres mg ON m.movie_id = mg.movie_id
-- JOIN genre g ON mg.genre_id = g.genre_id;

-- SELECT DISTINCT ON (g.genre_name)
--     g.genre_name,
--     m.title,
--     m.release_date
-- FROM movie m
-- JOIN movie_genres mg ON m.movie_id = mg.movie_id
-- JOIN genre g ON mg.genre_id = g.genre_id
-- ORDER BY g.genre_name, m.release_date DESC;

-- exercise 2

-- SELECT
--     p.person_name,
--     DENSE_RANK() OVER (ORDER BY COUNT(mc.movie_id) DESC) AS actor_rank
-- FROM person p
-- JOIN movie_cast mc ON p.person_id = mc.person_id
-- GROUP BY p.person_name;

-- WITH director_avg_rating AS (
--     SELECT
--         p.person_name,
--         AVG(m.vote_average) AS avg_rating
--     FROM person p
--     JOIN movie_crew mc ON p.person_id = mc.person_id
--     JOIN movie m ON mc.movie_id = m.movie_id
--     JOIN department d ON mc.department_id = d.department_id
--     WHERE d.department_name = 'Directing'
--     GROUP BY p.person_name
-- )
-- SELECT person_name, avg_rating
-- FROM (
--     SELECT *,
--            RANK() OVER (ORDER BY avg_rating DESC) AS rnk
--     FROM director_avg_rating
-- ) sub
-- WHERE rnk = 1;

-- SELECT
--     p.person_name,
--     SUM(m.revenue) AS total_revenue
-- FROM person p
-- JOIN movie_cast mc ON p.person_id = mc.person_id
-- JOIN movie m ON mc.movie_id = m.movie_id
-- GROUP BY p.person_name
-- ORDER BY total_revenue DESC;


-- WITH director_total_budget AS (
--     SELECT
--         p.person_name,
--         SUM(m.budget) AS total_budget
--     FROM person p
--     JOIN movie_crew mc ON p.person_id = mc.person_id
--     JOIN movie m ON mc.movie_id = m.movie_id
--     JOIN department d ON mc.department_id = d.department_id
--     WHERE d.department_name = 'Directing'
--     GROUP BY p.person_name
-- )
-- SELECT person_name, total_budget
-- FROM (
--     SELECT *,
--            RANK() OVER (ORDER BY total_budget DESC) AS rnk
--     FROM director_total_budget
-- ) sub
-- WHERE rnk = 1;
