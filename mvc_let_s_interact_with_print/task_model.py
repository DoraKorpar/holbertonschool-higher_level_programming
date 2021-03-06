class TaskModel():

    # Constructor
    def __init__(self, title):
        if type(title) is not str or not title:
            raise Exception("title is not a string")
        self.__title = title
        self.__callback_title = None

    # Getters and setters
    def get_title(self):
        return self.__title

    def set_callback_title(self, func):
        self.__callback_title = func

    def toggle(self):
        self.__title = self.__title[::-1]
        if self.__callback_title != None:
            self.__callback_title(self.__title)

    def __str__(self):
        return self.__title
