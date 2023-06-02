import time
from adafruit_pca9685 import PCA9685
import board
import busio
# Initialize the PCA9685 controller
i2c = busio.I2C(board.SCL, board.SDA)
pca = PCA9685(i2c)

pca.frequency = 50  # Set the PWM frequency (adjust if necessary)
servo_channel=pca.channe
