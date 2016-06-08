SELECT DISTINCT last_name FROM Person, TVShowPerson, TVShow
WHERE Person.id=TVShowPerson.person_id AND TVShowPerson.tvshow_id=TVShow.id AND TVShow.name="Game of Thrones"
ORDER BY last_name;

SELECT count(age) FROM Person
WHERE Person.age>30;

SELECT Person.id, Person.first_name, Person.last_name, Person.age, EyesColor.color, TVShow.name FROM Person, EyesColor, TVShowPerson, TVShow
WHERE Person.id=TVShowPerson.person_id AND Person.id=EyesColor.person_id AND TVShowPerson.tvshow_id=TVShow.id;

SELECT sum(age) FROM Person;

