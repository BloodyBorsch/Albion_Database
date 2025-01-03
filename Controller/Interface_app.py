from flet import *
from Data_Controller import SQL_Base
from Main_functions import list_parser
from enum import Enum


class Interface_application:

    def __init__(self, db: SQL_Base):
        self.data = db
        self.current_table = Table_name.NONE
        self.current_status = Status_type.START

        self.tables_list = list()
        self.items_list = list()
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

        app(self.step_forward)

    def step_forward(self, page: Page):

        match self.current_status:
            case Status_type.START:
                self.create_fields(page)
                self.create_menus(page)
                self.current_status = Status_type.WAITING
                self.current_table = Table_name.ITEMS
                self.step_forward(page)
            case Status_type.WAITING:
                self.renew_dropdown(page)
                self.show_data(page)
            case _:
                self.show_status(page)
                self.current_status = Status_type.WAITING
                self.step_forward(page)

    def show_status(self, page: Page):

        match self.current_status:
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

        page.snack_bar = SnackBar(Text(text, size=30), bgcolor=color)
        page.snack_bar.open = True
        page.update()

    def create_fields(self, page: Page):

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

    def renew_dropdown(self, page: Page):

        self.clear_fields(page)

        dirty_items_list = self.data.get_all_items()

        for x in dirty_items_list:
            if x["item_name"].title() not in self.items_list:
                self.items_list.append(x["item_name"].title())

        self.tables_dropdown.options = [
            dropdown.Option(x.title()) for x in self.tables_list
        ]

        [
            self.items_dropdown.options.append(dropdown.Option(x))
            for x in self.items_list
        ]

        page.update()

    def clear_fields(self, page: Page):
        self.data_table.rows.clear()
        self.data_table.columns.clear()
        self.items_list.clear()
        self.tables_dropdown.options.clear()
        self.items_dropdown.options.clear()

        self.selected_id = 0

        for menu in self.items_menu_elems:
            menu.value = ""

        for menu in self.runes_menu_elems:
            menu.value = ""

        page.update()

    def create_menus(self, page: Page):

        page.title = "Albion market data"

        self.tables_list = self.data.get_tables()

        for table in self.tables_list:
            if table == "items":
                self.expected_tables[table] = Table_name.ITEMS
            elif table == "runes":
                self.expected_tables[table] = Table_name.RUNES
            else:
                print("ошибка в get table!")

        self.tables_dropdown = Dropdown(
            width=100,
            options=[],
        )

        self.items_dropdown = Dropdown(
            width=300,
            options=[],
        )

        self.data_table = DataTable(
            columns=[],
            rows=[],
        )

        def save_data(e):
            try:
                match self.current_table:
                    case Table_name.ITEMS:
                        match self.current_status:
                            case Status_type.INSERT:
                                self.data.insert_data(
                                    list_parser(self.items_menu_elems)
                                )
                            case Status_type.UPDATE:
                                self.data.update_items_data(
                                    list_parser(self.items_menu_elems, self.selected_id)
                                )
                            case _:
                                print("Error in case save_items_data")
                    case Table_name.ITEMS_BY_NAME:
                        match self.current_status:
                            case Status_type.UPDATE:
                                self.data.update_items_data(
                                    list_parser(self.items_menu_elems, self.selected_id)
                                )
                    case Table_name.RUNES:
                        temp_list = list()
                        [temp_list.append(x.value) for x in self.runes_menu_elems]
                        temp_list.append(self.selected_id)
                        self.data.update_runes_data(temp_list)
                    case _:
                        print("Error in case save_runes_data")

                self.pop_up_items_menu.open = False
                self.pop_up_runes_menu.open = False
                page.update()
                self.step_forward(page)

            except Exception as e:
                print(e)
                print("Got error save_items_data!")

        self.pop_up_items_menu = AlertDialog(
            title=Text("Edit items menu"),
            content=Column(self.items_menu_elems),
            actions=[TextButton("Save", on_click=save_data)],
        )

        self.pop_up_runes_menu = AlertDialog(
            title=Text("Edit runes menu"),
            content=Column(self.runes_menu_elems),
            actions=[TextButton("Save", on_click=save_data)],
        )

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

        self.insert_button = ElevatedButton("Insert data", on_click=add_command)

        def show_chosen_items(e):
            self.current_table = Table_name.ITEMS_BY_NAME
            self.current_status = Status_type.WAITING
            self.step_forward(page)

        self.show_items_button = ElevatedButton(
            "Show items", on_click=show_chosen_items
        )

        def show_chosen_table(e):
            self.current_table = self.expected_tables[
                self.tables_dropdown.value.lower()
            ]
            self.current_status = Status_type.WAITING
            self.step_forward(page)

        first_row = Row(
            [
                self.tables_dropdown,
                ElevatedButton("Show table", on_click=show_chosen_table),
                self.items_dropdown,
                self.show_items_button,
            ]
        )

        page.add(
            Column(
                [
                    first_row,
                    self.data_table,
                    self.insert_button,
                ]
            ),
            self.pop_up_items_menu,
            self.pop_up_runes_menu,
        )

    def show_data(self, page: Page):

        match self.current_table:
            case Table_name.ITEMS:
                rows = self.data.get_items()
                self.show_items_data(page, rows)
            case Table_name.ITEMS_BY_NAME:
                rows = self.data.get_items_by_name(self.items_dropdown.value)
                self.show_items_data(page, rows)
            case Table_name.RUNES:
                rows = self.data.get_runes()
                self.show_runes_data(page, rows)
            case _:
                print("Error in show data!")

    def show_items_data(self, page: Page, rows):

        [
            self.data_table.columns.append(
                DataColumn(Text(self.items_columns_names[x]))
            )
            for x in range(len(self.items_columns_names))
        ]

        self.insert_button.disabled = False
        self.show_items_button.disabled = False

        def delete_command(e):
            self.current_status = Status_type.DELETE

            self.selected_id = e.control.data["id"]
            try:
                self.data.delete_data(self.selected_id)
                self.step_forward(page)
            except Exception as e:
                print(e)
                print("Ошибка удаления")

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

    def show_runes_data(self, page: Page, rows):

        [
            self.data_table.columns.append(
                DataColumn(Text(self.runes_columns_names[x]))
            )
            for x in range(len(self.runes_columns_names))
        ]

        self.insert_button.disabled = True
        self.show_items_button.disabled = True

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
            self.data_table.rows.append(
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
    WAITING = 4
    START = 5
    NONE = 6


class Table_name(Enum):
    ITEMS = 1
    RUNES = 2
    ITEMS_BY_NAME = 3
    NONE = 4
