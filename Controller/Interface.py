from tkinter import *
from tkinter import ttk
from Data_Controller import DB
from Interface_functions import print_info


class View:

    def __init__(self, db: DB):
        self.data = db
        self.create_main_window()
        self.create_buttons()        
        self.create_input_fields()        

        self.root.update() 
        self.root.mainloop()

    def click_button(self):
        self.data.select_all_data()        

    def create_main_window(self):
        self.root = Tk()
        self.root.title("Albion Database")
        self.icon = PhotoImage(
            file="C:\Projects\AD_Newbie_Data\Albion_Database\Controller\Meat.png"
        )
        self.root.iconphoto(False, self.icon)
        self.root.geometry("800x500+400+150")  # print(root.geometry())
        self.root.resizable(False, False)

    def create_buttons(self):
        self.btn = ttk.Button(text="Click Me", command=self.click_button)        
        self.btn["text"] = "Тест"
        self.btn.pack()

    def create_input_fields(self):
        self.input_field = ttk.Entry()
        self.input_field.pack(anchor=NW, padx=8, pady= 8)
