#!/usr/bin/python3
""""Test of base model class"""


from datetime import datetime
from time import sleep
import unittest
import json
from models.base_model import BaseModel
from models import storage

class TestBaseModel(unittest.TestCase):
    """Class of TestBaseModel"""
    
    def test_1(self):
        """Test n°1: BaseModel - self.created_at & self.id"""
        b = BaseModel()
        self.assertEqual(type(b.id), str)
        self.assertEqual(type(b.created_at), datetime)
        
    def test_2(self):
        """Test n°2: BaseModel - self.updated_at"""
        b = BaseModel()
        b_update = b.updated_at
        sleep(0.04)
        b.save()
        self.assertLess(b_update, b.updated_at)
    
    def test_3(self):
        """Test n°3: BaseModel - __str__(self)"""
        b = BaseModel()
        self.assertEqual(str(b), "[{}] ({}) {}".format(b.__class__.__name__, b.id, b.__dict__))

    def test_4(self):
        """Test n°4: BaseModel - to_dict()"""
        b = BaseModel()
        b_dict = dict(b.__dict__)
        b_dict["__class__"] = "BaseModel"
        b_dict["created_at"] = b_dict["created_at"].isoformat()
        b_dict["updated_at"] = b_dict["updated_at"].isoformat()
        self.assertDictEqual(b_dict, b.to_dict())

    def test_5(self):
        """Test n°5: BaseModel - save()"""
        b = BaseModel()
        b.save()
        with open('file.json', 'r') as f:
            self.assertIn("BaseModel", f.read())
