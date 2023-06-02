import time
from adafruit_servokit import ServoKit

# Inicializar el controlador PCA9685
kit = ServoKit(channels=8)

# Configurar el ángulo de los servomotores
servo1 = 1  # Canal del primer servomotor

try:
    while True:
        # Girar el servomotor a 0 grados
        kit.servo[servo1].angle = 2.5
        time.sleep(1)

        # Girar el servomotor a 90 grados
        kit.servo[servo1].angle = 70
        time.sleep(1)

        # Girar el servomotor a 180 grados
        kit.servo[servo1].angle = 12
        time.sleep(1)

except KeyboardInterrupt:
    # Detener el controlador PCA9685
    kit.servo[servo1].angle = None
