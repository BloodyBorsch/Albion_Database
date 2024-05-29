from flet import *
from Data_Controller import Data_Base
from enum import Enum


class Data_Table:

    def __init__(self, db: Data_Base):
        self.data = db
        self.default_table = Table_name.RUNES
        self.current_status = Status_type.NONE

        self.tables_list = list()
        self.expected_tables = dict()
        self.items_menu_elems = list()
        self.runes_menu_elems = list()

        self.selected_id = 0
        self.items_columns_names = [
            "Id",
            "Name",
            "Tier",
            "Start price",
            "Price lvl 2",
            "Price lvl 3",
            "Runes count",
            "Actions",
        ]
        self.runes_columns_names = [
            "Id",
            "Name",
            "T4 price",
            "T5 price",
            "T6 price",
            "T7 price",
            "T8 price",
            "Actions",
        ]

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

        self.items_data_table.rows.clear()
        self.show_data(page)

        page.snack_bar = SnackBar(Text(text, size=30), bgcolor=color)
        page.snack_bar.open = True
        page.update()

    def create_fields(self, page: Page):
        page.title = "Main FLET application"

        self.items_menu_elems.append(
            TextField(hint_text="Enter name of item", width=300)
        )
        self.items_menu_elems.append(TextField(hint_text="Enter Tier", width=300))
        self.items_menu_elems.append(
            TextField(hint_text="Enter start price", width=300)
        )
        self.items_menu_elems.append(
            TextField(hint_text="Enter price lvl 2", width=300)
        )
        self.items_menu_elems.append(
            TextField(hint_text="Enter price lvl 3", width=300)
        )
        self.items_menu_elems.append(
            TextField(hint_text="Enter runes count", width=300)
        )

        self.runes_menu_elems.append(
            TextField(hint_text="Enter name of rune", width=300)
        )
        self.runes_menu_elems.append(
            TextField(hint_text="Enter tier 4 price", width=300)
        )
        self.runes_menu_elems.append(
            TextField(hint_text="Enter tier 5 price", width=300)
        )
        self.runes_menu_elems.append(
            TextField(hint_text="Enter tier 6 price", width=300)
        )
        self.runes_menu_elems.append(
            TextField(hint_text="Enter tier 7 price", width=300)
        )
        self.runes_menu_elems.append(
            TextField(hint_text="Enter tier 8 price", width=300)
        )

    def create_menus(self, page: Page):

        self.tables_list = self.data.get_tables()
        for table in self.tables_list:
            if table == "items":
                self.expected_tables[Table_name.ITEMS] = table
            elif table == "runes":
                self.expected_tables[Table_name.RUNES] = table
            else:
                print("can't get table")

        self.tables_dropdown = Dropdown(
            width=100,
            options=[dropdown.Option(x.title()) for x in self.tables_list],
        )        

        def save_items_data(e):
            try:
                match self.current_status:
                    case Status_type.INSERT:
                        self.data.insert_data(self.items_menu_elems)
                        self.show_status(page, Status_type.INSERT)
                    case Status_type.UPDATE:
                        self.data.update_items_data(
                            self.items_menu_elems[0].value.title(),
                            self.items_menu_elems[1].value,
                            self.items_menu_elems[2].value,
                            self.items_menu_elems[3].value,
                            self.items_menu_elems[4].value,
                            self.items_menu_elems[5].value,
                            self.selected_id,
                        )
                        self.show_status(page, Status_type.UPDATE)
                    case _:
                        print("Error in case save_items_data")

                self.pop_up_items_menu.open = False
                page.update()
                self.clear_fields(page)

            except Exception as e:
                print(e)
                print("Got error save_items_data!")

        def save_runes_data(e):
            try:
                self.data.update_runes_data(
                    self.runes_menu_elems[0].value.title(),
                    self.runes_menu_elems[1].value,
                    self.runes_menu_elems[2].value,
                    self.runes_menu_elems[3].value,
                    self.runes_menu_elems[4].value,
                    self.runes_menu_elems[5].value,
                    self.selected_id,
                )
                self.show_status(page, Status_type.UPDATE)

                self.pop_up_runes_menu.open = False
                page.update()
                self.clear_fields(page)

            except Exception as e:
                print(e)
                print("Got error save_runes_data!")


        self.pop_up_items_menu = AlertDialog(
            title=Text("Edit menu"),
            content=Column(self.items_menu_elems),
            actions=[TextButton("Save", on_click=save_items_data)],
        )

        self.pop_up_runes_menu = AlertDialog(
            title=Text("Edit menu"),
            content=Column(self.runes_menu_elems),
            actions=[TextButton("Save", on_click=save_runes_data)],
        )
        
        self.show_data(page)

    def clear_fields(self, page: Page):
        self.selected_id = 0

        for menu in self.items_menu_elems:
            menu.value = ""

        for menu in self.runes_menu_elems:
            menu.value = ""

    def show_data(self, page: Page):
        match self.default_table:
            case Table_name.ITEMS:
                self.show_items_data(page)
            case Table_name.RUNES:
                self.show_runes_data(page)
            case _:
                print("Error in show data!")

    def show_items_data(self, page: Page):

        rows = self.data.select_from_items()

        def add_command(e):
            self.current_status = Status_type.INSERT

            try:
                self.clear_fields(page)
                self.pop_up_items_menu.open = True
                page.update()

            except Exception as e:
                print(e)
                print(f"Got error add_clicked!")

            page.update()

        self.items_data_table = DataTable(              ### TODO разнести по методам отображение данных
            columns=[
                DataColumn(Text(self.items_columns_names[0])),
                DataColumn(Text(self.items_columns_names[1])),
                DataColumn(Text(self.items_columns_names[2])),
                DataColumn(Text(self.items_columns_names[3])),
                DataColumn(Text(self.items_columns_names[4])),
                DataColumn(Text(self.items_columns_names[5])),
                DataColumn(Text(self.items_columns_names[6])),
                DataColumn(Text(self.items_columns_names[7])),
            ],
            rows=[],
        )

        first_row = Row(
            [
                ElevatedButton("Insert data", on_click=add_command),
                self.tables_dropdown,
            ]
        )

        page.add(
            Column(
                [
                    first_row,
                    self.items_data_table,
                ]
            ),
            self.pop_up_items_menu,
        )        

        def delete_command(e):
            print("Selected id is = ", e.control.data["id"])
            self.selected_id = e.control.data["id"]
            try:
                self.data.delete_data(self.selected_id)
                self.show_status(page, Status_type.DELETE)
            except Exception as e:
                print(e)
                print("Got error delete_command!")

        def edit_command(e):
            self.current_status = Status_type.UPDATE

            self.selected_id = e.control.data["id"]
            self.items_menu_elems[0].value = e.control.data["item_name"]
            self.items_menu_elems[1].value = e.control.data["Tier"]
            self.items_menu_elems[2].value = e.control.data["Start_price"]
            self.items_menu_elems[3].value = e.control.data["Price_2"]
            self.items_menu_elems[4].value = e.control.data["Price_3"]
            self.items_menu_elems[5].value = e.control.data["Runes_count"]

            self.pop_up_items_menu.open = True
            page.update()

        for row in rows:
            self.items_data_table.rows.append(
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

    def show_runes_data(self, page: Page):

        rows = self.data.select_from_runes()

        self.items_data_table = DataTable(
            columns=[
                DataColumn(Text(self.runes_columns_names[0])),
                DataColumn(Text(self.runes_columns_names[1])),
                DataColumn(Text(self.runes_columns_names[2])),
                DataColumn(Text(self.runes_columns_names[3])),
                DataColumn(Text(self.runes_columns_names[4])),
                DataColumn(Text(self.runes_columns_names[5])),
                DataColumn(Text(self.runes_columns_names[6])),
                DataColumn(Text(self.runes_columns_names[7])),
            ],
            rows=[],
        )

        first_row = Row(
            [                
                self.tables_dropdown,
            ]
        )

        page.add(
            Column(
                [
                    first_row,
                    self.items_data_table,
                ]
            ),
            self.pop_up_runes_menu,
        )        

        def edit_command(e):
            self.current_status = Status_type.UPDATE

            self.selected_id = e.control.data["id"]
            self.runes_menu_elems[0].value = e.control.data["rune_name"]
            self.runes_menu_elems[1].value = e.control.data["Tier4_price"]
            self.runes_menu_elems[2].value = e.control.data["Tier5_price"]
            self.runes_menu_elems[3].value = e.control.data["Tier6_price"]
            self.runes_menu_elems[4].value = e.control.data["Tier7_price"]
            self.runes_menu_elems[5].value = e.control.data["Tier8_price"]

            self.pop_up_runes_menu.open = True
            page.update()

        for row in rows:
            self.items_data_table.rows.append(
                DataRow(
                    cells=[
                        DataCell(Text(row["id"])),
                        DataCell(Text(row["rune_name"])),
                        DataCell(Text(row["Tier4_price"])),
                        DataCell(Text(row["Tier5_price"])),
                        DataCell(Text(row["Tier6_price"])),
                        DataCell(Text(row["Tier7_price"])),
                        DataCell(Text(row["Tier8_price"])),
                        DataCell(
                            Row(
                                [
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


class Table_name(Enum):
    ITEMS = 1
    RUNES = 2
    NONE = 3
