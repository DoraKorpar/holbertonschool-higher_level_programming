-- get number of seasons by tvshow_id
\! echo "Number of seasons by tvshow_id?";
SELECT tvshow_id, count(id) FROM Season GROUP BY tvshow_id ORDER BY tvshow_id;

-- get number of occurrences of same episode number ordered by episode number
\! echo "Number of occurrences of the same episode number ordered by episode number?";
SELECT number, count(id) FROM Episode GROUP BY number ORDER BY number;

-- get top 3 occurrences of genre in all TVshow, limit to top 3
\! echo "Top 3 of the Genre\'s occurrences in all TVShows ordered by this number?";
SELECT genre_id, count(genre_id) AS occurrences_genre FROM TVShowGenre GROUP BY genre_id ORDER BY count(genre_id) DESC LIMIT 3;

-- get all tvshows containing string and print lowercase
\! echo "Search all TVShow with this letter sequence \'th\' case insensitive and display with the name in lowercase?";
SELECT LOWER(name) AS name FROM TVShow WHERE name LIKE '%th%';
