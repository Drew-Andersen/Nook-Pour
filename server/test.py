import mysql.connector

connection = mysql.connector.connect(
    host="192.168.0.36",
    user="root",
    password="my-secret-pw",
    database="nookpour"
)

cursor = connection.cursor()

cursor.execute("")

connection.commit()

