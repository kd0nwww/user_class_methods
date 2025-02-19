class User:
    def __init__(self, user_id, name, surname, birthday, email=None, password=None):
        self.user_id = user_id
        self.name = name
        self.surname = surname
        self.email = email
        self.password = password
        self.birthday = birthday

    def get_details(self):
        return f"Name: {self.name}\nSurname: {self.surname}\nID: {self.user_id}\nBirthday: {self.birthday}\nEmail: {self.email}\nPassword: {self.password}"

    def get_age(self):
        from datetime import datetime
        from dateutil.relativedelta import relativedelta

        age = relativedelta(datetime.now(), self.birthday).years
        return age