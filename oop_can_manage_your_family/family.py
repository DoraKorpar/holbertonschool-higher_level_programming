class Person():
    ''' CLASS ATTRIBUTES '''
    EYES_COLORS = ["Blue", "Green", "Brown"]
    GENRES = ["Female", "Male"]

    ''' CONSTRUCTOR '''
    def __init__(self, id, first_name, date_of_birth, genre, eyes_color):
        if type(id) is not int or id < 0:
            raise Exception("id is not an integer")
        self.__id = id

        if type(first_name) is not str or not first_name:
            raise Exception("first_name is not a string")
        self.__first_name = first_name
        
        if len(date_of_birth) != 3:
            raise Exception("date_of_birth is not a valid date")
        if date_of_birth[0] < 1 or date_of_birth[0] > 12:
            raise Exception("date_of_birth is not a valid date")
        if date_of_birth[1] < 1 or date_of_birth[1] > 31:
            raise Exception("date_of_birth is not a valid date")
        self.__date_of_birth = date_of_birth

        if type(genre) is not str or genre not in Person.GENRES:
            raise Exception("genre is not valid")
        self.__genre = genre

        if type(eyes_color) is not str or eyes_color not in Person.EYES_COLORS:
            raise Exception("eyes_color is not valid")
        self.__eyes_color = eyes_color

    ''' GETTERS '''
    def last_name(self):
        self.last_name = last_name

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
