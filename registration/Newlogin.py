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
            login.enter()
            break
        else:
            print('Повторите попытку.')

def log():
    login = input('Введите логин (максимум 20 символов):')
    password = input('Введите пароль (максимум 10 цифр):')
    status = input('Введите 1, если вы ученик или 2, если вы преподователь:')
    if status == '1':
        status = '0'
    elif status == '2':
        status == 'VIP'
    else:
        print('Введите корректные значения')
    sql = "INSERT INTO people (login, password, status) VALUES(%s, %s, %s)"
    data = [login, password, status]
    cursor.execute(sql, data)
    connect.commit()

start()
