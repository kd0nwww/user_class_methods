import unittest
from user import User
from datetime import datetime
from userservice import UserService
from userutil import UserUtil

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

        self.assertEqual(UserService.get_number(), 3)
    
    def test_find_user(self):
        # Succesful search if the key is in users
        self.assertEqual(UserService.find_user(86121), UserService.users[86121])
        # Not succesful search 
        self.assertEqual(UserService.find_user(11111), "Not Found")

    def test_delete_user(self):
        UserService.delete_user(66901)
        self.assertEqual(UserService.get_number(), 2)

        # If we pass the id that is not in 'users'
        self.assertEqual(UserService.delete_user(11111), None) 

    def test_update_user(self):
        UserService.update_user(86121, name="Kirill", surname="Donetskov", birthday=datetime(2005, 6, 17))

        self.assertEqual(UserService.users[86121].name, "Kirill")
        self.assertEqual(UserService.users[86121].surname, "Donetskov")
        self.assertEqual(UserService.users[86121].birthday, datetime(2005, 6, 17))

    def test_get_number(self):
        self.assertEqual(UserService.get_number(), 2)

class TestUserUtil(unittest.TestCase):
    def setUp(self):
        pass

    def test_validate_email(self):
        self.assertEqual(UserUtil.validate_email("kirilldonetskov@gmail.com"), True)
        self.assertEqual(UserUtil.validate_email("beks228@fdf.com"), False)

    def test_is_strong_password(self):
        self.assertEqual(UserUtil.is_strong_password("Kfds_33sAf"), True)
        self.assertEqual(UserUtil.is_strong_password("fdffff111"), False)

    def test_generate_email(self):
        self.assertEqual(UserUtil.generate_email("Beksultan", "Duishaliev", "gmail.com"), "beksultan.duishaliev@gmail.com")
        self.assertEqual(UserUtil.validate_email("beksultan.duishaliev@gmail.com"), True)