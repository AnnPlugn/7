import warnings
import random
import universal
import db

warnings.filterwarnings("ignore")


def gen_list():
    my_list = [int(i) for i in range(120)]
    total_sum = sum(my_list)
    length = len(my_list)
    total_sum = sum(my_list)
    avg = total_sum / length
    db.save_result('list', my_list)
    db.save_result('len(list)', len(my_list))
    db.save_result('sum(list)', total_sum)
    db.save_result('avg(list)', avg)
    return


def main():
    run = True
    commands = """==========================================================================
1. Создать таблицу и БД, результат сохранить в MySQL.
2. Найти, результат сохранить в MySQL.
3. Сохранить все данные из MySQL в Excel.
4. Завершить"""
    while run:
        run = universal.uni(commands,
                            db.check_db, gen_list,
                            db.save_db_to_xlxs)
    return


if __name__ == '__main__':
    main()
