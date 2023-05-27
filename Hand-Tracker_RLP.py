#Import the necessary Packages for this software to run
import mediapipe
import cv2
import numpy as np

#Use MediaPipe to draw the hand framework over the top of hands it identifies in Real-Time
drawingModule = mediapipe.solutions.drawing_utils
handsModule = mediapipe.solutions.hands
import logging
#fmt = '[%(levelname)s %(asctime)s ---- %(message)s]'
txt = '[%(message)s]'
logging.basicConfig(level=logging.DEBUG, format=txt)

#window size
h=480
w=640

#upper and lower lanmarks
thumb = (4, 2)
index = (8, 5)
middle = (12, 9)
ring = (16, 13)
pinky = (20, 17)



# def length_of_the_phalanges(results):
#     thumb_upper_coord =     (results.landmark[thumb[0]].x, results.landmark[thumb[0]].y, results.landmark[thumb[0]].z)
#     thumb_lower_coord =     (results.landmark[thumb[1]].x, results.landmark[thumb[1]].y, results.landmark[thumb[1]].z)
#     index_upper_coord =     (results.landmark[thumb[0]].x, results.landmark[thumb[0]].y, results.landmark[thumb[0]].z)
#     index_lower_coord =     (results.landmark[thumb[1]].x, results.landmark[thumb[1]].y, results.landmark[thumb[1]].z)
#     middle_upper_coord =    (results.landmark[thumb[0]].x, results.landmark[thumb[0]].y, results.landmark[thumb[0]].z)
#     middle_lower_coord =    (results.landmark[thumb[1]].x, results.landmark[thumb[1]].y, results.landmark[thumb[1]].z)
#     ring_upper_coord =      (results.landmark[thumb[0]].x, results.landmark[thumb[0]].y, results.landmark[thumb[0]].z)
#     ring_lower_coord =      (results.landmark[thumb[1]].x, results.landmark[thumb[1]].y, results.landmark[thumb[1]].z)
#     pinky_upper_coord =     (results.landmark[thumb[0]].x, results.landmark[thumb[0]].y, results.landmark[thumb[0]].z)
#     pinky_lower_coord =     (results.landmark[thumb[1]].x, results.landmark[thumb[1]].y, results.landmark[thumb[1]].z)
#     return dict()



# For static images:
file = 'mano_abierta_izquierda.jpg'
# Read an image, flip it around y-axis for correct handedness output (see
# above).
image = cv2.flip(cv2.imread(file), 1)
# Convert the BGR image to RGB before processing.
with handsModule.Hands(static_image_mode=False, min_detection_confidence=0.7, min_tracking_confidence=0.7, max_num_hands=2) as hands:
    results = hands.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    if results.multi_hand_landmarks != None:
        #results pertaining to a single hand
        hand_landmarks = results.multi_hand_landmarks[0]
                #calcular las medidas de las falanges
                #calibrar hasta estabilizar
                #probar si tiene sentido
                #distances[i] =






#For real time:

# #Use CV2 Functionality to create a Video stream and add some values
# cap = cv2.VideoCapture(0)
# fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')

# with handsModule.Hands(static_image_mode=False, min_detection_confidence=0.7, min_tracking_confidence=0.7, max_num_hands=2) as hands:
#      while True:
#         ret, frame = cap.read()
#         frame1 = cv2.resize(frame, (w, h))
#         results = hands.process(cv2.cvtColor(frame1, cv2.COLOR_BGR2RGB))
#         if results.multi_hand_landmarks != None:
#             for handLandmarks in results.multi_hand_landmarks:
#                 drawingModule.draw_landmarks(frame1, handLandmarks, handsModule.HAND_CONNECTIONS)
#                 #[id, x, y]
#                 a=[]
#                 b=[]
#                 for id, pt in enumerate (handLandmarks.landmark):
#                     x = int(pt.x * w)
#                     y = int(pt.y * h)
#                     a.append([id,x,y])
#                     b.append(str(pt).replace ("< ","").replace("HandLandmark.", "").replace("_"," ").replace("[]",""))

#         cv2.imshow("Frame", frame1);
#         key = cv2.waitKey(1) & 0xFF
#         if key == ord("q"):
#             break