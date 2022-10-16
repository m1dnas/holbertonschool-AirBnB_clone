#!/usr/bin/python3
"""Tests of the user class"""

import models
import unittest
from models.user import User


class TestUser(unittest.TestCase):
    """All the tests for the user class"""

    def test_email(self):
        """Test n°1: User - user.email"""
        self.assertEqual(str, type(User.email))

    def test_password(self):
        """Test n°2: User - user.password"""
        self.assertEqual(str, type(User.password))

    def test_firstname(self):
        """Test n°3: User - user.first_name"""
        self.assertEqual(str, type(User.first_name))

    def test_lastname(self):
        """Test n°4: User - user.last_name"""
        self.assertEqual(str, type(User.last_name))                                   
