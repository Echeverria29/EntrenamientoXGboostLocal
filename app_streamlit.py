import streamlit as st
import numpy as np
import joblib
import pandas as pd

# Título de la aplicación
st.title("Predicción de Condiciones Operativas de la Máquina")

# Ingresar datos operativos
direccion_num = st.selectbox('Dirección (0 = Bajada, 1 = Subida)', [0, 1])
v_promedio = st.slider('Velocidad Promedio (m/s)', 0.0, 10.0, 5.0)
v_max = st.slider('Velocidad Máxima (m/s)', 0.0, 20.0, 10.0)
v_min = st.slider('Velocidad Mínima (m/s)', 0.0, 10.0, 1.0)
p_promedio = st.slider('Presión Promedio (PSI)', 500.0, 2000.0, 1200.0)
p_min = st.slider('Presión Mínima (PSI)', 500.0, 1000.0, 800.0)

# Cargar el modelo guardado
model = joblib.load('best_xgboost_model.pkl')

# Crear el array de entrada con los valores proporcionados por el usuario
input_data = np.array([[direccion_num, v_promedio, v_max, v_min, p_promedio, p_min]])

# Hacer predicciones
if st.button("Realizar Predicción"):
    # Predecir la presión máxima
    prediction_p_max = model.predict(input_data)
    
    # Simular otras predicciones basadas en el comportamiento de la máquina (velocidad, presión)
    prediccion_v_promedio = v_promedio * 1.05  # Simulación: ajustar según lógica o métricas reales
    prediccion_v_max = v_max * 0.98  # Simulación
    prediccion_v_min = v_min * 1.02  # Simulación
    
    # Mostrar todas las predicciones
    st.write(f"**Presión máxima predicha**: {prediction_p_max[0]:.2f} PSI")
    st.write(f"**Velocidad promedio ajustada**: {prediccion_v_promedio:.2f} m/s")
    st.write(f"**Velocidad máxima ajustada**: {prediccion_v_max:.2f} m/s")
    st.write(f"**Velocidad mínima ajustada**: {prediccion_v_min:.2f} m/s")

# Incluir un espacio adicional con markdown para personalizar el estilo
st.markdown("""
<style>
    .main {
        background-color: #f5f5f5;
        padding: 20px;
        border-radius: 10px;
    }
    h1 {
        color: #3e4a89;
        text-align: center;
    }
    .css-1aumxhk {
        color: #FF6347;
    }
    .stButton > button {
        background-color: #3e4a89;
        color: white;
        border-radius: 10px;
        padding: 10px;
        border: none;
    }
    .stButton > button:hover {
        background-color: #FF6347;
        color: white;
    }
</style>
""", unsafe_allow_html=True)
