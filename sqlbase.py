import pymysql
from pymysql.cursors import DictCursor


connect = pymysql.connect(
                      host = 'localhost',\
                      user = 'stanok',\
                      password = 'cnfyjr11101984',\
                      database = 'stanok',\
                      cursorclass = pymysql.cursors.DictCursor)

cursor = connect.cursor()


def teacher_look():
    sql = "SELECT*FROM progress WHERE login = %s"
    data = [input('Введите логин ученика:')]
    cursor.execute(sql, data)
    resultat = cursor.fetchall()
    return login

def teacher_math():
    sql = "UPDATE progress SET math = %s WHERE login LIKE %s"
    data = [input('Введите значение:')]
    cursor.execute(sql, data, login)
    connect.commit()

def teacher_physic():
    sql = "UPDATE progress SET physic = %s WHERE login LIKE %s"
    data = [input('Введите значение:')]
    cursor.execute(sql, data, login)
    connect.commit()

def teacher_python():
    sql = "UPDATE progress SET python = %s WHERE login LIKE %s"
    data = [input('Введите значение:')]
    cursor.execute(sql, data, login)
    connect.commit()

def teacher_lang():
    sql = "UPDATE progress SET lang = %s WHERE login LIKE %s"
    data = [input('Введите значение:')]
    cursor.execute(sql, data, login)
    connect.commit()

def teacher_course():
    sql = "UPDATE progress SET course = %s WHERE login LIKE %s"
    data = [input('Введите значение:')]
    cursor.execute(sql, data, login)
    connect.commit()


def log_sql(data):
    sql = "INSERT INTO people (login, password, status, fuckulty, course, sex) VALUES(%s, %s, %s, %s, %s, %s)"
    cursor.execute(sql, data)
    sql_p = "INSERT INTO progress (login,course,fuckulty) SELECT login,course,fuckulty FROM people"
    cursor.execute(sql_p)
    connect.commit()

def enter_pers():
    sql = "SELECT login, password FROM people"
    sqlbase.enter_pers(sql)
    cursor.execute(sql)
    persons = cursor.fetchall()

def enter_stat():
    sql = "SELECT status FROM people WHERE login = %s"
    cursor.execute(sql, login)
    stat = cursor.fetchall()
    return stat



#"INSERT INTO progress (login,course,fuckulty) SELECT login,course,fuckulty FROM people"
#sql = 'SELECT * FROM people'
#cursor.execute(sql)
#data = cursor.fetchall()
#for element in data:
#    print(element['login'])
