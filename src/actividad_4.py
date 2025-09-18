import pandas as pd
diccionario = [{"Producto": "Laptop", "Precio": 1200000, "Categoria": "electronica"},
         {"Producto": "Cuaderno", "Precio": 2000, "Categoria": "papeleria"},
         {"Prodcuto": "zapatero", "Precio": 15000, "Categoria": "hogar"}]

df = pd.DataFrame(diccionario)

print(df)
print(df['Precio'])
print(df.info())