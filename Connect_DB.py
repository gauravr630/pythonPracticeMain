import mysql.connector
import pytest
import pandas as pd
# establishing the connection
mydb = mysql.connector.connect(
    host="127.0.0.1",
    port="3306",
    user="root",
    passwd="Garvsql1@",
    database="gauravdb"
)
print(mydb)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM Students")

myresult = mycursor.fetchall()



for x in myresult:
  print(x)

data= pd.DataFrame(myresult)
print(data)

print(len(data))

def val_cnt():
    assert len(data)==5, " row count is wrong"

val_cnt()


