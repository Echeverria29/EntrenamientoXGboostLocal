import pandas as pd


# Cargar el CSV desde una ruta local o S3 si lo descargas antes
df_grouped = pd.read_csv(r'C:/Users/josue/Desktop/EntrenamientoXGboostLocal/xgboost_ready_data_month.csv',header=None)
# Cambia esto por la ruta a tu archivo CSV

# Ver las primeras filas para verificar el orden de las columnas
print(df_grouped)

