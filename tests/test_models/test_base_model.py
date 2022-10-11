#!/usr/bin/python3
""""Test of base model class"""


from datetime import datetime
import unittest
import json
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):

    def test_1(self):
        b = BaseModel()
        self.assertEqual(type(b.id), str)
        self.assertEqual(type(b.created_at), datetime)
        self.assertEqual(type(b.updated_at), datetime)