import Tkinter as tk

class TaskView(tk.Toplevel):

    # Constructor
    def __init__(self, master):
        tk.Toplevel.__init__(self, master)
        self.protocol('WM_DELETE_WINDOW', self.master.destroy)
        if self.master != tk.Tk():
            Exception("master is not a tk.Tk()")
        self.master = master

        self.__title_var = tk.StringVar()
        self.__title_label = tk.Label(self, textvariable=self.__title_var)
        self.__title_label.pack(side='right')

        self.toggle_button = tk.Button(self, text='Reverse')
        self.toggle_button.pack(side='left')

    def update_title(self, title):
        if type(title) != str or not title:
            Exception("title is not a string")
        self.__title_var.set(title)

        
    
