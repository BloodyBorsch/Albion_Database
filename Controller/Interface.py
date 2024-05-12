from tkinter import *
from tkinter import ttk
from Data_Controller import DB
from Interface_functions import print_info


class View:

    def __init__(self, db: DB):
        self.data = db

        self.root = Tk()
        self.root.title("Albion Database")
        self.icon = PhotoImage(
            file="C:\Projects\AD_Newbie_Data\Albion_Database\Controller\Meat.png"
        )
        self.root.iconphoto(False, self.icon)
        self.root.geometry("800x500+400+150")  # print(root.geometry())
        self.root.resizable(False, False)

        self.btn = ttk.Button(text="Click Me", command=self.click_button)        
        self.btn["text"] = "Тест"
        self.btn.pack()

        self.root.update()

        print_info(self.btn)

        self.root.mainloop()

    def click_button(self):
        self.data.select_all_data()
