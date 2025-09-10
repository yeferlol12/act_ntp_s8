import pandas as pd
lista_diccionarios = [{"Empleado": "Ana", "Salario": 2500000, "Departamento": "Madrid"},
         {"Empleado": "Juan", "Salario": 3000000, "Departamento": "Barcelona"},
         {"Empleado": "Pedro", "Salario": 3500000, "Departamento": "Sevilla"}]

df = pd.DataFrame(lista_diccionarios)

print(df)
print(df['Empleado'])