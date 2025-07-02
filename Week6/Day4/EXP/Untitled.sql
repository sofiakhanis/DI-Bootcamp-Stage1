SELECT m.medal_name,
       AVG((
           SELECT gc.age
           FROM games_competitor gc
           WHERE gc.person_id = ce.competitor_id
       )) AS avg_age
FROM competitor_event ce
JOIN medal m ON ce.medal_id = m.id
WHERE ce.medal_id IS NOT NULL
GROUP BY m.medal_name;

SELECT nr.region_name, COUNT(*) AS num_competitors
FROM (
    SELECT gr.person_id
    FROM competitor_event ce
    JOIN games_competitor gr ON gr.id = ce.competitor_id
    GROUP BY gr.person_id
    HAVING COUNT(DISTINCT ce.event_id) > 3
) qualified
JOIN person_region pr ON qualified.person_id = pr.person_id
JOIN noc_region nr ON pr.region_id = nr.id
GROUP BY nr.region_name
ORDER BY num_competitors DESC
LIMIT 5;


CREATE TEMP TABLE total_medals AS
SELECT ce.competitor_id, COUNT(*) AS total_medals
FROM competitor_event ce
WHERE ce.medal_id IS NOT NULL
GROUP BY ce.competitor_id;

SELECT *
FROM total_medals
WHERE total_medals > 2;

DELETE FROM total_medals
WHERE competitor_id IN (
    SELECT tm.competitor_id
    FROM total_medals tm
    LEFT JOIN competitor_event ce ON tm.competitor_id = ce.competitor_id AND ce.medal_id IS NOT NULL
    GROUP BY tm.competitor_id
    HAVING COUNT(ce.medal_id) = 0
);

