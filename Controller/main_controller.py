import pymysql
from Flet_Interface import Data_Table
from Data_Controller import Data_Base
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
            db = Data_Base(connection)
            #db.show_all_tables()
            interface = Data_Table(db)
        finally:
            connection.close()
            print("Connection closed ...")

    except Exception as ex:
        print("Connection refused ...")
        print(ex)
