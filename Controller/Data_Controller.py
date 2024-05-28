import pymysql


class Data_Base:

    def __init__(self, connector: pymysql.connections.Connection):
        self.connection = connector
        self.cursor = connector.cursor()
        self.fetch_number = 10
        
    def create_table(self):
        self.cursor.execute(
            "CREATE TABLE IF NOT EXISTS users (id int AUTO_INCREMENT,"
            " name varchar(32),"
            " password varchar(32),"
            " email varchar(32), PRIMARY KEY (id));"
        )

    def select_all_data(self):
        self.cursor.execute("SELECT * FROM items;")
        result = self.cursor.fetchmany(self.fetch_number)
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

    def update_data(self, name, tier, start_p, p_2, p_3, count, id):
        sql = "UPDATE items SET item_name = %s, Tier = %s, Start_price = %s, Price_2 = %s, Price_3 = %s, Runes_count = %s WHERE id = %s;"
        val = (name, tier, start_p, p_2, p_3, count, id)
        self.cursor.execute(sql, val)
        self.connection.commit()        

    def delete_data(self, id):
        sql = "DELETE FROM items WHERE id = %s;"
        val = (id)
        self.cursor.execute(sql, val)
        self.connection.commit()

    def search_data(self, product="", price=""):
        self.cursor.execute("SELECT * FROM buy WHERE product=?;", (product,))
        rows = self.cursor.fetchall()
        return rows

    def drop_table(self):
        self.cursor.execute("DROP TABLE users;")
