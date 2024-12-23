import pandas as pd
from sklearn.model_selection import train_test_split

def cargar_datos(ruta_csv):
    # Cargar el dataset
    df_grouped = pd.read_csv(ruta_csv, header=None)

    # Asignar nombres de columnas
    df_grouped.columns = ['Direccion_Num', 'V_Promedio', 'V_Max', 'V_Min', 'P_Promedio', 'P_Max', 'P_Min']

    # Dividir las características (X) y la columna objetivo (y)
    X = df_grouped[['Direccion_Num', 'V_Promedio', 'V_Max', 'V_Min', 'P_Promedio', 'P_Min']]
    y = df_grouped['P_Max']
    
    # Dividir en conjuntos de entrenamiento y prueba
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    print(f"Conjunto de entrenamiento: {X_train.shape}, Conjunto de prueba: {X_test.shape}")
    return X_train, X_test, y_train, y_test

