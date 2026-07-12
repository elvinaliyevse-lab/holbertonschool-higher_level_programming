-- A script that uses the hbtn_0d_tvshows database to list all genres not linked to the show Dexter.
SELECT
    DISTINCT g.name
FROM
    tv_genres AS g
INNER JOIN
    tv_show_genres AS m
ON
    g.id = m.genre_id
INNER JOIN
    tv_shows AS t
ON
    t.id = m.show_id
WHERE
    g.name NOT IN (
        SELECT
            name
        FROM
            tv_genres AS g
        INNER JOIN
            tv_show_genres AS m
        ON
            g.id = m.genre_id
        INNER JOIN
            tv_shows t
        ON
            m.show_id = t.id
        WHERE
            t.title = 'Dexter'
        )
ORDER BY
    name ASC;
