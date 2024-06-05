import pymysql


class SQL_Base:

    def __init__(self, connector: pymysql.connections.Connection):
        self.connection = connector
        self.cursor = connector.cursor()
        self.fetch_number = 10

    def select_items_by_name(self, name):
        sql = "SELECT * FROM items WHERE item_name = %s;"
        val = name
        self.cursor.execute(sql, val)
        result = self.cursor.fetchmany(self.fetch_number)
        return result

    def get_items(self):
        self.cursor.execute("SELECT * FROM items;")
        result = self.cursor.fetchmany(self.fetch_number)
        return result
    
    def get_all_items(self):
        self.cursor.execute("SELECT * FROM items;")
        result = self.cursor.fetchall()
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
        self.cursor.execute(sql_insert_command, [x for x in inserted_data])
        self.connection.commit()

    def update_items_data(self, inserted_data):
        sql = "UPDATE items SET item_name = %s, Tier = %s, Start_price = %s, Price_2 = %s, Price_3 = %s, Runes_count = %s WHERE id = %s;"
        val = [x for x in inserted_data]
        self.cursor.execute(sql, val)
        self.connection.commit()

    def update_runes_data(self, inserted_data):
        sql = "UPDATE runes SET rune_name = %s, Tier4_price = %s, Tier5_price = %s, Tier6_price = %s, Tier7_price = %s, Tier8_price = %s WHERE id = %s;"
        val = [x for x in inserted_data]
        self.cursor.execute(sql, val)
        self.connection.commit()

    def delete_data(self, id):
        sql = "DELETE FROM items WHERE id = %s;"
        val = id
        self.cursor.execute(sql, val)
        self.connection.commit()
