import pandas as pd
def test_1_conn(db_conn):
    mycursor = db_conn.cursor()

    mycursor.execute("SELECT * FROM Students")

    myresult = mycursor.fetchall()

    data1 = pd.DataFrame(myresult)
    print("target data below")
    print(data1)
