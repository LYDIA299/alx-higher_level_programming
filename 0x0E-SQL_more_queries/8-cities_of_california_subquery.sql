-- lists all the cities of California in the database hbtn_0d_usa
SELECT id, name
FROM cities
WHERE id = (
      SELECT id
      FROM states
      WHERE name = 'California')
ORDER BY id ASC
