from cryptography.fernet import Fernet
import os


class PasswordManager:
    def __init__(self, password, place):
        self.password = password
        self.key = ""
        self.__set_key(place)

    def __set_key(self, place_number):
        password_list = list(self.password)
        key_list = list(("h8dbpqTNFfcFa1RcCjKfFxxEzN3VYSDoDhzxSpdGDJo"))
        places = []

        for i in range(len(password_list)):
            places.append(place_number*(i+1))

        for index_number in places:
            holder = index_number
            if holder >= len(key_list):
                rem = holder % len(key_list)
                while rem in places:
                    if rem < len(key_list):
                        rem += 1
                places[places.index(index_number)] = rem

        iteration = 0

        for index_number in places:
            key_list[index_number] = password_list[iteration]
            iteration += 1

        print(key_list)
        print()

    def get_key(self):
        print(self.key)

    def create_file(self):
        path = "code.txt"
        if not os.path.exists(path):
            open("code.txt","x")