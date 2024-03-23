#!/usr/bin/python3
import os
from dotenv import load_dotenv
from email.mime.text import MIMEText
from models.basemodel import BaseModel, Base
from random import randint
from smtplib import SMTP
from sqlalchemy import Column, String


load_dotenv()

class User(BaseModel, Base):
    if os.environ.get("PEOPLEBASE_STORAGE_TYPE") == "file":
        username = ""
        gender = ""
        email = ""
        address = ""
        phone_number = ""
        password = ""
        role = "user"
    elif os.environ.get("PEOPLEBASE_STORAGE_TYPE") == "db":
        __tablename__ = "users"
        username = Column(String(50), nullable=False, unique=True)
        gender = Column(String(10), nullable=False)
        email = Column(String(60), nullable=False, unique=True)
        address = Column(String(500), nullable=False)
        phone_number = Column(String(20), nullable=False, unique=True)
        password = Column(String(20), nullable=False)
        role = Column(String(10), default="user", nullable=False)
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
    def send_code_to_email(self):
        """This verifies is the user owns the email he/she entered"""
        verification_code = str(randint(100000, 999999))
        peoplebase_email = os.environ.get("PEOPLEBASE_EMAIL")
        peoplebase_email_password = os.environ.get("PEOPLEBASE_EMAIL_PASSWORD")
        user_email = self.email
        message = MIMEText("Hi {}, Your verification code is '{}'. Please enter it to confirm your identity.\n\nIf you didn't register for our program, Please ignore this email.\n\nThank you.".format(self.full_name, verification_code), "plain")
        message["Subject"] = "PeopleBase Verification Code"
        message["From"] = peoplebase_email
        message["To"] = user_email
        with SMTP("smtp.example.com", 587) as server:
            server.starttls()
            server.login(peoplebase_email, peoplebase_email_password)  # Replace with your credentials
            server.sendmail(peoplebase_email, user_email, message.as_string())
        self.verification_code = verification_code
        self.save()