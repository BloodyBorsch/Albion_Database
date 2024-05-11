from enum import Enum


def create_table():
    create_table_query = (
        "CREATE TABLE IF NOT EXISTS users (id int AUTO_INCREMENT,"
        " name varchar(32),"
        " password varchar(32),"
        " email varchar(32), PRIMARY KEY (id));"
    )
    return create_table_query


def insert_data():
    insert_query = "INSERT INTO users (name, password, email) VALUES ('Seth', 'Rollins', 'Rollins@gmail.com');"
    return insert_query


def select_all_data():
    select_all_rows = "SELECT * FROM users;"
    return select_all_rows


def update_data(set_cursor, set_connection):
    update_query = "UPDATE users SET password = 'xxxxx' WHERE name = 'Seth';"
    set_cursor.execute(update_query)
    set_connection.commit()


def delete_data(set_cursor, set_connection):
    delete_query = "DELETE FROM users WHERE id = 1;"
    set_cursor.execute(delete_query)
    set_connection.commit()


def drop_table():
    drop_table_query = "DROP TABLE users;"
    return drop_table_query


def int_parser(value):
    try:
        return int(value), True
    except:
        return "Вводить можно только цифры", False


class Data_types(Enum):
    test = 1
    tst2 = 2
    test3 = 3
    test4 = 4
