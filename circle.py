# Class
class Circle():
    # Constructor
    def __init__(self, radius):
        self.__radius = radius
    
    def set_center(self, center):
        self.__center = center

    def get_center(self):
        return self.__center

    def set_color(self, color):
        self.__color = color

    def get_color(self):
        return self.__color

    def area(self):
        return ((self.__radius ** 2) * 3.14)
