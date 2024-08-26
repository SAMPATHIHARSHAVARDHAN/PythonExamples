#drop table
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="DURGA",
  database="KKCC"
)
try:
  mycursor = mydb.cursor()
  sql = "DROP TABLE listofmovies"
  mycursor.execute(sql)
  print("Table is Deleted")
except:
  print("Table Does't Existed")