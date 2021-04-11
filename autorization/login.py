import pymysql
from pymysql.cursors import DictCursor


connect = pymysql.connect(
                      host = 'localhost',\
                      user = 'stanok',\
                      password = 'cnfyjr11101984',\
                      database = 'stanok',\
                      cursorclass = pymysql.cursors.DictCursor)

cursor = connect.cursor()


def teacher():
    menu = input('Для просмотра информации введите 1, для редактирования 2, для выхода ПРОБЕЛ:')
    if menu == '1':
        if menu == '1':
            sql = "SELECT*FROM progress WHERE login = %s"
            data = [input('Введите логин ученика:')]
            cursor.execute(sql, data)
            resultat = cursor.fetchall()
            print(resultat)

teacher()