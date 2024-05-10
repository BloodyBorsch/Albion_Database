import pymysql
from config import host_sql, user_sql, password_sql, db_name_sql

try:
    connection = pymysql.connect(
        host=host_sql,
        port=3306,
        user=user_sql,
        password=password_sql,
        database=db_name_sql,
        cursorclass=pymysql.cursors.DictCursor
    )
    print("Succesfully connected ...")
    print("#" * 20)

    try:
        # cursor =  connection.cursor()

        # create table
        with connection.cursor() as cursor:
            create_table_query = "CREATE TABLE users (id int AUTO_INCREMENT," \
                                 " name varchar(32)," \
                                 " password varchar(32)," \
                                 " email varchar(32), PRIMARY KEY (id));"     
            cursor.execute(create_table_query)
            print("Table creation succed")       
    finally:
        connection.close()

except Exception as ex:
    print("Connection refused ...")
    print(ex)