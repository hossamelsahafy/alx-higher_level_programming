-- Script that Lists All genres from hbtn_0d_tvshows And Displays The Number Of Shows Linked To Each.
SELECT tv_genres.name AS genre,
    COUNT(tv_show_genres.show_id) AS number_of_shows
FROM tv_genres
    LEFT JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
GROUP BY tv_genres.name
HAVING COUNT(tv_show_genres.show_id) > 0
ORDER BY COUNT(tv_show_genres.show_id) DESC;