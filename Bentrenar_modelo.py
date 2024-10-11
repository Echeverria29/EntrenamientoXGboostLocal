# 2_entrenar_modelo.py
import xgboost as xgb
from utils import evaluar_modelo
from Acargar_datos import cargar_datos

# Cargar los datos
X_train, X_test, y_train, y_test = cargar_datos(r'C:/Users/josue/Desktop/Pro-EntrenamientoModeloXGboost-despliegue/xgboost_ready_data.csv')

# Crear y entrenar el modelo
xgb_model = xgb.XGBRegressor(objective='reg:squarederror', random_state=42)
xgb_model.fit(X_train, y_train)

# Predecir en el conjunto de prueba
y_pred = xgb_model.predict(X_test)

# Evaluar el modelo
mse, r2 = evaluar_modelo(y_test, y_pred)
