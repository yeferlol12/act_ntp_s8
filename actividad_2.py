import pandas as pd
series=pd.Series([85, 92, 78],
index=['Matemáticas', 'Ciencias', 'Historia'])
print("Notas de ciencia:", series['Ciencias'])
print(series.info())
print("suma de notas: ", series.sum())
print("promedio de notas:" , series.mean())