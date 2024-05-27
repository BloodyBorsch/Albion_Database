USE albion_db;
CREATE TABLE IF NOT EXISTS runes (
			id int PRIMARY KEY AUTO_INCREMENT,
            rune_name varchar(32),
            Tier4_price int,
            Tier5_price int, 
            Tier6_price int);
CREATE TABLE IF NOT EXISTS items (
			id int PRIMARY KEY AUTO_INCREMENT,
            item_name varchar(32),
            Tier int,
            Start_price int, 
            Price_2 int,
            Price_3 int,
            Runes_count int);
SHOW TABLES;
SHOW COLUMNS FROM items;
SELECT * FROM items;
