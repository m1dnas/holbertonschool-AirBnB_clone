#!/usr/bin/python3
""""Test of file storage"""


import os
import unittest
from models import storage
import models
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import json


class TestFileStorage(unittest.TestCase):
    """Testing for FileStorage class"""

    def testFile(self):
        self.assertEqual(str, type(FileStorage._FileStorage__file_path))

    def testObj(self):
        self.assertEqual(dict, type(FileStorage._FileStorage__objects))

    def testAll(self):
        dictionary = storage.all()
        self.assertEqual(type(dictionary), dict)

    def testNew(self):
        new = storage.all().copy()
        storage.new(BaseModel())
        self.assertNotEqual(new, storage.all())

    def test_save(self):
        with self.assertRaises(TypeError):
            models.storage.save(None)

    def test_reload(self):
        self.assertRaises(TypeError, models.storage.reload())
