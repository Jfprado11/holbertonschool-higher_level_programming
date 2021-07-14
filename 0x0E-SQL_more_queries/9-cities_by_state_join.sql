-- list all cities
-- that are containing in hbtn_0d_usa.
SELECT cities.id, cities.name, states.name
FROM cities, states
WHERE cities.id = states.id
ORDER BY cities.id ASC;
