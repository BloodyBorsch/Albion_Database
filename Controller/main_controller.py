import pymysql
from config import host_sql, user_sql, password_sql, db_name_sql
from functions import create_table, insert_data, select_all_data, drop_table, int_parser


def work_with_data(number):

    match number:
        case 1:  # Create Table
            cursor.execute(create_table())
            print("Table creation succeed")
        case 2:  # Insert Data
            cursor.execute(insert_data())
            connection.commit()
            print("Insert data succeed")
        case 3:  # Select all
            cursor.execute(select_all_data())
            rows = cursor.fetchall()
            [print(x) for x in rows]
            print("#" * 20)
        case 4:  # Drop Table
            cursor.execute(drop_table())
        case _:
            print(f"Число должно быть от 1 до 4")
            work_with_data(int(input(f"Введите число: ")))
            return

    command, go_next = int_parser(input(f"Для продолжения введите 1: "))

    if command != 1 or not go_next:
        print("Отмена")
        return
    else:
        work_with_data(interface())
        return


def interface():
    print(
        f"\n 1 - Создание таблицы "
        "\n 2 - Ввод данных в таблицу"
        "\n 3 - Показать всю таблицу"
        "\n 4 - Очистка данных "
    )
    command, go_next = int_parser(input(f"Введите число: "))

    if not go_next:
        print(command)
        interface()
        return

    return command


if __name__ == "__main__":

    print(f"Добрый день! Вас приветствует бот SQL.")
    command = interface()

    try:
        connection = pymysql.connect(
            host=host_sql,
            port=3306,
            user=user_sql,
            password=password_sql,
            database=db_name_sql,
            cursorclass=pymysql.cursors.DictCursor,
        )

        print("Succesfully connected ...")
        print("#" * 20)

        try:
            cursor = connection.cursor()
            work_with_data(command)
        finally:
            connection.close()

    except Exception as ex:
        print("Connection refused ...")
        print(ex)
