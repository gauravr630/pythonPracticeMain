import pandas as pd
import numpy as np

data = pd.read_csv("C:/Users/gaura/Downloads/Book1.csv")
df = pd.DataFrame(data)
print(data)

data1 = np.array(data)
print(data1)
data1[0,2]= 501
print(data1[0,2])
df1=pd.DataFrame(data1)
df1.to_csv("C:/Users/gaura/Downloads/Book2.csv")
df.to_excel('test.xlsx', sheet_name='sheet1', index=False)

data1=pd.read_csv("C:/Users/gaura/Downloads/batsman_runs_series.csv")
df = pd.DataFrame(data1)
print(data1)