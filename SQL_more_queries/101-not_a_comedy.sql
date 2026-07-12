-- A script that lists all shows without the genre Comedy in the database hbtn_0d_tvshows.
SELECT
    DISTINCT t.title
FROM
    tv_shows AS t
    LEFT JOIN tv_show_genres AS m ON m.show_id = t.id
    LEFT JOIN tv_genres AS g ON m.genre_id = g.id
WHERE
    t.title NOT IN (
        SELECT
            title
        FROM
            tv_shows AS t
            INNER JOIN tv_show_genres AS m ON m.show_id = t.id
            INNER JOIN tv_genres AS g ON g.id = m.genre_id
        WHERE
            g.name = 'Comedy'
        )
ORDER BY
    title ASC;
