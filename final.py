import cv2
import mediapipe as mp
import matplotlib.pyplot as plt
from functions import calculate_the_angles
import matplotlib.pyplot as plt
import time
from collections import deque
from statistics import mean

mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands
from models import model_indice
from models import model_medio
from models import model_anular
from models import model_menique



# Crear una cola con tamaño fijo
pred_0 = deque(maxlen=30)
pred_1 = deque(maxlen=30)
pred_2 = deque(maxlen=30)
pred_3 = deque(maxlen=30)

axis_time = deque(maxlen=30)


# Configurar el gráfico inicial
plt.ion()  # Habilitar el modo interactivo
fig, ax = plt.subplots()
linea_0, = ax.plot([], pred_0)  # Línea inicial vacía
linea_1, = ax.plot([], pred_1)  # Línea inicial vacía
linea_2, = ax.plot([], pred_2)  # Línea inicial vacía
linea_3, = ax.plot([], pred_3)  # Línea inicial vacía

# Configurar el rango de los ejes x e y
ax.set_ylim(-0.25, 1.5)  # Rango del eje y

# Variable para el tiempo inicial
tiempo_inicial = time.time()
tiempo_actualizacion = tiempo_inicial

# For webcam input:
cap = cv2.VideoCapture(0)
with mp_hands.Hands(
    model_complexity=1,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5) as hands:
	while cap.isOpened():
		success, image = cap.read()
		if not success:
			print("Ignoring empty camera frame.")
      		# If loading a video, use 'break' instead of 'continue'.
			continue

		# To improve performance, optionally mark the image as not writeable to
		# pass by reference.
		image.flags.writeable = False
		image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
		results = hands.process(image)

		# Draw the hand annotations on the image.
		image.flags.writeable = True
		image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
		if results.multi_hand_landmarks:
			mp_drawing.draw_landmarks(
				image,
				results.multi_hand_landmarks[0],
				mp_hands.HAND_CONNECTIONS,
				mp_drawing_styles.get_default_hand_landmarks_style(),
				mp_drawing_styles.get_default_hand_connections_style())

			angles = calculate_the_angles(results.multi_hand_landmarks[0])
			#motion predictions of servomotors
			tiempo_actual = time.time()
			axis_time.append(tiempo_actual - tiempo_inicial)

			
			pred_0.append(model_indice.predict((angles[0],)))
			pred_1.append(model_medio.predict((angles[1],)))

			pred_2.append(model_anular.predict((angles[2],)))
			pred_3.append(model_menique.predict((angles[3],)))

			# prediccions.append(model_medio.predict(angles[1]))
			# prediccions.append(model_anular.predict(angles[2]))
			# prediccions.append(model_menique.predict(angles[3]))

		
			#si pasa 0.1 segundos, dibujar
			plt.pause(0.1)
			#if tiempo_actual-tiempo_actualizacion
			# Actualizar la línea del gráfico
			
			pred_0[-1] = pred_0[-1]/1.4


			pred_1[-1] = pred_1[-1]/1.2

			m_0 = mean(list(pred_0))
			for e in len(pred_0):
				pred_0.append(m_0)
			linea_0.set_data(axis_time, pred_0)

			m_1=mean(list(pred_1))
			for e in len(pred_1):
				pred_1.append(m_1)
			linea_1.set_data(axis_time, pred_1)

			m_2=mean(list(pred_2))
			for e in len(pred_2):
				pred_2.append(m_2)
			linea_2.set_data(axis_time, pred_2)

			m_3=mean(list(pred_3))
			for e in len(pred_3):
				pred_3.append(m_3)
			linea_3.set_data(axis_time, pred_3)
			# Ajustar los límites de los ejes x e y según los nuevos datos
			ax.relim()
			ax.autoscale_view()
			# Redibujar el gráfico
			fig.canvas.draw()
			# Agregar una pausa para controlar la velocidad de actualización
			

		# Flip the image horizontally for a selfie-view display.
		cv2.imshow('MediaPipe Hands', cv2.flip(image, 1))
		if cv2.waitKey(5) & 0xFF == 27:
			break
cap.release()











import matplotlib.pyplot as plt

# Crear una lista vacía para almacenar los datos
datos_x = []
datos_y = []

# Configurar el gráfico inicial
plt.ion()  # Habilitar el modo interactivo
fig, ax = plt.subplots()
linea, = ax.plot(datos_x, datos_y)  # Línea inicial vacía

# Configurar el rango de los ejes x e y
ax.set_xlim(0, 10)  # Rango del eje x
ax.set_ylim(0, 100)  # Rango del eje y

# Actualizar el gráfico en tiempo real
while True:
    # Simular la obtención de datos de los parámetros
    # Aquí puedes reemplazar esta parte con tus propios cálculos o adquisición de datos

    # Obtener el nuevo dato de los parámetros
    nuevo_dato_x = obtener_parametro_x()
    nuevo_dato_y = obtener_parametro_y()

    # Agregar el nuevo dato a las listas de datos
    datos_x.append(nuevo_dato_x)
    datos_y.append(nuevo_dato_y)

    # Actualizar la línea del gráfico
    linea.set_data(datos_x, datos_y)

    # Ajustar los límites de los ejes x e y según los nuevos datos
    ax.relim()
    ax.autoscale_view()

    # Redibujar el gráfico
    fig.canvas.draw()

    # Agregar una pausa para controlar la velocidad de actualización
    plt.pause(0.1)  # Pausa de 0.1 segundos (ajusta este valor según tus necesidades)
