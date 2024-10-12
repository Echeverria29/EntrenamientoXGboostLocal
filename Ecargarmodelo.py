# 5_cargar_modelo.py
import joblib
from Acargar_datos import cargar_datos
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

# Cargar los datos de prueba
X_train, X_test, y_train, y_test = cargar_datos(r'C:/Users/josue/Desktop/EntrenamientoXGboostLocal/xgboost_ready_data_month.csv')

# Cargar el modelo guardado
best_model = joblib.load('best_xgboost_model.pkl')

# Hacer predicciones con el modelo cargado
y_pred_cargado = best_model.predict(X_test)

# Evaluar el modelo
mse_cargado = mean_squared_error(y_test, y_pred_cargado)
r2_cargado = r2_score(y_test, y_pred_cargado)
print(f"MSE cargado: {mse_cargado}")
print(f"R2 cargado: {r2_cargado}")

# Visualización del modelo cargado
plt.scatter(y_test, y_pred_cargado, alpha=0.5)
plt.plot([min(y_test), max(y_test)], [min(y_test), max(y_test)], color='green')
plt.xlabel("Valores Reales")
plt.ylabel("Predicciones Cargadas")
plt.title("Modelo Cargado: Predicciones vs Valores Reales")
plt.show()
