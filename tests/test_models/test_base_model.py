#!/usr/bin/python3
""""Test of base model class"""


from datetime import datetime
from time import sleep
import unittest
import json
from models.base_model import BaseModel
from models import storage
import os

class TestBaseModel(unittest.TestCase):

    def test_1(self):
        b = BaseModel()
        self.assertEqual(type(b.id), str)
        self.assertEqual(type(b.created_at), datetime)
        
    def test_2(self):
        b = BaseModel()
        b_update = b.updated_at
        sleep(0.04)
        b.save()
        self.assertLess(b_update, b.updated_at)
    
    def test_3(self):
        b = BaseModel()
        self.assertEqual(str(b), "[{}] ({}) {}".format(b.__class__.__name__, b.id, b.__dict__))

    def test_4(self):
        b = BaseModel()
        b_dict = dict(b.__dict__)
        b_dict["__class__"] = "BaseModel"
        b_dict["created_at"] = b_dict["created_at"].isoformat()
        b_dict["updated_at"] = b_dict["updated_at"].isoformat()
        self.assertDictEqual(b_dict, b.to_dict())

    def testSave(self):
        b = BaseModel()
        b.save()
        with open('file.json', 'r') as f:
            self.assertIn("BaseModel", f.read())
