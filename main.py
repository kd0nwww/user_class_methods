import unittest
from user import User
from datetime import datetime
from userservice import UserService

class TestUser(unittest.TestCase):
    def setUp(self):
        self.user = User(66221, "Kirill", "Donetskov", datetime(2005, 6, 17))

    def test_get_age(self):
        self.assertEqual(self.user.get_age(), 19)

    def test_user_id(self):
        self.assertEqual(self.user.user_id, 66221)
    
    def test_name_change(self):
        self.user.name = "Beks"
        self.assertEqual(self.user.name, "Beks")

class TestUserService(unittest.TestCase):
    def setUp(self):
        self.user = User(66901, "Magomed", "Mukhamedov", datetime(2006, 2, 19))
        self.user1 = User(86121, "Beksultan", "Duishaliev", datetime(2005, 11, 23))
        self.user2 = User(77191, "Saidusman", "Saidaliev", datetime(2004, 2, 14))
        
    def test_add_users(self):
        UserService.add_user(self.user)
        UserService.add_user(self.user1)
        UserService.add_user(self.user2)
        # checking the name
        self.assertEqual(UserService.users[66901].name, "Magomed")
        self.assertEqual(UserService.users[86121].name, "Beksultan")
        self.assertEqual(UserService.users[77191].name, "Saidusman")
    
    def test_get_number(self):
        self.assertEqual(UserService.get_number(), 3)

    def test_find_user(self):
        # Succesful search if the key is in users
        self.assertEqual(UserService.find_user(86121), UserService.users[86121])
        # Not succesful search 
        self.assertEqual(UserService.find_user(11111), "Not Found")