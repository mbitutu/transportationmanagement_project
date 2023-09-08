from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

START = "\nEnter 'a' to add a cargo, \n 'l' to see your cargo, \n 'f' to find a cargo by content, \n or 'q' to quit: "
class Cargo(Base):
    __tablename__ = 'cargo'
    id = Column(Integer, primary_key=True, autoincrement=True)
    content = Column(String)
    name = Column(String)
    contact = Column(String)
    location = Column(String)

# Create a SQLite database
engine = create_engine('sqlite:///cargo.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

def add_cargo():
    content = input("Enter the condition of the content (fragile or not fragile): ")
    name = input("Enter the name of the owner: ")
    contact = input("Enter the contact of the owner: ")
    location = input("Enter drop-off location: ")

    # Create a new Cargo object and add it to the database
    cargo = Cargo(content=content, name=name, contact=contact, location=location)
    session.add(cargo)
    session.commit()
    print("Cargo added successfully.")

def list_cargo():
    cargos = session.query(Cargo).all()
    if not cargos:
        print("No cargo available.")
    else:
        print("Cargo List:")
        for cargo in cargos:
            print(f"ID: {cargo.id}, Content: {cargo.content}, Name: {cargo.name}, Contact: {cargo.contact}, Location: {cargo.location}")

def find_cargo():
    search_content = input('Enter content you are looking for: ')
    cargos = session.query(Cargo).filter_by(content=search_content).all()
    if not cargos:
        print('Requested content was not found in the collection.')
    else:
        print("Found Cargo:")
        for cargo in cargos:
            print(f"ID: {cargo.id}, Content: {cargo.content}, Name: {cargo.name}, Contact: {cargo.contact}, Location: {cargo.location}")

user_selection = {
    'a': add_cargo,
    'l': list_cargo,
    'f': find_cargo
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

if __name__ == "__main__":
    menu()

# cargo = []
# START = "\nEnter 'a' to add a cargo, \n 'l' to see your cargo, \n 'f' to find a cargo by content, \n or 'q' to quit: "

# def add_cargo():
#     content = input ("Enter the condition of the content fragile or not fragile:")
#     name = input ("Enter the name of the owner:")
#     contact = input ("Enter the contact of the owner:")
#     location = input ("Enter dropoff location:")
#     cargo.append({
#         'content': content,
#         'name': name,
#         'contact': contact,
#         'location': location,

#     })


# def list_cargo():
#     quantity = len(cargo)
#     if quantity == 0:
#         print("No cargo available.")
#     else:
#         print("Cargo List:")
#         for index, item in enumerate(cargo, start=1):
#             print(f"Cargo {index}: {item}")


# def print_cargo_info(cargo):
#     print('Here is the information about the requested cargo')
#     print(f'Content: {cargo["content"]},')
#     print(f'Name: {cargo["name"]},')
#     print(f'Contact: {cargo["contact"]},')
#     print(f'Location: {cargo["location"]},')

# def find_cargo():
#     search_content = input('Enter content you are looking for: ')
#     for cargo in cargo:
#         if cargo['content'] == search_cargo:
#             print_cargo_info(cargo)
#         else:
#             print('Requested content was not found in the collection.')

# def list_cargo():
#     quantity = len(cargo)
#     if quantity == 0:
#         print("No cargo available.")
#     else:
#         print("Cargo List:")
#         for index, item in enumerate(cargo, start=1):
#             print(f"Cargo {index}: {item}")

# user_selection = {
#     'a': add_cargo,
#     'l': list_cargo,
#     'f': find_cargo
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


# if __name__ == "__main__":
#     menu()
    
