import os
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

START = "\nEnter 'a' to add a schedule, \n 'l' to see your schedules, \n 'f' to find a schedule by vehiclename, \n or 'q' to quit: "
class Schedule(Base):
    __tablename__ = 'schedules'
    id = Column(Integer, primary_key=True, autoincrement=True)
    vehiclename = Column(String)
    destination = Column(String)
    departuretime = Column(String)

# Create a SQLite database
engine = create_engine('sqlite:///schedules.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

def add_schedule():
    vehiclename = input("Enter vehiclename of the schedule: ")
    destination = input("Enter destination of the schedule: ")
    departuretime = input("Enter departuretime of the schedule: ")

    # Create a new Schedule object and add it to the database
    schedule = Schedule(vehiclename=vehiclename, destination=destination, departuretime=departuretime)
    session.add(schedule)
    session.commit()
    print("Schedule added successfully.")

def list_schedules():
    schedules = session.query(Schedule).all()
    if not schedules:
        print("No schedules available.")
    else:
        for schedule in schedules:
            print(f"Vehiclename: {schedule.vehiclename}, Destination: {schedule.destination}, Departuretime: {schedule.departuretime}")

def find_schedule():
    search_vehiclename = input('Enter vehiclename you are looking for: ')
    schedule = session.query(Schedule).filter_by(vehiclename=search_vehiclename).first()
    if schedule:
        print_schedule_info(schedule)
    else:
        print('Requested schedule was not found in the collection.')

def print_schedule_info(schedule):
    print('Here is information about the requested vehiclename')
    print(f'Vehiclename: {schedule.vehiclename},')
    print(f'Destination: {schedule.destination},')
    print(f'Departuretime: {schedule.departuretime},')

user_selection = {
    'a': add_schedule,
    'l': list_schedules,
    'f': find_schedule
}

def menu():
    selection = input(START).lower()
    while selection != 'q':
        if selection in user_selection:
            selected_action = user_selection[selection]
            selected_action()
        else:
            print("Unknown command. Please choose within available options: 'a', 'f', 'l' or 'q' to close the app.")
        selection = input(START)
    print('Thank you for using the app. See you next time!')

if __name__ == '__main__':
    menu()

# schedules = []
# START = "\nEnter 'a' to add a schedule, \n 'l' to see your schedules, \n 'f' to find a schedule by vehiclename, \n or 'q' to quit: "

# def add_schedule():
#     vehiclename = input ("Enter vehiclename of the schedule: ")
#     destination = input ("Enter destination of the schedule: ")
#     departuretime = input ("Enter departuretime of the schedule: ")
#     schedules.append ({
#         'vehiclename' : vehiclename,
#         'destination' : destination,
#         'departuretime' : departuretime,
#     })

# def list_schedules():
#     quantity = len(schedules)
#     vehiclenames = [schedule['vehiclename'] for schedule in schedules]
#     vehiclenames = ', '.join(vehiclenames)

#     if quantity:
#         print(f'You have following schedules available: {vehiclenames}. In total you have {quantity} {"schedule" if quantity == 1 else "schedules"}.')
#     else:
#         print('There are no schedules available today.')


# def print_schedule_info(schedule):
#     print('Here is information about requested vehiclename')
#     print(f'Vehiclename: {schedule["vehiclename"]},')
#     print(f'Destination: {schedule["destination"]},')
#     print(f'Departuretime: {schedule["year"]},')


# def find_schedule():
#         search_schedule= input('Enter schedule you are looking for: ')
#         for schedule in schedules:
#             if schedule['vehiclename'] == search_vehiclename:
#                 print schedule_info(schedule)
#             else:
#                 print('Requested schedule was not found in the collection.')


# user_selection = {
#     'a': add_schedule,
#     'l': list_schedules,
#     'f': find_schedule
# }


# def menu():
#     selection = input(START).lower()
#     while selection != 'q':
#         if selection in user_selection:
#             selected_action = user_selection[selection]
#             selected_action()
#         else:
#             print("Unknown command. Please choose within available options: 'a', 'f', 'l' or 'q' to close the app.")
#         selection = input(START)
#     print('Thank you for using the app. See you next time!')

# if __name__ == '__main__':
#     menu()   










