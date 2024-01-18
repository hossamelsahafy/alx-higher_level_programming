-- Script That Lists All Shows Contained In The Database hbtn_0d_tvshows.
SELECT tv_shows.title,
    genre_id
from tv_shows
    LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title,
    tv_show_genres.genre_id ASC;