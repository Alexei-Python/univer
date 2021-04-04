import pymysql
from pymysql.cursors import DictCursor

connect = pymysql.connect(
                          host = 'localhost',\
                          user = 'stanok',\
                          password = 'cnfyjr11101984',\
                          database = 'stanok',\
                          cursorclass = pymysql.cursors.DictCursor)

cursor = connect.cursor()



def start():
    while True:
        menu = input("Введите '1', если хотите зарегистрироваться или '2', если хотите войти:")
        if menu == '1':
            log()
            break
        elif menu == '2':
            enter()
            break
        else:
            print('Повторите попытку.')

def log():
    login = input('Введите логин (максимум 20 символов):')
    password = input('Введите пароль (максимум 10 цифр):')
    password = password[::-1]
    change = input('Введите 1, если вы ученик или 2, если вы преподователь:')
    stat = ''
    fuck = input('Введите факультет:')
    year = input('Введите курс:')
    floor = input('Введите ваш пол male/female:')
    if change == '1':
        stat = '0'
    if change == '2':
        stat = '1'
    else:
        print('Введите корректные значения')
    sql = "INSERT INTO people (login, password, status, fuckulty, course, sex) VALUES(%s, %s, %s, %s, %s, %s)"
    data = [login, password, stat, fuck, year, floor]
    cursor.execute(sql, data)
    connect.commit()


def enter():
    while True:
        login = input('Введите логин:')
        password = input('Введите пароль:')
        password = password[::-1]
        user = {'login': login, 'password': int(password)}
        sql = "SELECT login, password FROM people"
        cursor.execute(sql)
        person = cursor.fetchall()
        if user in person:
            sql = "SELECT status FROM people WHERE login = %s"
            cursor.execute(sql, login)
            stat = cursor.fetchall()
            for element in stat:
                if element['status'] == '1':
                    print('welcome, ser!')
            break
        else:
            print('Неверный логин или пароль')




def status():
    sql = "SELECT status FROM people WHERE login = 'stanok"
    cursor.execute(sql)
    stat = cursor.fetchall()
    for element in stat:
        if element['status'] == '1':
            print('welcome, ser!')


enter()
