from manager import PasswordManager
from cryptography.fernet import Fernet

# pm = PasswordManager(input("enter password"))
# pm.get_key()
x = Fernet.generate_key()
print(x)
x_list = list(x.decode())

for index in range(len(x_list)):
    print(f"{index}")