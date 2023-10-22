import os


class NameDB:
    def __init__(self):
        self._name_db = str(input("Введите имя БД: "))
        self._name_tb = str(input("Введите имя таблицы: "))

    def get_name_db(self):
        return self._name_db

    def get_name_tb(self):
        return self._name_tb


os.system('cls' if os.name == 'nt' else 'clear')
namedb = NameDB()