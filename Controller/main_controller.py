import pymysql
from Interface_app import Interface_application
from Data_Controller import SQL_Base
from config import host_sql, user_sql, password_sql, db_name_sql


if __name__ == "__main__":

    print(f"Добрый день! Вас приветствует бот SQL.")

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
            sql_data = SQL_Base(connection)
            interface = Interface_application(sql_data)
        finally:
            connection.close()
            print("Connection closed ...")

    except Exception as ex:
        print("Connection refused ...")
        print(ex)
