import time
from adafruit_pca9685 import PCA9685
import board
import busio
import adafruit_motor.servo

# Initialize the PCA9685 controller
i2c = busio.I2C(board.SCL, board.SDA)
pca = PCA9685(i2c,address=0x40)
servo=[]

pca.frequency = 25  # Set the PWM frequency (adjust if necessary)
for i in range(5):
    servo_channel=pca.channels[i]
    servo.append(i) = adafruit_motor.servo.Servo(servo_channel)   

servo[0].angle=0
servo[1].angle=0
servo[2].angle=0
servo[3].angle=0
servo[4].angle=0

time.sleep(0.7)

servo[0].angle=175
servo[1].angle=0
servo[2].angle=0
servo[3].angle=0
servo[4].angle=0

time.sleep(0.6)
servo[0].angle=175
servo[1].angle=170
servo[2].angle=0
servo[3].angle=2
servo[4].angle=2
time.sleep(0.5)
servo[0].angle=175
servo[1].angle=170
servo[2].angle=178
servo[3].angle=2
servo[4].angle=2
time.sleep(0.4)
servo[0].angle=175
servo[1].angle=170
servo[2].angle=178
servo[3].angle=160
servo[4].angle=0
time.sleep(0.5)
servo[0].angle=175
servo[1].angle=170
servo[2].angle=180
servo[3].angle=172
servo[4].angle=180

time.sleep(1.8)

servo[0].angle=0
servo[1].angle=2
servo[2].angle=180
servo[3].angle=175
servo[4].angle=2

time.sleep(2.3)

servo[0].angle=0
servo[1].angle=1
servo[2].angle=4
servo[3].angle=0
servo[4].angle=1

time.sleep(1.5)

servo[0].angle=0
servo[1].angle=2
servo[2].angle=180
servo[3].angle=4
servo[4].angle=1

time.sleep(1)

servo[0].angle=0
servo[1].angle=0
servo[2].angle=0
servo[3].angle=0
servo[4].angle=0

time.sleep(1)

def set_servo_angle(channel, angle):
    duty_cycle = int((angle / 180) * 65535)
    pca.channels[channel].duty_cycle = duty_cycle

# Example usage:
#servo_channel = 1  # The channel your servo is connected to
#time.sleep(1)  # Wait for 1 second
#set_servo_angle(servo_channel, 470)  # Set the servo to 0 degrees
