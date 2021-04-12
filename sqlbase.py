import pymysql
from pymysql.cursors import DictCursor


connect = pymysql.connect(
                      host = 'localhost',\
                      user = 'stanok',\
                      password = 'cnfyjr11101984',\
                      database = 'stanok',\
                      cursorclass = pymysql.cursors.DictCursor)

cursor = connect.cursor()

class Sqltext:
    def log_sql(data, data_p):
        sql = "INSERT INTO people (login, password, status, fuckulty, course, sex) VALUES(%s, %s, %s, %s, %s, %s)"
        cursor.execute(sql, data)
        connect.commit()
        sql_p = "INSERT INTO progress (login, course, fuckulty) VALUES(%s, %s, %s)"
        cursor.execute(sql_p, data_p)
        connect.commit()

    def enter_pers():
        sql = "SELECT login, password FROM people"
        cursor.execute(sql)
        persons = cursor.fetchall()
        return persons


    def enter_stat(login):
        sql = "SELECT status FROM people WHERE login = %s"
        cursor.execute(sql, login)
        stat = cursor.fetchall()
        return stat

    def teacher_look():
        sql = "SELECT*FROM progress WHERE login = %s"
        login = [input('Введите логин ученика:')]
        cursor.execute(sql, login)
        resultat = cursor.fetchall()
        print(resultat)
        return login

    def teacher_math(login):
        sql = "UPDATE progress SET math = %s WHERE login LIKE %s"
        data = [input('Введите значение:')]
        cursor.execute(sql, data, login)
        connect.commit()

    def teacher_physic(login):
        sql = "UPDATE progress SET physic = %s WHERE login LIKE %s"
        data = [input('Введите значение:')]
        cursor.execute(sql, data, login)
        connect.commit()

    def teacher_python(login):
        sql = "UPDATE progress SET python = %s WHERE login LIKE %s"
        data = [input('Введите значение:')]
        cursor.execute(sql, data, login)
        connect.commit()

    def teacher_lang(login):
        sql = "UPDATE progress SET lang = %s WHERE login LIKE %s"
        data = [input('Введите значение:')]
        cursor.execute(sql, data, login)
        connect.commit()

    def teacher_course(login):
        sql = "UPDATE progress SET course = %s WHERE login LIKE %s"
        data = [input('Введите значение:')]
        cursor.execute(sql, data, login)
        connect.commit()

    def teacher_status(login):
        while True:
            sql = "UPDATE people SET status = %s WHERE login LIKE %s"
            data = [input('Введите значение 0 - студент, 1 - преподаватель:')]
            if data == '1' or '2':
                continue
            else:
                print('Ошибочка.')
                teacher_status()
            cursor.execute(sql, data, login)
            connect.commit()

    def student_look(login):
        sql = "SELECT*FROM progress WHERE login = %s"
        data = [login]
        cursor.execute(sql, data)
        resultat = cursor.fetchall()
        print(resultat)
