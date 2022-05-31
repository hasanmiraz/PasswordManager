from cryptography.fernet import Fernet


class PasswordManager:
    def __init__(self, password, place):
        self.password = password
        self.key = ""
        self.__set_key(place)

    def __set_key(self, place_number):
        password_list = list(self.password)
        key_list = list(("h8dbpqTNFfcFa1RcCjKfFxxEzN3VYSDoDhzxSpdGDJo").lower())

        # print(f"keylen = {len(key_list)}")    # debug
        # print(f"keylen = {key_list}")  # debug
        places = []
        for i in range(len(password_list)):
            # print(i)
            places.append(place_number*(i+1))
        for index_number in places:
            holder = index_number
            if holder >= len(key_list):
                rem = holder % len(key_list)
                while rem in places:
                    if rem < len(key_list):
                        rem += 1
                places[places.index(index_number)] = rem

        print(f"places list = {places}")   # debug
        # places.sort()   # debug
        # print(f"sorted places list = {places}")   # debug

        print(f"len_places = {len(places)}")  # debug

        iteration = 0
        for index_number in places:
            key_list[index_number] = password_list[iteration]
            iteration += 1
        print(key_list)
        print()
        # self.key = Fernet((key + "=").encode())

    def get_key(self):
        print(self.key)
