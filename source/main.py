from manager import PasswordManager
from cryptography.fernet import Fernet
from time import sleep
# password = input("enter password")
# code = int(input("enter code"))
pm = PasswordManager("abcd", 12)
# pm.get_key()
pm.create_file()