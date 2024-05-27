import pymysql


class Data_Base:

    def __init__(self, connector: pymysql.connections.Connection):
        self.connection = connector
        self.cursor = connector.cursor()
        
    def create_table(self):
        self.cursor.execute(
            "CREATE TABLE IF NOT EXISTS users (id int AUTO_INCREMENT,"
            " name varchar(32),"
            " password varchar(32),"
            " email varchar(32), PRIMARY KEY (id));"
        )

    def select_all_data(self):
        self.cursor.execute("SELECT * FROM items;")
        result = self.cursor.fetchall()
        return result


    def get_tables(self):
        self.cursor.execute("SHOW TABLES;")
        dirty_list = self.cursor.fetchall()

        clean_list = list()

        for x in dirty_list:
            for key, val in x.items():
                clean_list.append(str(val).title())

        return clean_list

    def insert_data(self, data_tuple):
        sql_insert_command = "INSERT INTO items (item_name, Tier, Start_price, Price_2, Price_3, Runes_count) VALUES (%s,%s,%s,%s,%s,%s);"        
        self.cursor.execute(sql_insert_command, data_tuple)
        self.connection.commit()
        print(self.cursor.rowcount, "Insert data succeed")

    def update_data(self, id, product, price):
        self.cursor.execute(
            "UPDATE buy SET product=?, price=? WHERE id=?;",
            (
                product,
                price,
                id,
            ),
        )
        self.connection.commit()

    def delete_data(self, id):
        self.cursor.execute("DELETE FROM buy WHERE id=?;", (id,))
        self.connection.commit()

    def search_data(self, product="", price=""):
        self.cursor.execute("SELECT * FROM buy WHERE product=?;", (product,))
        rows = self.cursor.fetchall()
        return rows

    def drop_table(self):
        self.cursor.execute("DROP TABLE users;")
