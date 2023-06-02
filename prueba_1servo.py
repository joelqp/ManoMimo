import time
from adafruit_pca9685 import PCA9685
import board
import busio
# Initialize the PCA9685 controller
i2c = busio.I2C(board.SCL, board.SDA)
pca = PCA9685()
pca.frequency = 50  # Set the PWM frequency (adjust if necessary)

def set_servo_angle(channel, angle):
    duty_cycle = int((angle / 180) * 65535)
    pca.channels[channel].duty_cycle = duty_cycle

# Example usage:
servo_channel = 0  # The channel your servo is connected to
set_servo_angle(servo_channel, 90)  # Set the servo to 90 degrees
time.sleep(1)  # Wait for 1 second
set_servo_angle(servo_channel, 0)  # Set the servo to 0 degrees
