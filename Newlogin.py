import pymysql
from pymysql.cursors import DictCursor
import sqlbase

connect = pymysql.connect(
                          host = 'localhost',\
                          user = 'stanok',\
                          password = 'cnfyjr11101984',\
                          database = 'stanok',\
                          cursorclass = pymysql.cursors.DictCursor)

cursor = connect.cursor()



def start():
    while True:
        menu = input("Введите '1' для зарегистрации или '2' для входа:")
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
    password = input('Введите пароль (максимум 10 знаков):')
    password = password[::-1]
    fuck = input('Введите факультет:')
    year = input('Введите курс:')
    floor = input('Введите ваш пол male/female:')
    data = [login, password, 0, fuck, year, floor]
    sqlbase.log_sql(data)
    print('Вы успешно зарегестрированы. Войдите в систему')
    start()

def enter():
    while True:
        login = input('Введите логин:')
        password = input('Введите пароль:')
        password = password[::-1]
        user = {'login': login, 'password': password}
        sqlbase.enter_pers(persons)
        person = persons
        if user in person:
            sql = "SELECT status FROM people WHERE login = %s"
            cursor.execute(sql, login)
            stat = cursor.fetchall()
            for element in stat:
                if element['status'] == '1':
                    print('welcome, ser!')
                    teacher()
                else:
                    student(login)
            break
        else:
            print('Неверный логин или пароль')


def student(login):
    menu = input('Для просмотра информации введите 1. Для выхода нажмите ПРОБЕЛ: ')
    if menu == '1':
        sql = "SELECT*FROM progress WHERE login = %s"
        data = [login]
        cursor.execute(sql, login)
        resultat = cursor.fetchall()
        print(resultat)
    elif menu == ' ':
        start()
    else:
        print('Введите корректные значения')
    start()


def teacher():
    menu = input('Для просмотра информации введите 1, для редактирования 2, для выхода ПРОБЕЛ:')
    if menu == '1':
        teacher_look(login)
        print(resultat)
    elif menu == '2':
        while True:
            teacher_look(login)
            print(resultat)
            chage = input('Для редактирования оценки или курса введите 1 - математика, 2 - физика, 3 - пайтон, 4 - язык,'
                          '5 - курс, для выхода нажмите ПРОБЕЛ:')
            if chage == '1':
                sqlbase.teacher_math(login)
            elif chage == '2':
                sqlbase.teacher_physic(login)
            elif chage == '3':
                sqlbase.teacher_python(login)
            elif chage == '4':
                sqlbase.teacher_lang(login)
            elif chage == '5':
                sqlbase.teacher_course(login)
            elif chage == ' ':
                teacher()
            else:
                print('Повторите ввод.')


start()