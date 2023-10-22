import pymysql.cursors
import pandas as pd
import NameDB
#import openpyxl


def check_db() -> None:
    try:
        conn = pymysql.connect(host='localhost',
                               user='root',
                               password='root',
                               cursorclass=pymysql.cursors.Cursor)
        cursor = conn.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS `%s`" % NameDB.namedb.get_name_db())
    except pymysql.err.ProgrammingError as e:
        print(e)

    conn = pymysql.connect(host='localhost',
                           user='root',
                           password='root',
                           database=NameDB.namedb.get_name_db(),
                           cursorclass=pymysql.cursors.Cursor)
    cursor = conn.cursor()
    print("База данных подключена")

    try:
        cursor.execute("SELECT * FROM %s" % NameDB.namedb.get_name_tb())
    except pymysql.err.MySQLError:
        with open('create_structure.sql', 'r') as sql_file:
            sql_script = sql_file.read()
            cursor.execute(sql_script % NameDB.namedb.get_name_tb())
            conn.commit()
            print("Скрипт SQL успешно выполнен")
    return


def save_result(operation, result):
    try:
        conn = pymysql.connect(host='localhost',
                               user='root',
                               password='root',
                               database=NameDB.namedb.get_name_db(),
                               cursorclass=pymysql.cursors.Cursor)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO " + NameDB.namedb.get_name_tb() + f" (operat, result) VALUES (%s, %s)",
                       (operation, str(result)))
        conn.commit()

        conn = pymysql.connect(host='localhost',
                               user='root',
                               password='root',
                               database=NameDB.namedb.get_name_db(),
                               cursorclass=pymysql.cursors.Cursor)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM " + NameDB.namedb.get_name_tb())
        print(cursor.fetchall()[-1])
    except pymysql.err.DataError as e:
        print('Ошибка с данными:', e)
    except pymysql.err.DatabaseError as e:
        print(e)
    return


def save_db_to_xlxs():
    try:
        conn = pymysql.connect(host='localhost',
                               user='root',
                               password='root',
                               database=NameDB.namedb.get_name_db(),
                               cursorclass=pymysql.cursors.Cursor)
        new_df = pd.read_sql("SELECT * FROM " + NameDB.namedb.get_name_tb(), conn)
        file1 = (input("Введите имя файла с расширением xlsx: "))
        new_df.to_excel(file1)
        print(new_df)
    except pymysql.err.DatabaseError as e:
        print(e)
    return
