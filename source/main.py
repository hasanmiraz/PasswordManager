from manager import PasswordManager
from cryptography.fernet import Fernet
from time import sleep


# enter aaa as password for testing
# for i in range(130):
#     print(i)
#     pm = PasswordManager("SEJKFGHWESRGHNFJKDSHFG", i)
#     pm.get_key()
# x = Fernet.generate_key()
# print(x)
# x_list = list(x.decode())
#
# for index in range(len(x_list)):
#     print(f"{index}")

# a = [10,20,30,40,50,60]
# print(a.index(40))
print(hash("hello"))
sleep(10)
print(hash("hello"))
sleep(5)
print(hash("hello"))
