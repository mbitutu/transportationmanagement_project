import os
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# Define a Review model to represent the reviews in the database
class Review(Base):
    __tablename__ = 'reviews'
    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String)
    company = Column(String)
    year = Column(Integer)
    rating = Column(Integer)

# Create a SQLite database
engine = create_engine('sqlite:///reviews.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

def add_review():
    email = input("Enter email of the review: ")
    company = input("Enter company that owns the review: ")
    year = int(input("Enter year of the review: "))
    rating = int(input("Enter rating of the review: "))

    # Create a new Review object and add it to the database
    review = Review(email=email, company=company, year=year, rating=rating)
    session.add(review)
    session.commit()
    print("Review added successfully.")

def list_reviews():
    reviews = session.query(Review).all()
    if not reviews:
        print("No reviews available.")
    else:
        for review in reviews:
            print(f"Email: {review.email}, Company: {review.company}, Year: {review.year}, Rating: {review.rating}")

def menu():
    while True:
        user_input = input("Enter 'a' to add a review, 'l' to see reviews, or 'q' to quit: ")

        if user_input == 'a':
            add_review()
        elif user_input == 'l':
            list_reviews()
        elif user_input == 'q':
            break
        else:
            print("Invalid input. Please try again.")

if __name__ == "__main__":
    menu()











# reviews = [] 

# def add_review():
#     email = input("Enter email of the review: ")
#     company = input("Enter company that owns the review: ")
#     year = input("Enter year of the review: ")
#     rating = input("Enter rating of the review: ")
#     reviews.append({
#         'email': email,
#         'company': company,
#         'year': year,
#         'rating': rating
#     })

# def list_reviews():
#     if not reviews:
#         print("No reviews available.")
#     else:
#         for review in reviews:
#             email = review['email']
#             company = review['company']
#             year = review['year']
#             rating = review['rating']
#             print(f"Email: {email}, Company: {company}, Year: {year}, Rating: {rating}")

# def menu():
#     while True:
#         user_input = input("Enter 'a' to add a review, 'l' to see reviews, or 'q' to quit: ")

#         if user_input == 'a':
#             add_review()
#         elif user_input == 'l':
#             list_reviews()
#         elif user_input == 'q':
#             break
#         else:
#             print("Invalid input. Please try again.")

# if __name__ == "__main__":
#     menu()

