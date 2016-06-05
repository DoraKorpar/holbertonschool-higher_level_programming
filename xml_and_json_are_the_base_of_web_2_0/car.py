import json
from xml.dom.minidom import Document

class Car():
    # Constructor
    def __init__(self, *args, **kwargs):
        if len(args) > 0 and isinstance(args[0], dict):
            hash = args[0]
            name = hash.get('name')
            brand = hash.get('brand')
            nb_doors = hash.get('nb_doors')
        else:
            name = kwargs.get('name')
            brand = kwargs.get('brand')
            nb_doors = kwargs.get('nb_doors')

        # Attribute exceptions
        if not name or type(name) != str:
            Exception("name is not a string")
        if not brand or type(brand) != str:
            Exception("brand is not a string")
        if type(nb_doors) != int or nb_doors < 0:
            Exception("nb_doors is not > 0")

        # Initialize
        self.__name = name
        self.__brand = brand
        self.__nb_doors = nb_doors

    # Getters
    def get_name(self):
        return self.__name

    def get_brand(self):
        return self.__brand
        
    def get_nb_doors(self):
        return self.__nb_doors

    # Setter
    def set_nb_doors(self, number):
        self.__nb_doors = number

    # returns dict of attributes
    def to_hash(self):
        return { 'name': self.__name,
                 'brand': self.__brand,
                 'nb_doors': self.__nb_doors }

    def to_json_string(self):
        json_string = json.dumps(self.to_hash())
        return json_string

    def to_xml_node(self, doc):
        car = doc.createElement('car')
        car.setAttribute('nb_doors', str(self.__nb_doors))

        name = doc.createElement('name')
        name_content = doc.createCDATASection(self.__name)
        name.appendChild(name_content)
        car.appendChild(name)

        brand = doc.createElement('brand')
        brand_content = doc.createTextNode(self.__brand)
        brand.appendChild(brand_content)
        car.appendChild(brand)
        
        return car
        
    # returns string of dict of attributes
    def __str__(self):
        return "%s %s (%d)" % (self.__name, self.__brand, self.__nb_doors)
