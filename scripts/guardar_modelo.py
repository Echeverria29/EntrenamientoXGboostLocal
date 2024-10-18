import joblib
from optimizar_modelo import best_model

# Guardar el modelo optimizado
joblib.dump(best_model, 'best_xgboost_model.pkl')

print("Modelo optimizado guardado como 'best_xgboost_model.pkl'")
