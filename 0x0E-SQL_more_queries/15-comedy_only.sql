-- lists all Comedy shows in the database
SELECT title
FROM tv_shows
INNER JOIN (tv_show_genres INNER JOIN tv_genres
ON tv_show_genres.genre_id = tv_genres.id)
ON tv_show_genres.show_id = tv_shows.id
WHERE name = 'Comedy'
ORDER BY tv_shows.title ASC;
