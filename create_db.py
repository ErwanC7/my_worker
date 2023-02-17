def create_database(cursor, nosql):
    cursor.execute("CREATE DATABASE IF NOT EXISTS users")
    nosql_db = nosql["rooms"]
    return nosql_db


def create_rooms_table(nosql_db):
    nosql_collection = nosql_db["building1"]
    nosql_collection2 = nosql_db["building2"]
    return nosql_db


def create_users_table(cursor):
    cursor.execute("CREATE TABLE IF NOT EXISTS owner ("
                   "id INT UNIQUE NOT NULL AUTO_INCREMENT PRIMARY KEY,"
                   "last_name VARCHAR(255) NOT NULL,"
                   "buy_date DATE,"
                   "building VARCHAR(10) NOT NULL,"
                   "room_id INT NOT NULL UNIQUE)")

    cursor.execute("CREATE TABLE IF NOT EXISTS renter ("
                   "id INT UNIQUE NOT NULL AUTO_INCREMENT PRIMARY KEY,"
                   "last_name VARCHAR(255) NOT NULL,"
                   "building VARCHAR(10) NOT NULL,"
                   "room_id INT NOT NULL)")


def remove_all(cursor, nosql):
    cursor.execute("DROP DATABASE IF EXISTS users")
    nosql_db = nosql["rooms"]
    collist = nosql_db.list_collection_names()
    if "building1" in collist:
        nosql_db.building1.drop()
    if "building2" in collist:
        nosql_db.building2.drop()
