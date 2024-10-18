import joblib
import os
from optimizar_modelo import best_model

# Definir la ruta donde se guardará el modelo
output_dir = 'models'
os.makedirs(output_dir, exist_ok=True)  # Crear la carpeta si no existe

# Guardar el modelo optimizado en la carpeta 'models'
model_path = os.path.join(output_dir, 'best_xgboost_model.pkl')
joblib.dump(best_model, model_path)

print(f"Modelo optimizado guardado como '{model_path}'")
