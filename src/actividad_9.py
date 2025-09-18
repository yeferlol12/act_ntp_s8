import pandas as pd

import numpy as np

datos = np.array([[2500000, 3550000, 4300000],
                   [1200000, 3010000, 5600000],
                   [1800000, 3570000, 4600000]])

df = pd.DataFrame(datos, columns=['Q1', 'Q2', 'Q3'])

print(df)
print(df.shape,df.info())