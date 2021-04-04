import pymysql
from pymysql.cursors import DictCursor


connect = pymysql.connect(
                      host = 'localhost',\
                      user = 'stanok',\
                      password = 'cnfyjr11101984',\
                      database = 'stanok',\
                      cursorclass = pymysql.cursors.DictCursor)

cursor = connect.cursor()


def enter():
    login = input('Введите логин:')
    password = input('Введите пароль:')
    password = password[::-1]
    user = {'login': login, 'password': int(password)}
    sql = "SELECT login, password FROM people"
    cursor.execute(sql)
    person = cursor.fetchall()
    if user in person:
        print('ok')


enter()