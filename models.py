from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base



Base = declarative_base()

class Cargo(Base):
    __tablename__ = 'cargo'
    
    id = Column(Integer, primary_key=True)
    description = Column(String)


class Customer(Base):
    __tablename__ = 'customers'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)


class Vehicle(Base):
    __tablename__ = 'vehicles'
    id = Column(Integer, primary_key=True)
    model = Column(String)


class Booking(Base):
    __tablename__ = 'bookings'
    id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey('customers.id'))
    vehicle_id = Column(Integer, ForeignKey('vehicles.id'))
    rating = Column(Integer)


class Review(Base):
    __tablename__ = 'reviews'
    id = Column(Integer, primary_key=True)
    review_type = Column(String)
    entity_id = Column(Integer)  # Either customer_id or driver_id
    rating = Column(Integer)
    comment = Column(String)