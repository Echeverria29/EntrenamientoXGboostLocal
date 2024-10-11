# Proyecto de Modelo Predictivo con XGBoost
Descripción del Proyecto
Este proyecto utiliza XGBoost para entrenar un modelo predictivo con el objetivo de anticipar situaciones específicas relacionadas con el comportamiento de un sistema basado en sensores de datos operativos. El modelo predice eventos relevantes basados en múltiples variables operativas que se registran diariamente.

Objetivo del Modelo
El modelo se ha desarrollado para predecir situaciones críticas que puedan ocurrir en un sistema monitoreado, como el comportamiento anómalo de ciertas variables, ayudando a los operadores a tomar decisiones en tiempo real. Por ejemplo, en sistemas de monitoreo de pozos, se puede predecir problemas como el arenamiento, basándose en variables como la velocidad, la presión, y la carga.

Datos Utilizados
El dataset utilizado incluye las siguientes variables:

V_Promedio: Velocidad promedio registrada por los sensores.
V_Max: Velocidad máxima registrada.
V_Min: Velocidad mínima registrada.
P_Promedio: Presión promedio del sistema.
P_Max: Presión máxima alcanzada.
P_Min: Presión mínima registrada.
Los datos han sido replicados y variabilizados para cubrir un período de 30 días, proporcionando suficiente información para entrenar el modelo de manera realista.

Funcionamiento del Modelo
Procesamiento de Datos: Se han eliminado columnas no relevantes y preparado los datos para el entrenamiento. Las variables importantes como velocidad y presión fueron identificadas para construir un modelo robusto.
Entrenamiento: El modelo utiliza el algoritmo XGBoost, que es conocido por su alta eficiencia y rendimiento en tareas de clasificación y regresión.
Predicciones: Una vez entrenado, el modelo es capaz de hacer predicciones diarias basadas en nuevas lecturas de las variables operativas. Esto permite anticipar comportamientos anómalos y ajustar los parámetros del sistema.
Entrenamiento y Evaluación
El modelo se entrena utilizando los datos generados para un mes, con el fin de capturar patrones diarios. Durante el entrenamiento, se ajustaron los hiperparámetros clave para optimizar el rendimiento del modelo.

Métricas de evaluación: El modelo se evalúa utilizando métricas como el error cuadrático medio (MSE) y el coeficiente de determinación (R²) para medir la precisión de las predicciones.
Uso del Modelo
Este modelo puede ser implementado en un entorno de producción donde se realicen monitoreos continuos. Al recibir datos en tiempo real, puede predecir y alertar sobre posibles eventos críticos, permitiendo a los ingenieros tomar decisiones informadas y ajustadas a las predicciones.

