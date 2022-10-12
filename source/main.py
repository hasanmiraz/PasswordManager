from manager import PasswordManager
from cryptography.fernet import Fernet
from time import sleep
# password = input("enter password")
# code = int(input("enter code"))
pm = PasswordManager("ABCD", 12)
print(pm.key)
# key = Fernet.generate_key()
# print(key)
art = "abcdefgh"
f = Fernet(pm.key)
token = f.encrypt(art.encode())
print(token)
print(f.decrypt(token).decode())
# pm.get_key()
# pm.create_file()
# print(pm.get_key())
# print(pm.generate_key())
# print(pm.get_key())
