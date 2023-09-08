from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

START = "\nEnter 'a' to book a seat, \n 'l' to see seats occupied, \n 'f' to find a booking, \n or 'q' to quit "
class Booking(Base):
    __tablename__ = 'bookings'
    id = Column(Integer, primary_key=True, autoincrement=True)
    vehiclename = Column(String)
    passengername = Column(String)
    timedate = Column(DateTime, default=datetime.now)
    vehiclemake = Column(String)

# Create a SQLite database
engine = create_engine('sqlite:///bookings.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

def add_booking():
    vehiclename = input("Enter vehiclename of booking: ")
    passengername = input("Enter passengername of booking: ")
    vehiclemake = input("Enter vehiclemake of booking: ")

    # Create a new Booking object and add it to the database
    booking = Booking(vehiclename=vehiclename, passengername=passengername, vehiclemake=vehiclemake)
    session.add(booking)
    session.commit()
    print("Booking added successfully.")

def list_occupied_seats():
    bookings = session.query(Booking).all()
    if not bookings:
        print("No bookings available.")
    else:
        print("Occupied Seats:")
        for booking in bookings:
            print(f"ID: {booking.id}, Passenger Name: {booking.passengername}, Vehicle Name: {booking.vehiclename}")

def find_booking():
    search_name = input("Enter passengername to search for: ")
    bookings = session.query(Booking).filter_by(passengername=search_name).all()
    if not bookings:
        print(f"No booking found for passengername: {search_name}")
    else:
        print("Found Bookings:")
        for booking in bookings:
            print(f"ID: {booking.id}, Passenger Name: {booking.passengername}, Vehicle Name: {booking.vehiclename}")

user_selection = {
    'a': add_booking,
    'l': list_occupied_seats,
    'f': find_booking
}

START = "\nEnter 'a' to book a seat, 'l' to see seats occupied, 'f' to find a booking, or 'q' to quit "

def menu():
    while True:
        selection = input(START).lower()
        if selection == 'q':
            break
        if selection in user_selection:
            selected_action = user_selection[selection]
            selected_action()
        else:
            print("Unknown command. Please choose within available options: 'a', 'f', 'l' or 'q' to close the app.")

if __name__ == "__main__":
    menu()

# booking = []
# START = "\nEnter 'a' to book a seat, \n 'l' to see seats occupied, \n 'f' to find a booking, \n or 'q' to quit "

# def add_booking():
#     vehiclename = input("Enter vehiclename of booking: ")
#     passengername = input("Enter passengername of booking: ")
#     timedate = input("Enter timedate of departure of booking: ")
#     vehiclemake = input("Enter vehiclemake of booking: ")
#     booking.append({
#         'vehiclename': vehiclename,
#         'passengername': passengername,
#         'timedate': timedate,
#         'vehiclemake': vehiclemake
#     })

# def list_occupied_seats():
#     print("Occupied Seats:")
#     for index, booking_info in enumerate(booking, start=1):
#         print(f"Seat {index}: {booking_info['passengername']} in {booking_info['vehiclename']}")

# def find_booking():
#     search_name = input("Enter passengername to search for: ")
#     found = False
#     for booking_info in booking:
#         if booking_info['passengername'] == search_name:
#             print("Booking found:")
#             print(f"Vehicle Name: {booking_info['vehiclename']}")
#             print(f"Passenger Name: {booking_info['passengername']}")
#             print(f"Time and Date of Departure: {booking_info['timedate']}")
#             print(f"Vehicle Make: {booking_info['vehiclemake']}")
#             found = True
#             break
#     if not found:
#         print(f"No booking found for passengername: {search_name}")

# while True:
#     print(START)
#     choice = input("Enter your choice: ").strip().lower()

#     if choice == 'a':
#         add_booking()
#     elif choice == 'l':
#         list_occupied_seats()
#     elif choice == 'f':
#         find_booking()
#     elif choice == 'q':
#         print("Quitting the program.")
#         break
#     else:
#         print("Invalid choice. Please try again.")



# booking = []

# def add_booking():
#     vehiclename = input("Enter vehiclename of booking: ")
#     passengername = input("Enter passengername of booking: ")
#     timedate = input("Enter timedate of departure of booking: ")
#     vehiclemake = input("Enter vehiclemake of booking: ")
#     booking.append({
#         'vehiclename': vehiclename,
#         'passengername': passengername,
#         'timedate': timedate,
#         'vehiclemake': vehiclemake
#     })

# def list_occupied_seats():
#     print("Occupied Seats:")
#     for index, booking_info in enumerate(booking, start=1):
#         print(f"Seat {index}: {booking_info['passengername']} in {booking_info['vehiclename']}")

# def find_booking():
#     search_name = input("Enter passengername to search for: ")
#     found = False
#     for booking_info in booking:
#         if booking_info['passengername'] == search_name:
#             print("Booking found:")
#             print(f"Vehicle Name: {booking_info['vehiclename']}")
#             print(f"Passenger Name: {booking_info['passengername']}")
#             print(f"Time and Date of Departure: {booking_info['timedate']}")
#             print(f"Vehicle Make: {booking_info['vehiclemake']}")
#             found = True
#             break
#     if not found:
#         print(f"No booking found for passengername: {search_name}")

# while True:
#     print(START)
#     choice = input("Enter your choice: ").strip().lower()

#     if choice == 'a':
#         add_booking()
#     elif choice == 'l':
#         list_occupied_seats()
#     elif choice == 'f':
#         find_booking()
#     elif choice == 'q':
#         print("Quitting the program.")
#         break
#     else:
#         print("Invalid choice. Please try again.")





