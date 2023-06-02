from adafruit_servokit import ServoKit
kit = ServoKit(channels=8)
from time import *


kit.servo[0].angle = 140
# kit.servo[1].angle = 140
# kit.servo[2].angle = 130
# kit.servo[3].angle = 160
# kit.servo[4].angle = 140



while True:
           #My Additions
        kit.servo[0].angle = 50


