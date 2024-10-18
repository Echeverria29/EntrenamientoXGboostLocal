# utils.py
from sklearn.metrics import mean_squared_error, r2_score

def evaluar_modelo(y_test, y_pred):
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    print(f"Error cuadrático medio (MSE): {mse}")
    print(f"Coeficiente de determinación (R2 Score): {r2}")
    return mse, r2
