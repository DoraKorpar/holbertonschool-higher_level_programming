import json

class Car():
    # Constructor
    def __init__(self, *args, **kwargs):
        if len(args) > 0 and isinstance(args[0], dict):
            hash = args[0]
            self.__name = hash.get('name')
            self.__brand = hash.get('brand')
            self.__nb_doors = hash.get('nb_doors')
        else:
            self.__name = kwargs.get('name')
            self.__brand = kwargs.get('brand')
            self.__nb_doors = kwargs.get('nb_doors')

        # Attribute exceptions
        if not self.__name or type(self.__name) != str:
            Exception("name is not a string")
        if not self.__brand or type(self.__brand) != str:
            Exception("brand is not a string")
        if type(self.__nb_doors) != int or self.__nb_doors < 0:
            Exception("nb_doors is not > 0")

        # Gette
    def get_name(self):
        return self.__name

    def get_brand(self):
        return self.__brand
        
    def get_nb_doors(self):
        return self.__nb_doors

    def to_hash(self):
        return { 'name': self.__name,
                 'brand': self.__brand,
                 'nb_doors': self.__nb_doors }

    def __str__(self):
        json_string = json.dumps(self.to_hash())
        return json_string
