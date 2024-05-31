import pymysql


class SQL_Base:

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

    def select_items_by_name(self, name):
        sql = "SELECT * FROM items WHERE item_name = %s;"
        val = name
        self.cursor.execute(sql, val)
        result = self.cursor.fetchmany(self.fetch_number)
        return result

    def select_from_items(self):
        self.cursor.execute("SELECT * FROM items;")
        result = self.cursor.fetchmany(self.fetch_number)
        return result
    
    def select_from_runes(self):
        self.cursor.execute("SELECT * FROM runes;")
        result = self.cursor.fetchmany(self.fetch_number)
        return result   

    def get_tables(self):
        self.cursor.execute("SHOW TABLES;") 
        dirty_list = self.cursor.fetchall() 
        clean_list = list()

        for x in dirty_list:
            for key, val in x.items():
                clean_list.append(str(val))

        return clean_list

    def insert_data(self, inserted_data):
        sql_insert_command = "INSERT INTO items (item_name, Tier, Start_price, Price_2, Price_3, Runes_count) VALUES (%s,%s,%s,%s,%s,%s);"        
        self.cursor.execute(sql_insert_command, [x.value for x in inserted_data])
        self.connection.commit()
        print(self.cursor.rowcount, "Insert data succeed")

    def update_items_data(self, name, tier, price_s, price_2, price_3, count, id):
        sql = "UPDATE items SET item_name = %s, Tier = %s, Start_price = %s, Price_2 = %s, Price_3 = %s, Runes_count = %s WHERE id = %s;"
        val = (name.title(), tier, price_s, price_2, price_3, count, id)
        self.cursor.execute(sql, val)
        self.connection.commit()   

    def update_runes_data(self, name, tier4, tier5, tier6, tier7, tier8, id):
        sql = "UPDATE runes SET rune_name = %s, Tier4_price = %s, Tier5_price = %s, Tier6_price = %s, Tier7_price = %s, Tier8_price = %s WHERE id = %s;"
        val = (name.title(), tier4, tier5, tier6, tier7, tier8, id)
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
