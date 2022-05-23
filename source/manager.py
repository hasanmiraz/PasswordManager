from cryptography.fernet import Fernet


class PasswordManager:
    def __init__(self, password, place):
        self.password = password
        self.key = ""
        self.set_key(place)

    def set_key(self):
        password_list = list(self.password)
        key = "YkzU23ER_5UigYSUtvy87IqEVVMRpz7VvvVWR7R97go"  # for testing
        key_list = list(key)
        # for key_place in key_list:
        #     if key_place

        self.key = Fernet(((self.password + key) + "=").encode())

    def get_key(self):
        print(self.key)
