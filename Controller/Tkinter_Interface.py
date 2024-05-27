from tkinter import *
from tkinter import ttk
from enum import Enum
from Data_Controller import Data_Base
from Interface_functions import print_info


class Tkinter_View:

    def __init__(self, db: Data_Base):
        self.menu_type = Menu_types.empty
        self.grid_size = 20
        self.data = db
        self.create_addition_windows()
        self.create_main_window()
        # self.create_input_fields()
        self.create_buttons()
        self.create_console()

        self.window.update()
        self.window.mainloop()

    def create_addition_windows(self):
        self.creation_table_menu = Create_table_menu(self.data)

    def create_main_window(self):
        self.window = Tk()
        self.window.title("Albion Database")
        self.icon = PhotoImage(
            file="C:\Projects\AD_Newbie_Data\Albion_Database\Controller\Meat.png"
        )
        self.window.iconphoto(False, self.icon)
        self.window.geometry("800x500+400+150")  # print(root.geometry())
        # self.window["bg"] = "grey"

        for c in range(self.grid_size):
            self.window.columnconfigure(index=c, weight=1)
        for r in range(self.grid_size):
            self.window.rowconfigure(index=r, weight=1)

        self.window.resizable(False, False)

    def create_buttons(self):
        self.create_btn = ttk.Button(text="Click Me", command=self.show_creation_menu)
        self.create_btn.grid(row=0, column=1, ipadx=6, ipady=6, padx=4, pady=4)

        # self.clear_btn = ttk.Button(text="Clear", command=self.clear)
        # self.clear_btn.pack(side=LEFT, anchor=N, padx=6, pady=6)

    def create_input_fields(self):
        self.input_field = ttk.Entry()
        self.input_field.pack(anchor=NW, padx=8, pady=8)

    def create_console(self):
        self.create = ttk.Label(self.window, text="Создание таблицы")
        self.create.grid(row=0, column=0, ipadx=6, ipady=6, padx=4, pady=4)

        self.insert = ttk.Label(self.window, text="Внесение данных")
        self.insert.grid(row=1, column=0, ipadx=6, ipady=6, padx=4, pady=4)

        self.select = ttk.Label(self.window, text="Поиск данных")
        self.select.grid(row=2, column=0, ipadx=6, ipady=6, padx=4, pady=4)

    def show_creation_menu(self):
        if self.menu_type == Menu_types.create:
            return

        self.menu_type = Menu_types.create
        self.creation_table_menu.show()


class Create_table_menu:

    def __init__(self, db: Data_Base):
        self.grid_size = 8
        self.data = db

    def show(self):
        self.creation_menu = Tk()
        self.creation_menu.title("Меню создания таблицы")
        self.creation_menu.geometry("600x300")

        for c in range(self.grid_size):
            self.creation_menu.columnconfigure(index=c, weight=1)
        for r in range(self.grid_size):
            self.creation_menu.rowconfigure(index=r, weight=1)

        self.creation_menu.resizable(False, False)
        self.create_rows()

    def create_rows(self):
        self.table_name = ttk.Label(self.creation_menu, text="Название таблицы: ")
        self.table_name.grid(row=0, column=0, ipadx=6, ipady=6, padx=4, pady=4)

        self.name_label = ttk.Label(self.creation_menu, text="Имя: ")
        self.name_label.grid(row=1, column=0, ipadx=6, ipady=6, padx=4, pady=4)

        self.password_label = ttk.Label(self.creation_menu, text="Пароль: ")
        self.password_label.grid(row=2, column=0, ipadx=6, ipady=6, padx=4, pady=4)

        self.mail_label = ttk.Label(self.creation_menu, text="Почта: ")
        self.mail_label.grid(row=3, column=0, ipadx=6, ipady=6, padx=4, pady=4)

        self.table_name_input = ttk.Entry(self.creation_menu)
        self.table_name_input.grid(row=0, column=1, ipadx=6, ipady=6, padx=4, pady=4)

        self.name_input = ttk.Entry(self.creation_menu)
        self.name_input.grid(row=1, column=1, ipadx=6, ipady=6, padx=4, pady=4)

        self.password_input = ttk.Entry(self.creation_menu)
        self.password_input.grid(row=2, column=1, ipadx=6, ipady=6, padx=4, pady=4)

        self.mail_input = ttk.Entry(self.creation_menu)
        self.mail_input.grid(row=3, column=1, ipadx=6, ipady=6, padx=4, pady=4)

        self.create_btn = ttk.Button(
            self.creation_menu, text="Создать", command=self.run_create
        )
        self.create_btn.grid(row=0, column=3, ipadx=6, ipady=6, padx=4, pady=4)

        self.console = ttk.Label(self.creation_menu, text="Консоль")
        self.console.grid(row=1, column=3, ipadx=6, ipady=6, padx=4, pady=4)

    def run_create(self):
        self.data.create_table()

        self.table_name_input.delete(0, END)
        self.name_input.delete(0, END)
        self.password_input.delete(0, END)
        self.mail_input.delete(0, END)


class Menu_types(Enum):
    create = 1
    insert = 2
    select = 3
    clear = 4
    empty = 5
