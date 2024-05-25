import flet as ft
from Data_Controller import DB
from Interface_functions import print_info


class Flet_View:

    def __init__(self, db: DB):
        ft.app(self.main)

    def main(self, page: ft.Page):
        page.title = "Flet counter example"
        page.vertical_alignment = ft.MainAxisAlignment.CENTER

        self.txt_number = ft.TextField(value="0", text_align=ft.TextAlign.RIGHT, width=100)

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