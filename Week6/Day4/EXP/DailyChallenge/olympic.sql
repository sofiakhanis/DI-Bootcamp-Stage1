CREATE TEMP TABLE multi_season_medalists AS
SELECT person_id,
       SUM(CASE WHEN g.season = 'Summer' THEN 1 ELSE 0 END) AS summer_medals,
       SUM(CASE WHEN g.season = 'Winter' THEN 1 ELSE 0 END) AS winter_medals
FROM competitor_event ce
JOIN games_competitor gc ON ce.competitor_id = gc.id
JOIN games g ON gc.games_id = g.id
WHERE ce.medal_id IS NOT NULL
GROUP BY person_id
HAVING SUM(CASE WHEN g.season = 'Summer' THEN 1 ELSE 0 END) > 0
   AND SUM(CASE WHEN g.season = 'Winter' THEN 1 ELSE 0 END) > 0;
   
SELECT msm.person_id, p.full_name, msm.summer_medals, msm.winter_medals
FROM multi_season_medalists msm
JOIN person p ON p.id = msm.person_id;

CREATE TEMP TABLE two_sport_medalists AS
SELECT gc.person_id,
       COUNT(DISTINCT e.sport_id) AS num_sports,
       COUNT(*) AS total_medals
FROM competitor_event ce
JOIN games_competitor gc ON ce.competitor_id = gc.id
JOIN event e ON ce.event_id = e.id
WHERE ce.medal_id IS NOT NULL
GROUP BY gc.person_id
HAVING COUNT(DISTINCT e.sport_id) = 2;

SELECT tsm.person_id, p.full_name, tsm.total_medals
FROM two_sport_medalists tsm
JOIN person p ON p.id = tsm.person_id
ORDER BY tsm.total_medals DESC
LIMIT 3;

WITH medals_per_event AS (
    SELECT gc.person_id,
           ce.event_id,
           COUNT(*) AS medal_count
    FROM competitor_event ce
    JOIN games_competitor gc ON ce.competitor_id = gc.id
    WHERE ce.medal_id IS NOT NULL
    GROUP BY gc.person_id, ce.event_id
),
max_medal_event AS (
    SELECT person_id, MAX(medal_count) AS max_medals
    FROM medals_per_event
    GROUP BY person_id
)

SELECT nr.region_name,
       SUM(me.max_medals) AS total_top_event_medals
FROM max_medal_event me
JOIN person_region pr ON me.person_id = pr.person_id
JOIN noc_region nr ON pr.region_id = nr.id
GROUP BY nr.region_name
ORDER BY total_top_event_medals DESC
LIMIT 5;

CREATE TEMP TABLE no_medals_many_games AS
SELECT gc.person_id,
       COUNT(DISTINCT gc.games_id) AS games_participated
FROM games_competitor gc
LEFT JOIN competitor_event ce ON gc.id = ce.competitor_id AND ce.medal_id IS NOT NULL
GROUP BY gc.person_id
HAVING COUNT(DISTINCT gc.games_id) > 3 AND COUNT(ce.medal_id) = 0;

SELECT nm.person_id, p.full_name, nm.games_participated
FROM no_medals_many_games nm
JOIN person p ON p.id = nm.person_id;

