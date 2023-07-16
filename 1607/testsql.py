import sqlite3

conn = sqlite3.connect("D:\Якубовская\sql\mySQL.sqlite3")
cursor = conn.cursor()

values = input('Введите имя: ')

cursor.execute("SELECT * FROM myTable2 WHERE Name = '" + values + "'")
result = cursor.fetchall()

for row in result:
    print(row)

conn.close()