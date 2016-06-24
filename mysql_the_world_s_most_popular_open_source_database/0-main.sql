SELECT 'List of all tables?' as '';
SHOW TABLES;

SELECT 'Display the table structure of TVShow, Genre, and TVShowGenre?' as '';
SHOW CREATE TABLE TVShow;
SHOW CREATE TABLE Genre;
SHOW CREATE TABLE TVShowGenre;

SELECT 'List of TVShows, only id and name ordered by name (A-Z)?' as '';
SELECT id, name FROM TVShow ORDER BY name;

SELECT 'List of Genres, only id and name ordered by name (Z-A)?' as '';
SELECT id, name FROM Genre ORDER BY name DESC;

SELECT 'List of Network, only id and name?' as '';
SELECT id, name FROM Network;

SELECT 'Number of episodes in the database?' as '';
SELECT count(id) FROM Episode;