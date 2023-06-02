from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.linear_model import LinearRegression
import pandas as pd
from functions import dataset_angles
from functions import video_to_images
from sklearn.model_selection import train_test_split


videos_dir = 'videos-to-process/'
data_dir = 'data/'
videos = ['palm_a.mp4', 'palm_j.mp4', 'fist_a.mp4', 'fist_j.mp4']
video_classes = ['palm', 'palm', 'fist', 'fist']
my_classes = {'palm':0, 'fist':1}


#Creacion datasets
for ind, video in enumerate(videos):
    #crea los frames de los videos y los guarda en el directorio data
    video_to_images(videos_dir+video, data_dir, video_classes[ind], ind)
atributes = ['top angle', 'middle angle', 'bottom angle']
target = 'class'
col = atributes+[target]
dataset = dataset_angles(data_dir, my_classes)
data_frames = []
for i in range(4):
    data_frames.append(pd.DataFrame(columns=col))
for im in dataset:
    for f in range(4):
        entry = im[0][f]
        entry.append(im[1])
        data_frames[f].loc[len(data_frames[f])] = entry




#entrenar modelo para el dedo indice=0
X = data_frames[0][data_frames[0].columns[:-1]]
y = data_frames[0][data_frames[0].columns[-1]]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
# Creación del modelo de regresión lineal
model_indice = LinearRegression()
# Entrenamiento del modelo
model_indice.fit(X_train, y_train)

#entrenar modelo para el dedo medio=1
X = data_frames[1][data_frames[0].columns[:-1]]
y = data_frames[1][data_frames[0].columns[-1]]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
# Creación del modelo de regresión lineal
model_medio = LinearRegression()
# Entrenamiento del modelo
model_medio.fit(X_train, y_train)

#entrenar modelo para el dedo anular=2
X = data_frames[2][data_frames[0].columns[:-1]]
y = data_frames[2][data_frames[0].columns[-1]]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
# Creación del modelo de regresión lineal
model_anular = LinearRegression()
# Entrenamiento del modelo
model_anular.fit(X_train, y_train)

#entrenar modelo para el dedo meñique=3
X = data_frames[3][data_frames[0].columns[:-1]]
y = data_frames[3][data_frames[0].columns[-1]]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
# Creación del modelo de regresión lineal
model_menique = LinearRegression()
# Entrenamiento del modelo
model_menique.fit(X_train, y_train)

