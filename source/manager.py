from cryptography.fernet import Fernet


class PasswordManager:
    def __init__(self, password):
        self.password = password
        self.key = ""
        self.set_key()

    def set_key(self):
        key = "IjS2FjFfVh-0FdESMJSqRolKHUMBxHpQ4K48IEM"  # for testing
        self.key = Fernet(((self.password + key) + "=").encode())

    def get_key(self):
        print(self.key)
