-- A script that lists all genres in the database hbtn_0d_tvshows_rate by their rating.
SELECT
    g.name,
    SUM(r.rate) AS rating
FROM
    tv_genres AS g
    INNER JOIN tv_show_genres AS m ON m.genre_id = g.id
    INNER JOIN tv_shows AS t ON t.id = m.show_id
    INNER JOIN tv_show_ratings AS r ON r.show_id = t.id
GROUP BY
    g.name
ORDER BY
    rating DESC;
