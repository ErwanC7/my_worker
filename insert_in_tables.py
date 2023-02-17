from datetime import datetime


def insert_rooms(nosql_db):
    building = input("Which building ? (1 or 2)\n")
    if building == '1':
        building = 'building1'
    elif building == '2':
        building = 'building2'
    else:
        return print("Wrong input")
    owner_name = input("Owner name ?\n")
    print("Perry?")
    nosql_db[building].insert_one({"owner_name": owner_name})
    print("Perry3?")
    return print('room added to ' + building + ' owned by ' + owner_name, end='\n\n')


def insert_owner_users(cursor):
    building = input("Which building ? (1 or 2)\n")
    if building == '1':
        building = 'building1'
    elif building == '2':
        building = 'building2'
    else:
        return print("Wrong input")
    last_name = input("Last name ?\n")
    date_now = f'{datetime.now()}'
    room_id = input("Room id ?\n")
    cursor.execute(
        "INSERT INTO owner (last_name, building, buy_date, room_id) VALUES ('" + last_name + "', '" + building + "', '" + date_now + "', '" + room_id + "')")
    print('owner added with last name ' + last_name + ' and buy date ' + date_now, end='\n\n')


def insert_renter_users(cursor):
    building = input("Which building ? (1 or 2)\n")
    if building == '1':
        building = 'building1'
    elif building == '2':
        building = 'building2'
    else:
        return print("Wrong input")
    last_name = input("Last name ?\n")
    room_id = input("Room id ?\n")
    cursor.execute(
        "INSERT INTO renter (last_name, building, room_id) VALUES ('" + last_name + "', '" + building + "', '" + room_id + "')")
    return print(f'renter added with last name {last_name} and room id {room_id} in building {building}', end='\n\n')


def insert_users(cursor):
    cursor.execute("USE users")
    user_type = input("Which type of user ? (owner or renter)\n")

    if user_type != 'owner' and user_type != 'renter':
        print("Wrong input")
    if user_type == 'owner':
        return insert_owner_users(cursor)
    elif user_type == 'renter':
        return insert_renter_users(cursor)
    else:
        return print("Wrong input")
