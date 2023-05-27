import numpy as np
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import pandas as pd
import mediapipe
from functions import *
drawingModule = mediapipe.solutions.drawing_utils
handsModule = mediapipe.solutions.hands



videos_dir = 'videos-to-process/'
data_dir = 'data/'

videos = ['palm_a.mp4', 'palm_j.mp4', 'fist_a.mp4', 'fist_j.mp4']
video_classes = ['palm', 'palm', 'fist', 'fist']

my_classes = ['palm', 'fist']



# for ind, video in enumerate(videos):
#     #crea los frames de los videos y los guarda en el directorio data
#     video_to_images(videos_dir+video, data_dir, video_classes[ind], ind)



col = ['top angle', 'middle angle', 'bottom angle', 'class']
dataset = dataset_angles(data_dir, my_classes)

# ahora tengo todos los datos en una lista de tuplas, cada tupla es de 2 elementos, los angulos de todos los dedos de una imagen y su clase
# el 1º elemento de la tupla es un diccionario que tiene como clave el indice del dedo (si es el indice=0, anular=2, etc) y como valor otro diccionario
# este otro diccionario tiene como clave el indice del angulo (superior=0, medio=1, inferior=2) y como valor el angulo en grados

#ahora valos a crear 4 datasets para los 4 modelos (uno por cada dedo)
data_frames = []
for i in range(4):
    data_frames.append(pd.DataFrame(columns=col))

#para los 4 dedos:
for im in dataset:
    for f in range(4):
        entry = list(im[0][f].values())
        entry.append(im[1])
        data_frames[f].loc[len(data_frames[f])] = entry



# procesar datos (retorna conjunto X  e y de todo el dataset)
# creo dataframe
# para cada imagen añado la entrada del calculo de los angulos y la etiqueta al dataframe

# -. uno datafram
# x. tengo dataframe del conjunto X e Y





# x1    x2      x3      y
# 115   90     30     0.3



# # División de los datos en conjuntos de entrenamiento y prueba
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# # Creación del modelo de regresión lineal
# model = LinearRegression()

# # Entrenamiento del modelo
# model.fit(X_train, y_train)

# # Predicción en el conjunto de prueba
# y_pred = model.predict(X_test)

# # Evaluación del modelo
# mse = mean_squared_error(y_test, y_pred)
# r2 = r2_score(y_test, y_pred)

# print("Error cuadrático medio (MSE):", mse)
# print("Coeficiente de determinación (R^2):", r2)

# # Validación cruzada
# cv_scores = cross_val_score(model, X, y, cv=5)  # 5-fold cross-validation

# print("Puntuaciones de validación cruzada:", cv_scores)
# print("Puntuación media de validación cruzada:", np.mean(cv_scores))
