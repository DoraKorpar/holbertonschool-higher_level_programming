UPDATE Person
SET age=27
WHERE first_name="Jon";

UPDATE Person
SET age=18
WHERE first_name="Walter Junior";

DELETE FROM Person
WHERE id=1;

DELETE FROM EyesColor
WHERE person_id=1;

SELECT * FROM Person
ORDER BY first_name;