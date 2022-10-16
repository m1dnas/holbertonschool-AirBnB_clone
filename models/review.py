#!/usr/bin/python3
""""the review of the user"""

from models.base_model import BaseModel


class Review(BaseModel):
    """the review of place"""
    place_id = ""
    user_id = ""
    text = ""
