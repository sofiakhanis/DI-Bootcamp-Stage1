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

UPDATE person p
SET height = (
    SELECT AVG(p2.height::FLOAT)
    FROM person_region pr
    JOIN person p2 ON pr.person_id = p2.id
    WHERE pr.region_id = (
        SELECT pr2.region_id FROM person_region pr2 WHERE pr2.person_id = p.id
    )
)
WHERE p.height IS NULL OR p.height = '';


CREATE TEMP TABLE multi_event_competitors (
    person_id INT,
    games_id INT,
    total_events INT
);

INSERT INTO multi_event_competitors (person_id, games_id, total_events)
SELECT gc.person_id, gc.games_id, COUNT(DISTINCT ce.event_id) AS total_events
FROM games_competitor gc
JOIN competitor_event ce ON gc.id = ce.competitor_id
GROUP BY gc.person_id, gc.games_id
HAVING COUNT(DISTINCT ce.event_id) > 1;


WITH total_avg AS (
    SELECT AVG(medal_count::FLOAT / competitor_count) AS overall_avg
    FROM (
        SELECT pr.region_id,
               COUNT(DISTINCT ce.competitor_id) AS competitor_count,
               COUNT(ce.medal_id) AS medal_count
        FROM person_region pr
        JOIN games_competitor gc ON gc.person_id = pr.person_id
        JOIN competitor_event ce ON ce.competitor_id = gc.id
        WHERE ce.medal_id IS NOT NULL
        GROUP BY pr.region_id
    ) region_stats
)


SELECT nr.region_name,
       (COUNT(ce.medal_id)::FLOAT / COUNT(DISTINCT gc.person_id)) AS region_avg
FROM person_region pr
JOIN noc_region nr ON pr.region_id = nr.id
JOIN games_competitor gc ON gc.person_id = pr.person_id
JOIN competitor_event ce ON ce.competitor_id = gc.id
WHERE ce.medal_id IS NOT NULL
GROUP BY nr.region_name
HAVING (COUNT(ce.medal_id)::FLOAT / COUNT(DISTINCT gc.person_id)) >
       (SELECT overall_avg FROM total_avg);

CREATE TEMP TABLE dual_season_participants AS
SELECT person_id
FROM (
    SELECT person_id, COUNT(DISTINCT season) AS seasons_count
    FROM games_competitor gc
    JOIN games g ON gc.games_id = g.id
    GROUP BY person_id
) season_counts
WHERE seasons_count = 2;

SELECT p.id, p.full_name
FROM person p
WHERE p.id IN (SELECT person_id FROM dual_season_participants);