from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

START = "\nEnter 'a' to add a vehicle, 'l' to see vehicles available, \n 'f'to find a vehicle by make, \n or 'q' to quit: "
class Vehicle(Base):
    __tablename__ = 'vehicles'
    id = Column(Integer, primary_key=True, autoincrement=True)
    model = Column(String)
    driver = Column(String)
    experience = Column(Integer)
    number = Column(Integer)

# Create a SQLite database
engine = create_engine('sqlite:///vehicles.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

def add_vehicle():
    model = input("Enter model of the vehicle: ")
    driver = input("Enter driver of the vehicle: ")
    experience = input("Enter experience of the vehicle: ")
    number = input("Enter number the vehicle can carry: ")

    # Create a new Vehicle object and add it to the database
    vehicle = Vehicle(model=model, driver=driver, experience=experience, number=number)
    session.add(vehicle)
    session.commit()
    print("Vehicle added successfully.")

def list_vehicles():
    vehicles = session.query(Vehicle).all()
    if not vehicles:
        print("No vehicles available.")
    else:
        print("Vehicle List:")
        for vehicle in vehicles:
            print(f"ID: {vehicle.id}, Model: {vehicle.model}, Driver: {vehicle.driver}, Experience: {vehicle.experience}, Number: {vehicle.number}")

def find_vehicle():
    search_model = input('Enter model you are looking for: ')
    vehicles = session.query(Vehicle).filter_by(model=search_model).all()
    if not vehicles:
        print('Requested model is not available in the collection.')
    else:
        print("Found Vehicles:")
        for vehicle in vehicles:
            print(f"ID: {vehicle.id}, Model: {vehicle.model}, Driver: {vehicle.driver}, Experience: {vehicle.experience}, Number: {vehicle.number}")

user_selection = {
    'a': add_vehicle,
    'l': list_vehicles,
    'f': find_vehicle
}

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

# vehicles = []
# START = "\nEnter 'a' to add a vehicle, 'l' to see vehicles available, \n 'f'to find a vehicle by make, \n or 'q' to quit: "


# def add_vehicle():
#     model = input("Enter model of the vehicle: ")
#     driver = input("Enter driver of the vehicle: ")
#     experience = input("Enter experience of the vehicle: ")
#     number = input("Enter number the vehicle can carry: ")
#     vehicles.append({
#         'model': model,
#         'driver': driver,
#         'experience': experience,
#         'number': number
#     })

# def list_vehicles():
#     quantity = len(vehicles)
#     if quantity == 0:
#         print("No vehicles available.")
#     else:
#         for vehicle in vehicles:
#             model = vehicle['model']
#             print(f'Model: {model}')

# def print_vehicle_info(vehicle):
#     print('Here is information about the requested model:')
#     print(f'Model: {vehicle["model"]},')
#     print(f'Driver: {vehicle["driver"]},')
#     print(f'Experience: {vehicle["experience"]},')
#     print(f'Number: {vehicle["number"]}.')

# def find_vehicle():
#     search_model = input('Enter model you are looking for: ')
#     found = False
#     for vehicle in vehicles:
#         if vehicle['model'] == search_model:
#             print_vehicle_info(vehicle)
#             found = True
#     if not found:
#         print('Requested model is not available in the collection.')

# def menu():
#     while True:
#         user_input = input("Enter 'a' to add a vehicle, 'l' to see vehicles available, 'f' to find a vehicle by make, or 'q' to quit: ")

#         if user_input == 'a':
#             add_vehicle()
#         elif user_input == 'l':
#             list_vehicles()
#         elif user_input == 'f':
#             find_vehicle()
#         elif user_input == 'q':
#             break
#         else:
#             print("Invalid input. Please try again.")

# if __name__ == "__main__":
#     menu()
