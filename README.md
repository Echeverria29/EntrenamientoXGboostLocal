# Proyecto de Entrenamiento de Modelo XGBoost con Optimización de Hiperparámetros

Este proyecto tiene como objetivo entrenar un modelo de XGBoost utilizando datos de sensores (velocidad, presión, etc.), optimizar los hiperparámetros mediante RandomizedSearchCV y evaluar su rendimiento tanto antes como después de la optimización. Además, se guardará y cargará el modelo para su reutilización en futuras predicciones.

## Contenido
- [Requisitos](#requisitos)
- [Estructura del Proyecto](#estructura-del-proyecto)
- [Instrucciones de Ejecución](#instrucciones-de-ejecución)
- [Evaluación y Resultados](#evaluación-y-resultados)
  - [Entrenamiento Inicial](#entrenamiento-inicial)
  - [Optimización de Hiperparámetros](#optimización-de-hiperparámetros)
  - [Modelo Cargado](#modelo-cargado)
- [Imágenes](#imágenes)

---

## Requisitos

Para ejecutar este proyecto de manera local, asegúrate de tener instalados los siguientes paquetes:

- pandas  
- xgboost  
- scikit-learn  
- joblib  
- matplotlib  
- numpy  
- boto3 (si deseas trabajar con S3)

Instala las dependencias necesarias con:

$ pip install -r requirements.txt

## Estructura del Proyecto

El proyecto está organizado de la siguiente manera:
- **data/**  
  Archivos relacionados con datasets:  
  - `xgboost_ready_data.csv`  
  - `xgboost_ready_data_month.csv`  

- **models/**  
  Modelos entrenados y guardados:  
  - `best_xgboost_model.pkl`  
  - **model_files/** *(opcional)*: Si generas más archivos del modelo

- **images/**  
  Imágenes generadas del entrenamiento y evaluación:  
  - `entrenamiento_1.png`  
  - `entrenamiento_hiperparametros_2.png`  
  - `modelo_cargado_3.png`  

- **scripts/**  
  Scripts Python del proyecto:  
  - `cargar_datos.py` - Cargar y dividir los datos  
  - `entrenar_modelo.py` - Entrenamiento sin optimización  
  - `optimizar_modelo.py` - Optimización con RandomizedSearchCV  
  - `cargar_modelo.py` - Cargar y evaluar un modelo guardado  
  - `utils.py` - Funciones de utilidad (si aplica)  

- **streamlit_app/**  
  Aplicación Streamlit:  
  - `app_streamlit.py` - Código principal de la app  
  - `requirements.txt` - Dependencias del entorno para la app  

- **Archivos adicionales:**  
  - `README.md` - Descripción del proyecto y guía de uso  
  - `.gitignore` - Archivos a ignorar en el control de versiones  
  - `requirements.txt` - Dependencias generales del proyecto


# Instrucciones de Ejecución
# Cargar y Dividir Datos

El primer paso es cargar los datos desde el archivo CSV y dividirlos en conjuntos de entrenamiento y prueba. El código se encuentra python scripts/cargar_datos.py

Los datos se dividen en un 80% para entrenamiento y un 20% para prueba. Se generará la siguiente salida con la cantidad de muestras en cada conjunto:

Conjunto de entrenamiento: (69096, 6), Conjunto de prueba: (17275, 6)

# Entrenamiento del Modelo Básico

En el archivo python scripts/entrenar_modelo.py se entrena un modelo básico de XGBoost sin optimización de hiperparámetros.

Después de entrenar el modelo, se genera un gráfico con las predicciones versus los valores reales.

Gráfico de entrenamiento básico (sin optimización):
![](https://github.com/Echeverria29/EntrenamientoXGboostLocal/blob/main/images/entrenamiento1.PNG)

# Optimización de Hiperparámetros

El archivo python scripts/optimizar_modelo.py contiene la implementación de RandomizedSearchCV para encontrar los mejores hiperparámetros del modelo.

Después de la optimización, se muestra el siguiente gráfico con las predicciones optimizadas.

Gráfico de optimización con hiperparámetros:
![](https://github.com/Echeverria29/EntrenamientoXGboostLocal/blob/main/images/entrenamiento2hiperparametros.png)



# Guardar y Cargar el Modelo

El modelo optimizado se guarda en un archivo .pkl para su posterior uso. Luego, puedes cargar este modelo utilizando el archivo python scripts/guardar_modelo.py.

python cargar_modelo.py
Este script cargará el modelo guardado y evaluará su rendimiento nuevamente. Se generará el siguiente gráfico:

Gráfico de predicciones con el modelo cargado:
![](https://github.com/Echeverria29/EntrenamientoXGboostLocal/blob/main/images/modelocargado3.png)

# Evaluación y Resultados
# Entrenamiento Inicial
Después de entrenar el modelo sin optimización de hiperparámetros, los resultados iniciales son los siguientes:


MSE: 719.471593554146
R²: 0.8039996548861984
Gráfico:
# Optimización de Hiperparámetros
Utilizando RandomizedSearchCV, los mejores hiperparámetros encontrados fueron:


Mejores hiperparámetros: {'subsample': 0.9, 'reg_lambda': 1.0, 'reg_alpha': 0.0001, 'n_estimators': 500, 'max_depth': 11, 'learning_rate': 0.08944444444444445, 'gamma': 0.5, 'colsample_bytree': 1.0}
Los resultados después de la optimización son:


MSE optimizado: 217.73657880850624
R² optimizado: 0.9406836281338827
Gráfico:


# Modelo Cargado
Finalmente, al cargar el modelo optimizado y evaluarlo nuevamente, obtenemos los mismos resultados:

MSE cargado: 217.73657880850624
R² cargado: 0.9406836281338827
