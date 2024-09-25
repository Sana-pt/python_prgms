admins={'aa':'aa4'}
receptionists={'rr':'rr4'}
guests={}
rooms={}
reservations={}
g_c=1
r_c=1


def main_menu():
    while True:
        print("  Main Menu\n1.Admin\n2.Receptionist\n3.Guest\n4.Exit")
        choice=input("Enter a choice: ")
        if choice=='1':
            admin_login()
        elif choice=='2':
            receptionist_login()
        elif choice=='3':
            guest_menu()
        elif choice=='4':
            print("Exit")
            break
        else:
            print("Invalid choice.")


def admin_login():
    username=input("Enter username of admin: ")
    password=input("Enter password of admin: ")
    if admins.get(username)==password:
        admin_menu()
    else:
        print("Invalid Admin credentials.")

def admin_menu():
    while True:
        print("\n Admin Menu\n")
        print("1.Add Room")
        print("2.Update Room Details")
        print("3.Remove Room")
        print("4.View All Reservations")
        print("5.Generate Reports")
        print("6.Exit")
        choice=input("Enter a choice: ")
        if choice=='1':
            add_room()
        elif choice=='2':
            update_room()
        elif choice=='3':
            remove_room()
        elif choice=='4':
            view_all_reservations()
        elif choice=='5':
            generate_reports()
        elif choice=='6':
            break
        else:
            print("Invalid choice.")

def add_room():
    while True:
        room_number=input("Enter room number: ")
        if room_number in rooms:
            print("Room exists")
        else:
            break
    room_types=["single","double","suite"]
    while True:
        room_type=input("Enter room type(single/double/suite:").lower()
        if room_type in room_types:
            break
        else:
            print("Invalid room type")
    price=input("Enter price per night: ")
    rooms[room_number]={'type':room_types,'price':price,'status':'available'}
    print(f"Room {room_number} has added.")


def update_room():
    room_number=input("Enter room number to update: ")
    if room_number in rooms:
        new_price=input("Enter new price per night: ")
        valid_status=["available","occupied","reserved"]
        while True:
            new_status=input("Enter status(available,occupied,reserved): ").lower()
            if new_status in valid_status:
                break
            else:
                print("Invalid status.")
        rooms[room_number]['price'] = new_price
        rooms[room_number]['status'] = new_status
        print(f"Room {room_number} updated successfully.")
    else:
        print("Room not found.")

def remove_room():
    room_number=input("Enter room number to remove: ")
    if room_number in rooms:
        del rooms[room_number]
        print(f"Room {room_number} removed successfully.")
    else:
        print("Room not found.")

def view_all_reservations():
    if reservations:
        for res_id,details in reservations.items():
            print(f"Reservation ID:{res_id},Guest ID:{details['guest_id']},Room:{details['room_number']},Status:{details['status']}")
    else:
        print("No reservations available.")

def generate_reports():
    total_rooms=len(rooms)
    occupied_rooms=sum(1 for room in rooms.values() if room['status']=='occupied')
    available_rooms=sum(1 for room in rooms.values() if room['status']=='available')
    reserved_rooms=total_rooms-occupied_rooms -available_rooms
    revenue=sum(float(room['price']) for room in rooms.values() if room['status']=='occupied')

    print(f"Total Rooms: {total_rooms}")
    print(f"Occupied Rooms: {occupied_rooms}")
    print(f"Available Rooms: {available_rooms}")
    print(f"Reserved Rooms: {reserved_rooms}")
    print(f"Total Revenue: {revenue:.2f}")

def receptionist_login():
    username=input("Enter username of receptionist: ")
    password=input("Enter password of receptionist: ")
    if receptionists.get(username)==password:
        receptionist_menu()
    else:
        print("Invalid Receptionist credentials.")

def receptionist_menu():
    while True:
        print("\n Receptionist Menu \n")
        print("1.Check-in guest")
        print("2.Check-out guest")
        print("3.Make reservation")
        print("4.Cancel reservation")
        print("5.View available rooms")
        print("6.View guest details")
        print("7.Exit")
        choice=input("Enter a choice: ")

        if choice=='1':
            check_in_guest()
        elif choice=='2':
            check_out_guest()
        elif choice=='3':
            make_reservation()
        elif choice=='4':
            cancel_reservation()
        elif choice=='5':
            view_available_rooms()
        elif choice=='6':
            view_guest_details()
        elif choice=='7':
            break
        else:
            print("Invalid choice.")

def check_in_guest():
    g_id=input("Enter guest ID: ")
    room_number=input("Enter room number: ")
    if room_number in rooms and rooms[room_number]['status']=='reserved':
        rooms[room_number]['status']='occupied'
        print(f"Guest {g_id} checked into room {room_number}")
    else:
        print("Room not reserved.")

def check_out_guest():
    g_id=input("Enter guest ID: ")
    room_number = input("Enter room number: ")
    if room_number in rooms and rooms[room_number]['status']=='occupied':
        rooms[room_number]['status']='available'
        print(f"Guest {g_id} checked out from room {room_number}")
    else:
        print("Room not occupied.")

def make_reservation():
    global r_c
    guest_id=input("Enter guest ID: ")
    room_number=input("Enter room number: ")
    if room_number in rooms and rooms[room_number]['status']=='available':
        check_in_date=input("Enter check-in date: ")
        check_out_date=input("Enter check-out date: ")
        rooms[room_number]['status']='reserved'
        reservations[r_c]={'guest_id':guest_id,'room_number':room_number,'check_in':check_in_date,'check_out':check_out_date,'status':'reserved'}
        print(f"Reservation {r_c} created successfully.")
        r_c+= 1
    else:
        print("No room reserved.")

def cancel_reservation():
    res_id=input("Enter reservation ID: ")
    if int(res_id) in reservations:
        room_number=reservations[int(res_id)]['room_number']
        rooms[room_number]['status']='available'
        del reservations[int(res_id)]
        print("Cancelled reservetion")
    else:
        print("No room reserved")

def view_available_rooms():
    available_rooms=[room_num for room_num, details in rooms.items() if details['status']=='available']
    if available_rooms:
        for room in available_rooms:
            print(f"Room {room}:{rooms[room]}")
    else:
        print("No rooms")

def view_guest_details():
    if guests:
        for g_id,details in guests.items():
            print(f"Guest ID:{g_id},Name:{details['name']},Contact:{details['contact']}")
    else:
        print("No guest found")

def guest_menu():
    while True:
        print("\n Guest Menu \n")
        print("1.Register")
        print("2.Login")
        print("3.Exit")
        choice=input("Enter a choice: ")

        if choice=='1':
           guest_register()
        elif choice=='2':
            guest_login()
        elif choice=='3':
            break
        else:
            print("Invalid choice")

def guest_register():
    global g_c
    while True:
        g_id=input("Enter guest ID: ")
        if g_id not in guests:
            print("Invalid guest ID")
        else:
            break
    name=input("Enter name: ")
    contact=input("Enter contact details: ")
    address=input("Enter address: ")
    username=input("Enter username: ")
    if guests.get(username)==password:
        guest_menu()
    else:
        print("Invalid username.")
        return
    password=input("Enter password: ")

    guests[g_c]={'name':name,'contact':contact,'address':address,'username':username,'password':password}
    print(f"Registration successful. Your Guest ID is {g_c}")
    g_c+=1

def guest_login():
    username=input("Enter username: ")
    password=input("Enter password: ")
    g_id=None
    for gid, details in guests.items():
        if details['username']==username and details['password']==password:
            g_id=gid
            break
    if g_id:
        guest_log_menu(g_id)
    else:
        print("Invalid credentials.")

def guest_log_menu(g_id):
    while True:
        print("\n Guest Logged In Menu \n")
        print("1.View available rooms")
        print("2.Make reservation")
        print("3.View reservation status")
        print("4.Update personal information")
        print("5.Cancel reservation")
        print("6.Exit")
        choice = input("Enter choice: ")

        if choice == '1':
            view_available_rooms()
        elif choice == '2':
            make_reservation_for_guest(g_id)
        elif choice == '3':
            view_reservation_status(g_id)
        elif choice == '4':
            update_personal_information(g_id)
        elif choice == '5':
            cancel_guest_reservation(g_id)
        elif choice == '6':
            break
        else:
            print("Invalid choice")

def make_reservation_for_guest(g_id):
    global r_c
    room_number=input("Enter room number: ")
    if room_number in rooms and rooms[room_number]['status']=='available':
        check_in_date=input("Enter check-in date: ")
        check_out_date=input("Enter check-out date: ")
        rooms[room_number]['status']='reserved'
        reservations[r_c]={'guest_id':g_id,'room_number':room_number,'check_in':check_in_date,'check_out':check_out_date,'status':'reserved'}
        print(f"Reservation successfull.")
        r_c+=1
    else:
        print("no room.")

def view_reservation_status(g_id):
    guest_reservations=[res for res in reservations.values() if res['guest_id']==g_id]
    if guest_reservations:
        for res in guest_reservations:
            print(f"Room {res['room_number']},check-in:{res['check_in']},check-out:{res['check_out']},status:{res['status']}")
    else:
        print("empty reservation.")

def update_personal_information(g_id):
    contact=input("Enter new contact details: ")
    address=input("Enter new address: ")
    guests[g_id]['contact']=contact
    guests[g_id]['address']=address
    print("updated successfully.")

def cancel_guest_reservation(g_id):
    guest_reservations=[res_id for res_id, res in reservations.items() if res['g_id'] == g_id]
    if guest_reservations:
        for res_id in guest_reservations:
            room_number = reservations[res_id]['room_number']
            rooms[room_number]['status']='available'
            del reservations[res_id]
        print("cancelled successfully.")
    else:
        print("No reservations.")


main_menu()
