#!/usr/bin/python3
""""Test of file storage"""


import unittest
from models.base_model import BaseModel
from models import storage
import json

file = "file.json"


class TestFileStorage(unittest.TestCase):
    """Testing for FileStorage class"""

    def testAll(self):

        dictionary = storage.all()
        self.assertEqual(type(dictionary), dict)

    def testNew(self):

        new = storage.all().copy()
        storage.new(BaseModel())
        self.assertNotEqual(new, storage.all())

    
    