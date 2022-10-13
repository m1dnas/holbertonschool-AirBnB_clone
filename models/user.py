#!/usr/bin/python3
""""the user of the console"""

from models.base_model import BaseModel

class User(BaseModel):
    """"the class of user"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
