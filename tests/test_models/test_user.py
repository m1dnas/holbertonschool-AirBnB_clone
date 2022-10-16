#!/usr/bin/python3
"""Tests of the user class"""

import models
import unittest
from models.user import User


class TestUser(unittest.TestCase):
    """All the tests for the user class"""

    def email_test(self):
        """Test n°1: User - user.email"""
        self.assertEqual(str, type(User.email))

    def password_test(self):
        """Test n°2: User - user.password"""
        self.assertEqual(str, type(User.password))

    def firstname_test(self):
        """Test n°3: User - user.first_name"""
        self.assertEqual(str, type(User.first_name))

    def lastname_test(self):
        """Test n°4: User - user.last_name"""
        self.assertEqual(str, type(User.last_name))                                   