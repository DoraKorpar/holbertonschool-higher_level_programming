import json
import os.path

''' DECLARING PERSON CLASS '''
class Person():

    ''' CLASS ATTRIBUTES '''
    EYES_COLORS = ["Blue", "Green", "Brown"]
    GENRES = ["Female", "Male"]

    ''' CONSTRUCTOR and PRIVATE ATTRIBUTES '''
    def __init__(self, id, first_name, date_of_birth, genre, eyes_color):
        if type(id) is not int or id < 0:
            raise Exception("id is not an integer")
        if type(first_name) is not str or not first_name:
            raise Exception("first_name is not a string")
        if len(date_of_birth) != 3:
            raise Exception("date_of_birth is not a valid date")
        if date_of_birth[0] < 1 or date_of_birth[0] > 12:
            raise Exception("date_of_birth is not a valid date")
        if date_of_birth[1] < 1 or date_of_birth[1] > 31:
            raise Exception("date_of_birth is not a valid date")
        if type(genre) is not str or genre not in Person.GENRES:
            raise Exception("genre is not valid")
        if type(eyes_color) is not str or eyes_color not in Person.EYES_COLORS:
            raise Exception("eyes_color is not valid")
        self.__id = id
        self.__first_name = first_name
        self.__date_of_birth = date_of_birth
        self.__genre = genre
        self.__eyes_color = eyes_color

        ''' PUBLIC ATTRIBUTES '''
        self.last_name = "Smith"
        self.is_married_to = 0
        self.children = []

    ''' GETTERS '''
    def get_id(self):
        return self.__id
    
    def get_eyes_color(self):
        return self.__eyes_color

    def get_genre(self):
        return self.__genre

    def get_date_of_birth(self):
        return self.__date_of_birth

    def get_first_name(self):
        return self.__first_name

    ''' HANDLING COMPARATORS '''
    def __cmp__(self, other):
        if self.age() < other.age() : return -1
        if self.age() == other.age() : return 0 
        if self.age() > other.age() : return 1

    ''' JSON METHODS '''
    def json(self):
        dict = {
            'id': self.__id,
            'kind': self.__class__.__name__,
            'eyes_color': self.__eyes_color,
            'genre': self.__genre,
            'date_of_birth': self.__date_of_birth,
            'first_name': self.__first_name,
            'last_name': self.last_name,
            'is_married_to': self.is_married_to
            }
        return dict

    def load_from_json(self, json):
        if type(json) is not dict:
            raise Exception("json is not valid")
        self.__id = json['id']
        self.__eyes_color = json['eyes_color']
        self.__genre = json['genre']
        self.__date_of_birth = json['date_of_birth']
        self.__first_name = json['first_name']
        self.last_name = json['last_name']
        self.is_married_to = json['is_married_to']

    ''' METHOD DEFAULTS FOR SUBCLASSES '''
    def can_run(self):
        return True

    def need_help(self):
        return True

    def is_young(self):
        return True
    
    def can_vote(self):
        return True

    def can_be_married(self):
        return True

    def can_have_child(self):
        return False

    ''' PUBLIC METHODS '''
    def __str__(self):
        return self.__first_name + " " + self.last_name

    def is_male(self):
        if self.__genre == "Male":
            return True
        else:
            return False

    def age(self):
        if self.__date_of_birth[0] > 5 and self.__date_of_birth[1] > 20:
            return (2015 - self.__date_of_birth[2])
        else:
            return (2016 - self.__date_of_birth[2])

    def is_married(self):
        return (self.is_married_to != 0)

    def divorce(self, p):
        self.is_married_to = 0
        p.is_married_to = 0

    def just_married_with(self, p):
        if self.can_be_married() or p.can_be_married() == False:
            raise Exception("Can't be married")
        if self.is_married_to != 0 or p.is_married_to != 0:
            raise Exception("Already married")
        self.is_married_to = p.__id
        p.is_married_to = self.__id
        if self.__genre == "Male":
            p.last_name = self.last_name
        if p.__genre == "Male":
            self.last_name = p.last_name

    def has_child_with(self, p, id, first_name, date_of_birth, genre, eyes_color):
        if p is None or p.can_have_child == False:
            raise Exception("p is not an Adult or Senior")
        if self is None or self.can_have_child == False:
            raise Exception("self is not an Adult or Senior")
        if type(id) is not int or id < 0:
            raise Exception("id is not an integer")
        if not first_name or type(first_name) is not str:
            raise Exception("string is not a string")
        if len(date_of_birth) != 3:
            raise Exception("date_of_birth is not a valid date")
        if date_of_birth[0] < 1 or date_of_birth[0] > 12:
            raise Exception("date_of_birth is not a valid date")
        if date_of_birth[1] < 1 or date_of_birth[1] > 31:
            raise Exception("date_of_birth is not a valid date")
        if type(genre) is not str or genre not in Person.GENRES:
            raise Exception("genre is not valid")
        if type(eyes_color) is not str or eyes_color not in Person.EYES_COLORS:
            raise Exception("eyes_color is not valid")
        self.children.append(id)
        p.children.append(id)
        baby = Baby(Person)
        baby.__id = id
        baby.__first_name = first_name
        baby.__date_of_birth = date_of_birth
        baby.__genre = genre
        baby.__eyes_color = eyes_color
        return baby

    def adopt_child(self, c):
        if self.can_have_child() == False:
            raise Exception("Can't adopt a person")
        if c.__class__.__name__ != "Baby" or c.__class__.__name__ != "Teenager":
            raise Exception("Can't be adopted")
        self.children.append(c.get_id())

''' OTHER FAMILY CLASSES '''
class Baby(Person):

    def can_run(self):
        return False
    def can_vote(self):
        return False
    def can_be_married(self):
        return False

class Teenager(Person):

    def need_help(self):
        return False
    def can_vote(self):
        return False
    def can_be_married(self):
        return False

class Adult(Person):

    def need_help(self):
        return False
    def is_young(self):
        return False
    def can_have_child(self):
        return True

class Senior(Person):

    def can_run(self):
        return False
    def is_young(self):
        return False

''' JSON FUNCTIONS '''
def save_to_file(list, filename):
    if type(filename) is not str or os.path.exists(filename) == False:
        raise Exception("filename is not valid or doesn't exit")

    for i in range(len(list)):
        list[i] = list[i].json()
    file = open(filename, 'w')        
    string = json.dumps(list)
    file.write(string)
    file.close()

def load_from_file(filename):
    if type(filename) is not str or os.path.exists(filename) == False:
        raise Exception("filename is not valid or doesn't exit")
    j = open(filename, 'r')
    contents = j.read()
    j.close()
    
    data = json.loads(contents)
    person_array = []
    for i in range(len(data)):
        if 'kind' in data[i]:
            if data[i]['kind'] == "Baby":
                person = Baby(0, "first_name", [01, 01, 2000], "Male", "Green")
            if data[i]['kind'] == "Teenager":
                person = Teenager(0, "first_name", [01, 01, 2000], "Male", "Green")
            if data[i]['kind'] == "Adult":
                person = Adult(0, "first_name", [01, 01, 2000], "Male", "Green")
            if data[i]['kind'] == "Senior":
                person = Senior(0, "first_name", [01, 01, 2000], "Male", "Green")
        else:
            person = Person(0, "first_name", [01, 01, 2000], "Male", "Green")
        person.load_from_json(data[i])
        person_array.append(person)

    return person_array
