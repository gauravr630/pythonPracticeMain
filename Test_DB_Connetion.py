import mysql.connector
import pytest
import pandas as pd
# establishing the connection
import pytest

mydb = mysql.connector.connect(
    host="127.0.0.1",
    port="3306",
    user="root",
    passwd="Garvsql1@",
    database="gauravdb"
)
print("my db is below")
print(mydb)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM Students")

myresult = mycursor.fetchall()

for x in myresult:
    print(x)

df2 = pd.DataFrame(myresult)
df2.columns = ['StudentID', 'Name', 'Age', 'Grade']
print("target data below")
print(df2)
tgt_cnt = len(df2)
print("count of rows is :", len(df2))
print("duplicate is")
print("sum of duplicate is ", df2.duplicated().sum())

data = pd.read_csv("C:/Users/gaura/Downloads/Book1.csv")
df1 = pd.DataFrame(data)
print("Source data below")
src_cnt = len(df1)
print(df1)
print("duplicate is")
print("sum of duplicate is ", df1.duplicated().sum())

diff = df1[df1.isin(df2)]
print(diff)


def test_val_cnt():
    print("compare source and target count")
    assert len(df1) == len(df2), " row count is wrong"


def test_dup_cnt_src():
    print("duplicate src count")
    cnt = df1.duplicated().sum()
    assert cnt == 0, "source has duplicates"


def test_dup_cnt_tgt():
    print("duplicate tgt count")
    cnt1 = df2.duplicated().sum()
    assert cnt1 == 0, "tgt has duplicates"
