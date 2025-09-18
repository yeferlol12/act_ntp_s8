import pandas as pd
datos = [["El principito", "Antoine de Saint-Exupéry ", 1943],
         ["El caballero de la armadura oxidada", "Robert Fisher", 1989],
         ["100 años de soleda", "Gabriel García Márquez", 1967]]

df = pd.DataFrame(datos, columns=["Titulo", "Autor", "Año"])

print(df)
print(df.shape)