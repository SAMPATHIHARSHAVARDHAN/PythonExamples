# read n records
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="DURGA",
  database="KKCC"
)
mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM listofmovies order by sno desc LIMIT 1")
myresult = mycursor.fetchall()
for x in myresult:
  print(x)