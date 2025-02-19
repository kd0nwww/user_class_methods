class User:
    def __init__(self, user_id, name, surname, email, password, birthday):
        self.user_id = user_id
        self.name = name
        self.surname = surname
        self.email = email
        self.password = password
        self.birthday = birthday


class UserService:

    users = {}

    @classmethod
    def add_user(cls, user):
        UserService.users[user.user_id] = user

    @classmethod
    def find_user(cls, user_id):
        user = UserService.users.get(user_id, "Not Found")
        return user
    
    @classmethod
    def delete_user(cls, user_id):
        if UserService.find_user(user_id) == "Not Found":
            print("Deletion failed. User with given id is not in the list")
            return
        else:
            del UserService.users[user_id]

    @classmethod
    def update_user(cls, user_id, **user_update):
        if UserService.find_user(user_id) == "Not Found":
            print("Update failed. User with given id is not in the list")
            return 
        else:
            for attr, value in user_update.items():
                if hasattr(UserService.users[user_id], attr):
                    setattr(UserService.users[user_id], attr, value)

    @classmethod
    def get_number(cls):
        return len(UserService.users)

class UserUtil:
    pass