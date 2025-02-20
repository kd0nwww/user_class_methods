class UserUtil:

    @staticmethod
    def generate_user_id():

        from datetime import datetime
        import random

        user_id = str(datetime.now())[2:4]
        user_id += "".join([str(random.randint(1, 9)) for _ in range(7)])
        return user_id

    @staticmethod
    def generate_password():

        import random
        
        lower_characters = list("abcdefghijklmnopqrstuvwxyz")
        upper_characters = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        numbers = list("1234567890")
        symbols = list("!@#$%^&*()_=+-}?><:;,[]")

        password = []

        while len(password) < 8:

            password += ([random.choice(lower_characters) for _ in range(random.randrange(1, 5))]) 
            password += ([random.choice(upper_characters) for _ in range(random.randrange(1, 5))]) 
            password += ([random.choice(numbers) for _ in range(random.randrange(1, 5))]) 
            password += ([random.choice(symbols) for _ in range(random.randrange(1, 5))]) 

        random.shuffle(password)
        return "".join(password)

    @staticmethod
    def is_strong_password(password):

        if len(password) < 8:
            return False
 
        has_upper = False
        has_lower = False
        has_digit = False
        has_special = False
        symbols = "!@#$%^&*()-_=+[{]};:'\",<.>/?`~"

        for char in password:
            if char.isupper():
                has_upper = True
            elif char.islower():
                has_lower = True
            elif char.isdigit():
                has_digit = True
            elif char in symbols:
                has_special = True

        if not has_upper:
            return False
        if not has_lower:
            return False
        if not has_digit:
            return False
        if not has_special:
            return False

        return True
        
    @staticmethod
    def generate_email(name, surname, domain):
        return name.lower() + "." + surname.lower() + "@" + domain

    @staticmethod
    def validate_email(email):
        domains = ["gmail.com", "yahoo.com", "alatoo.edu.kg", "mail.ru"]
        if email.find("@") == -1:
            return False
        else:
            found_in_list = False
            for domain in domains:
                if domain == email.split("@")[1]:
                    found_in_list = True

            if found_in_list:
                return True
            else:
                return False