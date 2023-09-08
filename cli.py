import click
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Customer(Base):
    __tablename__ = 'customers'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    phone_number = Column(String)


class Vehicle(Base):
    __tablename__ = 'vehicles'
    id = Column(Integer, primary_key=True)
    license_plate = Column(String)
    make = Column(String)
    model = Column(String)
    year = Column(Integer)
engine = create_engine('sqlite:///transportation.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()
@click.group()
def main():
    pass
@main.command()
def add_customer():
    name = click.prompt('Customer name')
    email = click.prompt('Customer email')
    phone_number = click.prompt('Customer phone number')
    customer = Customer(name=name, email=email, phone_number=phone_number)
    session.add(customer)
    session.commit()
    click.echo('Customer added successfully')
@main.command()
def add_order():
    customer_id = click.prompt('Customer ID')
    pickup_location = click.prompt('Pickup location')
    dropoff_location = click.prompt('Dropoff location')
    date = click.prompt('Date')
    time = click.prompt('Time')
    order = Order(customer_id=customer_id, pickup_location=pickup_location, dropoff_location=dropoff_location, date=date, time=time)
    session.add(order

