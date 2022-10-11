#!/usr/bin/python3
""""Test of base model class"""


from datetime import datetime
from time import sleep
import unittest
import json
from models.base_model import *
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):

    def test_1(self):
        b = BaseModel()
        self.assertEqual(type(b.id), str)
        self.assertEqual(type(b.created_at), datetime)
        b_update = b.updated_at
        sleep(0.04)
        b.save()
        self.assertLess(b_update, b.updated_at)
        self.assertEqual(str(b), "[{}] ({}) {}".format(b.__class__.__name__, b.id, b.__dict__))
        b_dict = b.to_dict()
        self.assertTrue(type(b_dict), dict)