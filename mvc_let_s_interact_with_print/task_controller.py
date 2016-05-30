import Tkinter as tk
from task_model import TaskModel
from task_view import TaskView

class TaskController():

    # Constructor
    def __init__(self, master, model):
        '''
        if self.master != tk.Tk():
            Exception("master is not a tk.Tk()")
        '''
        if isinstance(model, TaskModel) == False:
            Exception("model is not a TaskModel")
        self.__model = model

        # Creates the view
        self.__view = TaskView(master)

        # Link View Elements to Controller
        self.__view.toggle_button.config(command=self.reverse_string)

        self.title_change(self.__model.get_title())


    # Action to Model from View elements
    def reverse_string(self):
        self.__model.set_callback_title(self.title_change)
        self.__model.toggle()
        
    # Updates View from Model
    def title_change(self, title):
        self.__view.update_title(title)
