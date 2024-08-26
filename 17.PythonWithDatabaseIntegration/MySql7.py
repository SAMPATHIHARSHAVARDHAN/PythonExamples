#7. order by name
import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="DURGA",
  database="KKCC"
)
mycursor = mydb.cursor()
#sql = "SELECT * FROM listofmovies ORDER BY sno " #by default ascending
sql = "SELECT * FROM listofmovies ORDER BY sno desc"  #descending
mycursor.execute(sql)
myresult = mycursor.fetchall()
for x in myresult:
  print(x)