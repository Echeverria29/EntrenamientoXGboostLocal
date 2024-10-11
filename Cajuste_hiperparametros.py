from sklearn.model_selection import GridSearchCV
import xgboost as xgb
from utils import evaluar_modelo
from Acargar_datos import cargar_datos
from sklearn.model_selection import RandomizedSearchCV
import numpy as np
# Cargar los datos
X_train, X_test, y_train, y_test = cargar_datos(r'C:/Users/josue/Desktop/EntrenamientoXGboostLocal/xgboost_ready_data_month.csv')

# Crear el modelo base
xgb_model = xgb.XGBRegressor(objective='reg:squarederror', random_state=42)
# Definir una cuadrícula más amplia de hiperparámetros
param_grid = {
    'max_depth': np.arange(3, 12, 2),  # Profundidad de 3 a 11
    'n_estimators': np.arange(100, 1000, 100),  # Número de estimadores de 100 a 1000
    'learning_rate': np.linspace(0.001, 0.2, 10),  # Tasas de aprendizaje desde 0.001 a 0.2
    'subsample': np.linspace(0.6, 1.0, 5),  # Subsample entre 0.6 y 1.0
    'colsample_bytree': np.linspace(0.6, 1.0, 5),  # Colsample bytree entre 0.6 y 1.0
    'gamma': np.linspace(0, 0.5, 5),  # Gamma entre 0 y 0.5
    'reg_alpha': np.logspace(-4, 0, 5),  # Regularización L1
    'reg_lambda': np.logspace(-4, 0, 5)  # Regularización L2
}

# Configurar RandomizedSearchCV
random_search = RandomizedSearchCV(estimator=xgb_model, param_distributions=param_grid,
                                   n_iter=50, scoring='neg_mean_squared_error', cv=5, verbose=1, random_state=42, n_jobs=-1)


# Ejecutar la búsqueda de hiperparámetros
random_search.fit(X_train, y_train)

# Mostrar los mejores hiperparámetros
print(f"Mejores hiperparámetros: {random_search.best_params_}")

# Hacer predicciones con el mejor modelo
best_model = random_search.best_estimator_
y_pred_optimized = best_model.predict(X_test)

# Evaluar el modelo optimizado
mse, r2 = evaluar_modelo(y_test, y_pred_optimized)
print(f"MSE optimizado: {mse}, R2 optimizado: {r2}")
