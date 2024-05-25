import time
import flet as ft
from Data_Controller import DB
from Interface_functions import print_info


class Flet_View:

    def __init__(self, db: DB):
        self.data = db
        self.tables_list = list()
        ft.app(self.show_tables)

    def show_tables(self, page: ft.Page):
        page.title = "Main FLET application"        

        def show(e):
            self.tables_list = self.data.get_tables()
            [page.add(ft.Text(x)) for x in self.tables_list]                
        
        page.add(ft.Row([ft.ElevatedButton("Show Tables", on_click=show)]))    

    def first_test(self, page: ft.Page):
        page.title = "Flet counter example"
        page.vertical_alignment = ft.MainAxisAlignment.CENTER

        self.txt_number = ft.TextField(
            value="0", text_align=ft.TextAlign.RIGHT, width=100
        )

        def minus_click(e):
            self.txt_number.value = str(int(self.txt_number.value) - 1)
            page.update()

        def plus_click(e):
            self.txt_number.value = str(int(self.txt_number.value) + 1)
            page.update()

        page.add(
            ft.Row(
                [
                    ft.IconButton(ft.icons.REMOVE, on_click=minus_click),
                    self.txt_number,
                    ft.IconButton(ft.icons.ADD, on_click=plus_click),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
            )
        )

    def second_test(self, page: ft.Page):
        page.title = "Flet text example"

        def add_clicked(e):
            page.add(ft.Checkbox(label=new_task.value))
            new_task.value = ""
            new_task.focus()
            new_task.update()

        new_task = ft.TextField(hint_text="What's needs to be done?", width=300)
        page.add(ft.Row([new_task, ft.ElevatedButton("Add", on_click=add_clicked)]))

        # def button_clicked(e):
        #     page.add(ft.Text("Clicked!"))

        # page.add(ft.ElevatedButton(text="Click me", on_click=button_clicked))

        # for i in range(10):
        #     page.controls.append(ft.Text(f"Line {i}"))
        #     if i > 4:
        #         page.controls.pop(0)
        #     page.update()
        #     time.sleep(0.3)
        
        # self.t = ft.Text()
        # page.add(self.t)

        # page.add(
        #     ft.Row(controls=[
        #         ft.TextField(label="Your name"),
        #         ft.ElevatedButton(text="Say my name!")
        #     ])
        #)

        # for i in range(10):
        #     self.t.value = f"Step {i}"
        #     page.update()
        #     time.sleep(1)

        # page.controls.append(self.t)
        # page.update()

    def third_test(self, page: ft.Page):

        ### TEXT

        # def btn_click(e):
        #     if not txt_name.value:
        #         txt_name.error_text = "Please enter your name"
        #         page.update()
        #     else:
        #         name = txt_name.value
        #         page.clean()
        #         page.add(ft.Text(f"Hello, {name}!"))

        # txt_name = ft.TextField(label="Your name")
        # page.add(txt_name, ft.ElevatedButton("Say hello!", on_click=btn_click))

        ### CHECKBOX

        # def checkbox_changed(e):
        #     output_text.value = (
        #         f"You have learned how to ski :  {todo_check.value}."
        #     )
        #     page.update()

        # output_text = ft.Text()
        # todo_check = ft.Checkbox(label="ToDo: Learn how to use ski", value=False, on_change=checkbox_changed)
        # page.add(todo_check, output_text)

        ### DROPDOWN

        def button_clicked(e):
            output_text.value = f"Dropdown value is:  {color_dropdown.value}"
            page.update()

        output_text = ft.Text()
        submit_btn = ft.ElevatedButton(text="Submit", on_click=button_clicked)
        color_dropdown = ft.Dropdown(
            width=100,
            options=[
                ft.dropdown.Option("Red"),
                ft.dropdown.Option("Green"),
                ft.dropdown.Option("Blue"),
            ],
        )
        page.add(color_dropdown, submit_btn, output_text)
