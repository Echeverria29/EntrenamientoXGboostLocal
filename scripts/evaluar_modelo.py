# 5_cargar_modelo.py
import joblib
from cargar_datos import cargar_datos
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

# Cargar los datos de prueba
X_train, X_test, y_train, y_test = cargar_datos(
    r'TU_URLdata/xgboost_ready_data_month.csv'
)

# Cargar el modelo guardado
best_model = joblib.load(r'TU_URL/models/best_xgboost_model.pkl')

# Hacer predicciones con el modelo cargado
y_pred_cargado = best_model.predict(X_test)

# Evaluar el modelo
mse_cargado = mean_squared_error(y_test, y_pred_cargado)
r2_cargado = r2_score(y_test, y_pred_cargado)

# Imprimir resultados de MSE y R²
print(f"MSE cargado: {mse_cargado}")
print(f"R2 cargado: {r2_cargado}")

# Visualización mejorada del modelo cargado
plt.figure(figsize=(8, 6))
plt.scatter(y_test, y_pred_cargado, alpha=0.6, edgecolor='k', label='Predicciones')
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], color='red', linestyle='--', label='Valores Ideales')

# Añadir título con el R² en porcentaje
plt.title(f'Modelo Cargado: Predicciones vs Valores Reales\nR²: {r2_cargado:.2%}', fontsize=16)
plt.xlabel("Valores Reales", fontsize=14)
plt.ylabel("Predicciones Cargadas", fontsize=14)
plt.legend()
plt.grid(True)

# Mostrar el gráfico
plt.show()
