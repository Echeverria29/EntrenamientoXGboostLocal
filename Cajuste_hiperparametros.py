import xgboost as xgb
from Acargar_datos import cargar_datos
from sklearn.model_selection import RandomizedSearchCV
import numpy as np
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt
# Cargar los datos
X_train, X_test, y_train, y_test = cargar_datos(r'C:/Users/josue/Desktop/EntrenamientoXGboostLocal/xgboost_ready_data_month.csv')

# Crear el modelo base
xgb_model = xgb.XGBRegressor(objective='reg:squarederror', random_state=42)
# Definir una cuadrícula de hiperparámetros
param_grid = {
    'max_depth': np.arange(3, 12, 2),  
    'n_estimators': np.arange(100, 1000, 100),  
    'learning_rate': np.linspace(0.001, 0.2, 10),  
    'subsample': np.linspace(0.6, 1.0, 5),  
    'colsample_bytree': np.linspace(0.6, 1.0, 5),  
    'gamma': np.linspace(0, 0.5, 5),  
    'reg_alpha': np.logspace(-4, 0, 5),  
    'reg_lambda': np.logspace(-4, 0, 5)  
}

# Configurar RandomizedSearchCV
random_search = RandomizedSearchCV(estimator=xgb_model, param_distributions=param_grid, n_iter=50, scoring='neg_mean_squared_error', cv=5, verbose=1, random_state=42, n_jobs=-1)

# Ejecutar búsqueda
random_search.fit(X_train, y_train)

# Mostrar los mejores hiperparámetros
print(f"Mejores hiperparámetros: {random_search.best_params_}")

# Usar el mejor modelo
best_model = random_search.best_estimator_
y_pred_optimized = best_model.predict(X_test)

# Evaluar el modelo optimizado
mse_optimized = mean_squared_error(y_test, y_pred_optimized)
r2_optimized = r2_score(y_test, y_pred_optimized)
print(f"MSE optimizado: {mse_optimized}")
print(f"R2 optimizado: {r2_optimized}")

# Visualización del modelo optimizado
plt.scatter(y_test, y_pred_optimized, alpha=0.5)
plt.plot([min(y_test), max(y_test)], [min(y_test), max(y_test)], color='blue')
plt.xlabel("Valores Reales")
plt.ylabel("Predicciones Optimizadas")
plt.title("Optimización: Predicciones vs Valores Reales")
plt.show()