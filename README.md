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

## Requisitos

Para ejecutar este proyecto de manera local, asegúrate de tener instalados los siguientes paquetes:

- pandas
- xgboost
- scikit-learn
- joblib
- matplotlib
- numpy
- boto3 (si deseas trabajar con S3)

Puedes instalar las dependencias necesarias utilizando pip:

```bash
pip install pandas xgboost scikit-learn joblib matplotlib numpy boto3


📦 Proyecto_XGBoost
 ┣ 📂 data
 ┃ ┣ 📜 xgboost_ready_data_month.csv      # Dataset con el que se entrena el modelo
 ┣ 📂 images                             # Carpeta para las imágenes de gráficos generados
 ┃ ┣ 📜 entrenamiento1.png               # Gráfico predicciones vs reales, sin optimización
 ┃ ┣ 📜 entrenamiento2hiperparametros.png # Gráfico predicciones vs reales, optimizado
 ┃ ┣ 📜 modelocargado3.png                # Gráfico predicciones vs reales, modelo cargado
 ┣ 📜 1_cargar_datos.py                   # Script para cargar y dividir los datos
 ┣ 📜 2_entrenar_modelo.py                # Script para entrenar el modelo sin optimización
 ┣ 📜 3_optimizar_modelo.py               # Script para optimizar el modelo con RandomizedSearchCV
 ┣ 📜 4_cargar_modelo.py                  # Script para cargar el modelo guardado y evaluar
 ┣ 📜 README.md                           # Este archivo README
 ┗ 📜 requirements.txt                    # Archivo con las dependencias necesarias
# Instrucciones de Ejecución
# Cargar y Dividir Datos

El primer paso es cargar los datos desde el archivo CSV y dividirlos en conjuntos de entrenamiento y prueba. El código se encuentra en 1_cargar_datos.py.

bash
Copiar código
python 1_cargar_datos.py
Los datos se dividen en un 80% para entrenamiento y un 20% para prueba. Se generará la siguiente salida con la cantidad de muestras en cada conjunto:

yaml
Copiar código
Conjunto de entrenamiento: (69096, 6), Conjunto de prueba: (17275, 6)
# Entrenamiento del Modelo Básico

En el archivo 2_entrenar_modelo.py se entrena un modelo básico de XGBoost sin optimización de hiperparámetros.

bash
Copiar código
python 2_entrenar_modelo.py
Después de entrenar el modelo, se genera un gráfico con las predicciones versus los valores reales.

Gráfico de entrenamiento básico (sin optimización):
# Optimización de Hiperparámetros

El archivo 3_optimizar_modelo.py contiene la implementación de RandomizedSearchCV para encontrar los mejores hiperparámetros del modelo.

bash
Copiar código
python 3_optimizar_modelo.py
Después de la optimización, se muestra el siguiente gráfico con las predicciones optimizadas.

Gráfico de optimización con hiperparámetros:
# Guardar y Cargar el Modelo

El modelo optimizado se guarda en un archivo .pkl para su posterior uso. Luego, puedes cargar este modelo utilizando el archivo 4_cargar_modelo.py.

bash
Copiar código
python 4_cargar_modelo.py
Este script cargará el modelo guardado y evaluará su rendimiento nuevamente. Se generará el siguiente gráfico:

Gráfico de predicciones con el modelo cargado:
# Evaluación y Resultados
# Entrenamiento Inicial
Después de entrenar el modelo sin optimización de hiperparámetros, los resultados iniciales son los siguientes:

bash
Copiar código
MSE: 719.471593554146
R²: 0.8039996548861984
Gráfico:
# Optimización de Hiperparámetros
Utilizando RandomizedSearchCV, los mejores hiperparámetros encontrados fueron:

bash
Copiar código
Mejores hiperparámetros: {'subsample': 0.9, 'reg_lambda': 1.0, 'reg_alpha': 0.0001, 'n_estimators': 500, 'max_depth': 11, 'learning_rate': 0.08944444444444445, 'gamma': 0.5, 'colsample_bytree': 1.0}
Los resultados después de la optimización son:

bash
Copiar código
MSE optimizado: 217.73657880850624
R² optimizado: 0.9406836281338827
Gráfico:
# Modelo Cargado
Finalmente, al cargar el modelo optimizado y evaluarlo nuevamente, obtenemos los mismos resultados:

bash
Copiar código
MSE cargado: 217.73657880850624
R² cargado: 0.9406836281338827
Gráfico:
# Imágenes