#!/usr/bin/python3
"""Test of the city class"""

import models
import unittest
from models.city import City


class TestCity_instantiation(unittest.TestCase):
    """All the tests for the city class"""

    def test_state_id(self):
        """Test n°1: City - city.state_id"""
        self.assertEqual(str, type(City.state_id))

    def test_name(self):
        """Test n°2: City - city.name"""
        self.assertEqual(str, type(City.name))