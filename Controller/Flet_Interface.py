import time
import flet as ft
from Data_Controller import Data_Base
from Interface_functions import print_info


class Data_Table:

    def __init__(self, db: Data_Base):
        self.data = db
        self.tables_list = list()
        ft.app(self.create_table)

    def create_table(self, page: ft.Page):
        page.title = "Main FLET application"

        def add_clicked(e):  
            try:
                data_tuple = tuple()      
                data_tuple = (
                    name_data.value,
                    tier.value,
                    price1.value,
                    price2.value,
                    price3.value,
                    count.value,
                )            
                self.data.insert_data(data_tuple)
                self.data_table.rows.clear()
                self.get_data(page)

                page.snack_bar = ft.SnackBar(
                    ft.Text("Sucess added", size=30),
                    bgcolor="green"
                )
                page.snack_bar.open = True
                page.update()
            except Exception as e:
                print(e)
                print(f"Got error!")
            
            name_data.value = ""
            tier.value = ""
            price1.value = ""
            price2.value = ""
            price3.value = ""
            count.value = ""
            page.update()


        name_data = ft.TextField(hint_text="Enter name of item", width=300)
        tier = ft.TextField(hint_text="Enter Tier", width=300)
        price1 = ft.TextField(hint_text="Enter start price", width=300)
        price2 = ft.TextField(hint_text="Enter price lvl 2", width=300)
        price3 = ft.TextField(hint_text="Enter price lvl 3", width=300)
        count = ft.TextField(hint_text="Enter runes count", width=300)

        self.data_table = ft.DataTable(
            columns=[
                ft.DataColumn(ft.Text("Id")),
                ft.DataColumn(ft.Text("Name")),
                ft.DataColumn(ft.Text("Tier")),
                ft.DataColumn(ft.Text("Start price")),
                ft.DataColumn(ft.Text("Price lvl 2")),
                ft.DataColumn(ft.Text("Price lvl 3")),
                ft.DataColumn(ft.Text("Runes count")),
                ft.DataColumn(ft.Text("Actions")),

            ],
            rows=[]
        )

        first_row = ft.Row(
            [
                name_data,
                ft.ElevatedButton("Insert data", on_click=add_clicked),
                #self.data_table,
            ]
        )

        page.add(ft.Column(
            [
                first_row,
                tier,
                price1,
                price2,
                price3,
                count,
                self.data_table               
            ]
        ))  
        self.get_data(page)      

    def show_tables(self, page: ft.Page):
        page.title = "Main FLET application"

        def show(e):
            self.tables_list = self.data.get_tables()
            [page.add(ft.Text(x)) for x in self.tables_list]

            tables_dropdown = ft.Dropdown(
                width=100,
                options=[ft.dropdown.Option(x) for x in self.tables_list],
            )
            page.add(tables_dropdown)

        page.add(ft.Row([ft.ElevatedButton("Show Tables", on_click=show)]))

    def get_data(self, page: ft.Page):        
        rows = self.data.select_all_data()         
       
        def delete_command(e):
            pass

        def edit_command(e):
            pass

        for row in rows:
            self.data_table.rows.append(
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text(row["id"])),
                        ft.DataCell(ft.Text(row["item_name"])),
                        ft.DataCell(ft.Text(row["Tier"])),
                        ft.DataCell(ft.Text(row["Start_price"])),
                        ft.DataCell(ft.Text(row["Price_2"])),
                        ft.DataCell(ft.Text(row["Price_3"])),
                        ft.DataCell(ft.Text(row["Runes_count"])),
                        ft.DataCell(
                            ft.Row(
                                [
                                    ft.IconButton("delete", icon_color="red",
                                                  data=row,
                                                  on_click=delete_command),
                                    ft.IconButton("edit", icon_color="green",
                                                  data=row,
                                                  on_click=edit_command),
                                ]
                            )
                        )
                    ]
                )
            )

        page.update()
        print(f"Page updated")
            

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
        # )

        # for i in range(10):
        #     self.t.value = f"Step {i}"
        #     page.update()
        #     time.sleep(1)

        # page.controls.append(self.t)
        # page.update()

    def third_test(self, page: ft.Page):

        ### TEXT

        def btn_click(e):
            if not txt_name.value:
                txt_name.error_text = "Please enter your name"
                page.update()
            else:
                name = txt_name.value
                page.clean()
                page.add(ft.Text(f"Hello, {name}!"))

        txt_name = ft.TextField(label="Your name")
        page.add(txt_name, ft.ElevatedButton("Say hello!", on_click=btn_click))

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

        # def button_clicked(e):
        #     output_text.value = f"Dropdown value is:  {color_dropdown.value}"
        #     page.update()

        # output_text = ft.Text()
        # submit_btn = ft.ElevatedButton(text="Submit", on_click=button_clicked)
        # color_dropdown = ft.Dropdown(
        #     width=100,
        #     options=[
        #         ft.dropdown.Option("Red"),
        #         ft.dropdown.Option("Green"),
        #         ft.dropdown.Option("Blue"),
        #     ],
        # )
        # page.add(color_dropdown, submit_btn, output_text)
