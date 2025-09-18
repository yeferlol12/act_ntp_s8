import csv

# Define los nombres de las columnas
column_names = ["Curso", "Instrutor", "Duracion"]

# Crea una lista de datos para cada fila
data = [
    ["Tecnico en electricidad industrial", "Politecnico Cafor", "18 meses"],
    ["Tecnico en mecatronica", "U. Potificia Bolivariana", "24 meses"],
    ["Tecnico en administracion", "Cesde", "18 meses"]
]

# Abre el archivo CSV en modo escritura
with open("info.csv", "w", newline="") as file:
    writer = csv.writer(file)

    # Escribe la fila de encabezados
    writer.writerow(column_names)

    # Escribe cada fila de datos
    for row in data:
        writer.writerow(row)

print("Archivo CSV creado correctamente.")