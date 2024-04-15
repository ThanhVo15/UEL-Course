print("\n1.SELECT STUDENT")
from flask import Flask
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '@Obama123'
app.config['MYSQL_DB'] = 'studentmanagement'
app.config['MYSQL_HOST'] = 'localhost'

mysql = MySQL(app)

with app.app_context():
    try:
        cursor = mysql.connection.cursor()

        cursor.execute('SELECT * FROM student')
        data = cursor.fetchall()

        print('ID\tCODE\tName')
        for item in data:
            print(f"{item[0]}\t{item[1]}\t{item[2]}")

    except Exception as e:
        print("Error = ", e)
    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'conn' in locals():
            conn.close()
        print("MySQL is closed")
print("-"*20)
#-----------------------------------------------------
print("\n2. SELECT MANY STUDENT")
app = Flask(__name__)
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '@Obama123'
app.config['MYSQL_DB'] = 'studentmanagement'
app.config['MYSQL_HOST'] = 'localhost'

mysql = MySQL(app)

with app.app_context():
    try:
        cursor = mysql.connection.cursor()

        cursor.execute('SELECT ID, CODE, Name FROM student')
        data = cursor.fetchmany(5)

        print('ID\tCODE\tName')
        for item in data:
            print(f"{item[0]}\t{item[1]}\t{item[2]}")

    except Exception as e:
        print("Error = ", e)
    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'conn' in locals():
            conn.close()
        print("MySQL is closed")
print("-"*20)
#-----------------------------------------------------
print("\n3. SELECT ONE STUDENT")
app = Flask(__name__)
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '@Obama123'
app.config['MYSQL_DB'] = 'studentmanagement'
app.config['MYSQL_HOST'] = 'localhost'

mysql = MySQL(app)

with app.app_context():
    try:
        cursor = mysql.connection.cursor()

        cursor.execute('SELECT * from student')
        data = cursor.fetchone()

        print(data)

    except Exception as e:
        print("Error = ", e)
    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'conn' in locals():
            conn.close()
        print("MySQL is closed")
print("-"*20)
#-----------------------------------------------------
print("\n4. SELECT ORDER STUDENT")
app = Flask(__name__)
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '@Obama123'
app.config['MYSQL_DB'] = 'studentmanagement'
app.config['MYSQL_HOST'] = 'localhost'

mysql = MySQL(app)

with app.app_context():
    try:
        cursor = mysql.connection.cursor()

        cursor.execute('SELECT * FROM student ORDER BY Name DESC')
        data = cursor.fetchall()

        print('ID\tCODE\tName')
        for item in data:
            print(f"{item[0]}\t{item[1]}\t{item[2]}")

    except Exception as e:
        print("Error = ", e)
    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'conn' in locals():
            conn.close()
        print("MySQL is closed")
print("-"*20)
#-----------------------------------------------------
print("\n5. SELECT PAGING STUDENT")
app = Flask(__name__)
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '@Obama123'
app.config['MYSQL_DB'] = 'studentmanagement'
app.config['MYSQL_HOST'] = 'localhost'

mysql = MySQL(app)

with app.app_context():
    try:
        cursor = mysql.connection.cursor()

        cursor.execute('SELECT * FROM student LIMIT 4 OFFSET 3')
        data = cursor.fetchall()

        print('ID\tCODE\tName')
        for item in data:
            print(f"{item[0]}\t{item[1]}\t{item[2]}")

    except Exception as e:
        print("Error = ", e)
    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'conn' in locals():
            conn.close()
        print("MySQL is closed")


