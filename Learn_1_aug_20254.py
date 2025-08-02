import pandas as pd
data = pd.read_csv("C:/Users/gaura/Downloads/Book1.csv")
print(data)
df = pd.DataFrame(data)
print(df)
print(df.shape)
print(len(df['B']))
