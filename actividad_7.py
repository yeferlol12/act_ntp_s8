import pandas as pd
from pathlib import Path

ruta=Path("info.csv")
if ruta.exists():
    df = pd.read_csv("info.csv")
    print(df)
else:
    print("El archivo no existe.")


