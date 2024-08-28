import pymysql

connection = pymysql.connect(host='localhost', port=3306, user='root', passwd='123456', db='test', charset='utf8')

try:
    with connection:
        with connection.cursor() as cursor:
            # 建立一条记录
            sql = "insert into users (name, password) values (%s, %s)"
            cursor.execute(sql, ('webmaster', 'very-secret'))

        # connection 不能自动提交数据，必须手动提交
        connection.commit()

        with connection.cursor() as cursor:
            sql = "select * from users"
            cursor.execute(sql)
            result = cursor.fetchall()
            print(result)
except pymysql.Error as e:
    connection.rollback()
finally:
    connection.close()
