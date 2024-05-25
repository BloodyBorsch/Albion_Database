import pymysql


class DB:

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
        self.cursor.execute("SELECT * FROM users;")
        rows = self.cursor.fetchall()
        [print(x) for x in rows]
        print("#" * 20)

    def get_tables(self):
        self.cursor.execute("SHOW TABLES;")        
        dirty_list = self.cursor.fetchall()  

        [print(x) for x in dirty_list]
        
        clean_list = list()     
        
        for x in dirty_list:
            for key, val in x.items():
                #print(val)
                clean_list.append(str(val).title())
        
        return clean_list

        # print(str(*self.cursor.fetchall()).title())
        # return str(self.cursor.fetchall()).title()

    def insert_data(self, product, price, comment):
        self.cursor.execute(
            "INSERT INTO buy VALUES (NULL,?,?,?);",
            (
                product,
                price,
                comment,
            ),
        )
        self.connection.commit()
        print("Insert data succeed")

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
