INSERT INTO EyesColor VALUES (6, "Green");
INSERT INTO EyesColor VALUES (7, "Brown");

CREATE TABLE TVShow (
       id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
       name char(128) NOT NULL
);

CREATE TABLE TVShowPerson (
       tvshow_id INTEGER NOT NULL,
       person_id INTEGER NOT NULL,
       FOREIGN KEY(tvshow_id) REFERENCES TVShow(id),
       FOREIGN KEY(person_id) REFERENCES Person(id)
);

INSERT INTO TVShow VALUES (1, "Homeland");
INSERT INTO TVShow VALUES (2, "The big bang theory");
INSERT INTO TVShow VALUES (3, "Game of Thrones");
INSERT INTO TVShow VALUES (4, "Breaking Bad");

INSERT INTO TVShowPerson VALUES (4, 2);
INSERT INTO TVShowPerson VALUES (3, 3);
INSERT INTO TVShowPerson VALUES (2, 4);
INSERT INTO TVShowPerson VALUES (3, 5);
INSERT INTO TVShowPerson VALUES (3, 6);
INSERT INTO TVShowPerson VALUES (3, 7);

SELECT * FROM Person;
SELECT * FROM EyesColor;
SELECT * FROM TVShow;
SELECT * FROM TVShowPerson;