import time
from adafruit_pca9685 import PCA9685
import board
import busio
# Initialize the PCA9685 controller
i2c = busio.I2C(board.SCL, board.SDA)
pca = PCA9685(i2c,address=0x40)

pca.frequency = 25  # Set the PWM frequency (adjust if necessary)
servo_channel=pca.channels[0]

import adafruit_motor.servo
servo = adafruit_motor.servo.Servo(servo_channel)

servo.angle=140
time.sleep(1)
servo.angle=0
time.sleep(1)
pca.deinit()

def set_servo_angle(channel, angle):
    duty_cycle = int((angle / 180) * 65535)
    pca.channels[channel].duty_cycle = duty_cycle

# Example usage:
#servo_channel = 1  # The channel your servo is connected to
#time.sleep(1)  # Wait for 1 second
#set_servo_angle(servo_channel, 470)  # Set the servo to 0 degrees


