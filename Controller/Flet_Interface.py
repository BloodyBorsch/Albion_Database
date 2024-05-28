from flet import *
from Data_Controller import Data_Base
from enum import Enum


class Data_Table:

    def __init__(self, db: Data_Base):
        self.data = db
        self.tables_list = list()
        self.menu_elems = list()
        self.targeted_id = 0
        self.current_status = Status_type.NONE
        app(self.start)

    def start(self, page: Page):

        self.create_fields(page)
        self.create_menus(page)

    def show_status(self, page: Page, status):
        text, color = "", ""

        match status:
            case Status_type.INSERT:
                text = "Success added"
                color = "green"
            case Status_type.UPDATE:
                text = "Success edited"
                color = "green"
            case Status_type.DELETE:
                text = "Success deleted"
                color = "red"
            case _:
                print(f"Troubles in enum")

        self.data_table.rows.clear()
        self.show_data(page)

        page.snack_bar = SnackBar(Text(text, size=30), bgcolor=color)
        page.snack_bar.open = True
        page.update()

    def create_fields(self, page: Page):
        page.title = "Main FLET application"

        self.menu_elems.append(TextField(hint_text="Enter name of item", width=300))
        self.menu_elems.append(TextField(hint_text="Enter Tier", width=300))
        self.menu_elems.append(TextField(hint_text="Enter start price", width=300))
        self.menu_elems.append(TextField(hint_text="Enter price lvl 2", width=300))
        self.menu_elems.append(TextField(hint_text="Enter price lvl 3", width=300))
        self.menu_elems.append(TextField(hint_text="Enter runes count", width=300))

    def create_menus(self, page: Page):

        self.tables_list = self.data.get_tables()

        tables_dropdown = Dropdown(
            width=100,
            options=[dropdown.Option(x) for x in self.tables_list],
        )

        def add_command(e):
            self.current_status = Status_type.INSERT

            try:
                self.clear_fields(page)
                self.pop_up_menu.open = True
                page.update()

            except Exception as e:
                print(e)
                print(f"Got error add_clicked!")

            page.update()

        def save_data(e):
            try:
                match self.current_status:
                    case Status_type.INSERT:
                        self.data.insert_data(self.menu_elems)
                        self.show_status(page, Status_type.INSERT)
                    case Status_type.UPDATE:
                        self.data.update_data(
                            self.menu_elems[0].value,
                            self.menu_elems[1].value,
                            self.menu_elems[2].value,
                            self.menu_elems[3].value,
                            self.menu_elems[4].value,
                            self.menu_elems[5].value,
                            self.targeted_id,
                        )
                    case _:
                        print("Error in Save data")

                self.pop_up_menu.open = False
                page.update()
                self.clear_fields(page)
                self.show_status(page, Status_type.UPDATE)

            except Exception as e:
                print(e)
                print("Got error save_data!")

        self.pop_up_menu = AlertDialog(
            title=Text("Edit menu"),
            content=Column(self.menu_elems),
            actions=[TextButton("Save", on_click=save_data)],
        )

        self.data_table = DataTable(
            columns=[
                DataColumn(Text("Id")),
                DataColumn(Text("Name")),
                DataColumn(Text("Tier")),
                DataColumn(Text("Start price")),
                DataColumn(Text("Price lvl 2")),
                DataColumn(Text("Price lvl 3")),
                DataColumn(Text("Runes count")),
                DataColumn(Text("Actions")),
            ],
            rows=[],
        )

        first_row = Row(
            [
                ElevatedButton("Insert data", on_click=add_command),
                tables_dropdown,
            ]
        )

        page.add(
            Column(
                [
                    first_row,
                    self.data_table,
                ]
            ),
            self.pop_up_menu,
        )
        self.show_data(page)

    def clear_fields(self, page: Page):
        self.targeted_id = 0

        for menu in self.menu_elems:
            menu.value = ""

    def show_data(self, page: Page):
        rows = self.data.select_all_data()

        def delete_command(e):
            print("Selected id is = ", e.control.data["id"])
            self.targeted_id = e.control.data["id"]
            try:
                self.data.delete_data(self.targeted_id)
                self.show_status(page, Status_type.DELETE)
            except Exception as e:
                print(e)
                print("Got error delete_command!")

        def edit_command(e):
            self.current_status = Status_type.UPDATE

            self.targeted_id = e.control.data["id"]
            self.menu_elems[0].value = e.control.data["item_name"]
            self.menu_elems[1].value = e.control.data["Tier"]
            self.menu_elems[2].value = e.control.data["Start_price"]
            self.menu_elems[3].value = e.control.data["Price_2"]
            self.menu_elems[4].value = e.control.data["Price_3"]
            self.menu_elems[5].value = e.control.data["Runes_count"]

            self.pop_up_menu.open = True
            page.update()

        for row in rows:
            self.data_table.rows.append(
                DataRow(
                    cells=[
                        DataCell(Text(row["id"])),
                        DataCell(Text(row["item_name"])),
                        DataCell(Text(row["Tier"])),
                        DataCell(Text(row["Start_price"])),
                        DataCell(Text(row["Price_2"])),
                        DataCell(Text(row["Price_3"])),
                        DataCell(Text(row["Runes_count"])),
                        DataCell(
                            Row(
                                [
                                    IconButton(
                                        "delete",
                                        icon_color="red",
                                        data=row,
                                        on_click=delete_command,
                                    ),
                                    IconButton(
                                        "edit",
                                        icon_color="green",
                                        data=row,
                                        on_click=edit_command,
                                    ),
                                ]
                            )
                        ),
                    ]
                )
            )

        page.update()


class Status_type(Enum):
    INSERT = 1
    UPDATE = 2
    DELETE = 3
    NONE = 4
