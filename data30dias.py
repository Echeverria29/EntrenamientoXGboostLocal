import numpy as np

# Asumimos que los datos actuales representan un solo día.
# Vamos a replicar la data para generar 30 días de datos con variaciones

# Número de días a replicar
dias = 30
num_registros_dia = len(data)

# Crear una lista para almacenar los nuevos datos
new_data = []

# Iterar por cada día
for dia in range(dias):
    # Añadir una pequeña variación aleatoria a los datos de cada día
    variacion = np.random.normal(0, 0.1, size=data.shape)
    day_data = data + variacion
    day_data.iloc[:, 0] = dia  # Marcar el día en la primera columna
    new_data.append(day_data)

# Concatenar los datos generados para cada día
new_data = pd.concat(new_data, ignore_index=True)

# Mostrar las primeras filas de los nuevos datos generados
import ace_tools as tools; tools.display_dataframe_to_user(name="Datos generados para un mes", dataframe=new_data)

# Guardar el nuevo dataset en un archivo CSV
new_data_path = '/mnt/data/xgboost_ready_data_month.csv'
new_data.to_csv(new_data_path, index=False)

new_data_path
