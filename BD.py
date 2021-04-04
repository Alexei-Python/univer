import pymysql
from pymysql.cursors import DictCursor

class Connection:
    connect = pymysql.connect(
                          host = 'localhost',\
                          user = 'stanok',\
                          password = 'cnfyjr11101984',\
                          database = 'stanok',\
                          cursorclass = pymysql.cursors.DictCursor)

    cursor = connect.cursor()

"INSERT INTO progress (login,course,fuckulty) SELECT login,course,fuckulty FROM people"
#sql = 'SELECT * FROM people'
#cursor.execute(sql)
#data = cursor.fetchall()
#for element in data:
#    print(element['login'])
