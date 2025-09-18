import pandas as pd
import requests

def obtener_usuario():
    url="https://playground.mockoon.com/users"
         
    try:
        response = requests.get(url,timeout=10)
        # Verificar que la petición fue exitosa
        if response.status_code == 200:
            # Convertir la respuesta JSON a DataFrame
            data = response.json()
            df = pd.DataFrame(data)

            print(df.head())
            print(df)
            return df
        else:
                print(f"Error en la petición: {response.status_code}") 
                return None
    except requests.RequestException as e:
         print(f"Error de conexion:{e}")
         return None
usuarios=obtener_usuario()