#!/usr/bin/python3
"""Test of the amenity class"""

import models
import unittest
from models.amenity import Amenity


class TestAmenity_instantiation(unittest.TestCase):
    """The test for the amenity class"""

    def test_name_is_public_class_attribute(self):
        self.assertEqual(str, type(Amenity.name))