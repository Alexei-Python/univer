import pymysql
import sqlbase
from pymysql.cursors import DictCursor
from sqlbase import Sqltext


def start():
    while True:
        menu = input("Введите '1' для регистрации или '2' для входа:")
        if menu == '1':
            log()
            break
        elif menu == '2':
            enter()
            break
        else:
            print('Повторите попытку.')


def log():
    name = input('Введите логин (максимум 20 символов):')
    password = input('Введите пароль (максимум 10 знаков):')
    password = password[::-1]
    fuck = input('Введите факультет:')
    year = input('Введите курс:')
    floor = input('Введите ваш пол male/female:')
    data = [name, password, 0, fuck, year, floor]
    data_p = [name, year, fuck]
    Sqltext.log_sql(data, data_p)
    print('Вы успешно зарегестрированы. Войдите в систему')
    start()


def enter():
    while True:
        name = input('Введите логин:')
        password = input('Введите пароль:')
        password = password[::-1]
        user = {'login': name, 'password': password}
        persons = sqlbase.Sqltext.enter_pers()
        if user in persons:
            stat = sqlbase.Sqltext.enter_stat(name)
            for element in stat:
                if element['status'] == '1':
                    print('Welcome, Sir!')
                    teacher()
                else:
                    student(name)
            break
        else:
            print('Неверный логин или пароль')


def student(name):
    menu = input('Для просмотра информации введите 1. Для выхода нажмите ПРОБЕЛ: ')
    if menu == '1':
        sqlbase.Sqltext.student_look(name)
    elif menu == ' ':
        start()
    else:
        print('Введите корректные значения')
    start()


def teacher():
    menu = input('Для просмотра информации введите 1, для редактирования 2, для выхода ПРОБЕЛ:')
    if menu == '1':
        sqlbase.Sqltext.teacher_look()
        teacher()
    elif menu == '2':
        teacher_edit()
    elif menu == ' ':
        start()
    else:
        print('Ошибка в выборе')
        teacher()

def teacher_edit():
    login = sqlbase.Sqltext.teacher_look()
    while True:
        chage = input('Для редактирования введите 1 - математика, 2 - физика, 3 - пайтон, 4 - язык,'
                      '5 - курс, 6 - статус. для выхода нажмите ПРОБЕЛ:')
        if chage == '1':
            sqlbase.Sqltext.teacher_math(login)
            print('Оценка по математике изменена.')
            teacher_edit()
        elif chage == '2':
            sqlbase.Sqltext.teacher_physic(login)
            print('Оценка по физике изменена.')
            teacher_edit()
        elif chage == '3':
            sqlbase.Sqltext.teacher_python(login)
            print('Оценка по Пайтону изменена.')
            teacher_edit()
        elif chage == '4':
            sqlbase.Sqltext.teacher_lang(login)
            print('Оценка по языку изменена.')
            teacher_edit()
        elif chage == '5':
            sqlbase.Sqltext.teacher_course(login)
            print('Ученик переведен на другой курс.')
            teacher_edit()
        elif chage == '6':
            sqlbase.Sqltext.teacher_status(login)
            print('Статус успешно изменен.')
            teacher_edit()
        elif chage == ' ':
            teacher()
        else:
            print('Повторите ввод.')
            teacher_edit()

start()