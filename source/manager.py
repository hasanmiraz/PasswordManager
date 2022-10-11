from cryptography.fernet import Fernet
import os


class PasswordManager:
    def __init__(self, password, place):
        self.password = password
        self.place = place
        # self.key = self.__get_key
        self.__set_key()
        self.create_file()

    def __set_key(self):
        password_list = list(self.password)
        place_number = self.place
        # print(f"the type is : {type(self.key())}")
        key_list = list(self.__get_key.lower())
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
        # pass

    @staticmethod
    def create_file():
        path1 = "code.txt"
        path2 = "data.txt"
        if not os.path.exists(path1):
            open("code.txt", "x")
        if not os.path.exists(path2):
            open("data.txt", "x")

    @property
    def __get_key(self):
        key = open("code.txt", "r")
        return key.read()

    def __generate_key(self):
        file = open("code.txt", "w")
        for i in range(20):
            key = str(Fernet.generate_key())
            key = key[2: -2]
            file.write(key+"\n")

