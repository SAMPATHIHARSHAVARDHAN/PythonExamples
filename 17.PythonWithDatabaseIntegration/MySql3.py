#3. create table
import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="DURGA",
  database="KKCC"
)
"""
create table tablename(
columnname1 datatype(size),
columnname2 datatype(size),
)
"""
mycursor = mydb.cursor()
try:
  mycursor.execute("CREATE TABLE listofmovies "
                   "(sno int(5),movie_name varchar(30),"
                   "hero_name VARCHAR(128),"
                   "actress_name VARCHAR(128),"
                   "director_name varchar(128),"
                   "realease_year date)")
  print("Table Successfully Created")
except:
  print("Table already Created")