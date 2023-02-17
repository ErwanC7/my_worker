import sys
import mysql.connector
import pymongo

from create_db import create_database, create_users_table, remove_all, create_rooms_table
from insert_in_tables import insert_rooms, insert_users


def get_inputs(cursor, nosql_db):
    user_input = input("Which database you want to fill ? (rooms / users, or exit to leave)\n")

    while user_input != 'exit':
        if user_input == 'rooms':
            try:
                insert_rooms(nosql_db)
            except Exception as err:
                print(err)
        elif user_input == 'users':
            try:
                insert_users(cursor)
            except Exception as err:
                print(err)
        else:
            print("Wrong input")
        user_input = input("Which database you want to fill ? (rooms / users, or exit to leave)\n")


def main(argc, argv):

    # connection to the server
    sql_db = mysql.connector.connect(
        user='root', password='password', host='127.0.0.1')
    nosql = pymongo.MongoClient("mongodb://localhost:27017/")

    # create a cursor on the server (to execute queries)
    cursor = sql_db.cursor()

    # Remove all databases
    if argc == 2 and (argv[1] == '-r' or argv[1] == '--remove'):
        remove_all(cursor, nosql)

    # Create databases with tables
    nosql_db = create_database(cursor, nosql)
    create_rooms_table(nosql_db)
    cursor.execute("USE users")
    create_users_table(cursor)

    # Get inputs
    get_inputs(cursor, nosql_db)

    # send everything ?
    sql_db.commit()

    # Close *
    cursor.close()
    sql_db.close()


if __name__ == '__main__':
    main(len(sys.argv), sys.argv)
