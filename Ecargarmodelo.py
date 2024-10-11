import joblib
from utils import evaluar_modelo
from Acargar_datos import cargar_datos

# Cargar los datos
X_train, X_test, y_train, y_test = cargar_datos(r'C:/Users/josue/Desktop/Pro-EntrenamientoModeloXGboost-despliegue/xgboost_ready_data_one_month.csv')

# Cargar el modelo guardado
best_model = joblib.load('best_xgboost_model.pkl')

# Hacer predicciones con el modelo optimizado
y_pred_optimized = best_model.predict(X_test)

# Evaluar el modelo
mse, r2 = evaluar_modelo(y_test, y_pred_optimized)
print(f"MSE optimizado: {mse}, R2 optimizado: {r2}")
