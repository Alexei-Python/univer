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
            teacher()
        else:
            student(login)
        break
else:
    print('Неверный логин или пароль')