import pymysql

conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='123456', db='test')

try:
    with conn:
        with conn.cursor() as cursor:
            sql = "select * from users"
            cursor.execute(sql)
            result = cursor.fetchall()
            print(result)
finally:
    conn.close()
