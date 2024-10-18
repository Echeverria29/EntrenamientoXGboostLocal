import xgboost as xgb
from cargar_datos import cargar_datos
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

# Cargar los datos
X_train, X_test, y_train, y_test = cargar_datos(r'TU_URL/data/xgboost_ready_data_month.csv')

# Crear y entrenar el modelo
xgb_model = xgb.XGBRegressor(objective='reg:squarederror', random_state=42)
xgb_model.fit(X_train, y_train)

# Predecir en el conjunto de prueba
y_pred = xgb_model.predict(X_test)

# Evaluar el modelo
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print(f"MSE: {mse}")
print(f"R2: {r2}")

# Visualización mejorada
plt.figure(figsize=(8, 6))
plt.scatter(y_test, y_pred, alpha=0.6, edgecolor='k', label='Predicciones')
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], color='red', linestyle='--', label='Valores Ideales')

# Añadir título con el R² en porcentaje
plt.title(f'Predicciones vs Valores Reales\nR²: {r2:.2%}', fontsize=16)
plt.xlabel("Valores Reales", fontsize=14)
plt.ylabel("Predicciones", fontsize=14)
plt.legend()
plt.grid(True)

# Mostrar el gráfico
plt.show()
