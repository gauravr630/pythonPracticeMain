import numpy as np
import pandas as pd

data123 = [("gauarv", "avi", "shruti", "pallavi"),
           ("80", "40", "60", "50"), ("patna", "arah", "bsp", "Bokaro")
           ]
arr_new = np.array(data123)
print(arr_new)
Df1 = pd.DataFrame(data123)
Df1.columns = ["name", "marks", "city", "age"]
print(Df1)
