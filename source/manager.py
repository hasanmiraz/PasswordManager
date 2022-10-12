from cryptography.fernet import Fernet
import os
import pickle


class PasswordManager:
    def __init__(self, password, secret_key):
        self.password = password
        self.secret_key = secret_key
        self.key
        self.__create_file()

    def encrypt_password(self):
        pass

    def decrypt_password(self):
        pass

    def __set_key(self):
        password_list = list(self.password)
        place_number = self.secret_key
        key_list = list(self.__get_key().lower())
        places = list()

        # the indexes where the password should be placed
        for i in range(len(password_list)):
            places.append(place_number * (i + 1))

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

        return ("".join(key_list)+"=").encode()
        print(key_list)
        print()

    # determining which key should we get
    def __get_specific_key(self):
        return int(self.secret_key % 20)

    @staticmethod
    def __create_file():
        path1 = "code.txt"
        path2 = "data.txt"
        if not os.path.exists(path1):
            open("code.txt", "x")
        if not os.path.exists(path2):
            open("data.txt", "x")

    # getting that key based on the index got from __get_specific_key
    def __get_key(self):
        key = open("code.txt", "r")
        all_key = key.read()
        all_key_list = all_key.split("\n")
        return all_key_list[self.__get_specific_key()]

    @staticmethod
    def __generate_key():
        file = open("code.txt", "w")
        for i in range(20):
            key = str(Fernet.generate_key())
            key = key[2: -2]
            file.write(key + "\n")
