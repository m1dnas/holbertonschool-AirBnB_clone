#!/usr/bin/python3
"""Test of the state class"""

import models
import unittest
from models.state import State


class TestState_instantiation(unittest.TestCase):
    """Test for the state class"""

    def test_name_is_public_class_attribute(self):
        self.assertEqual(str, type(State.name))