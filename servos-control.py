import RPi.GPIO as GPIO
import time

# we're going to use the BOARD pin-numbering scheme
GPIO.setmode(GPIO.BOARD) 

# define the GPIO pin numbers
servoPINs = [2, 3, 4, 14, 15]

# set them as output
for pin in servoPINs:
    GPIO.setup(pin, GPIO.OUT)

# set all the pins to use PWM at 50 Hz
servos = [GPIO.PWM(pin, 50) for pin in servoPINs]

# initialization
for servo in servos:
    servo.start(2.5)

def move_servos(positions):
    for servo, position in zip(servos, positions):
        servo.ChangeDutyCycle(position)
    time.sleep(0.1)

try:
    while True:
        # Here you can replace with the code that gets the positions for the servos
        # positions should be a list with 5 elements, each between 2.5 to 12.5
        # For example, let's use [2.5, 5, 7.5, 10, 12.5]
        positions = [2.5, 5, 7.5, 10, 12.5]
        move_servos(positions)
        
except KeyboardInterrupt:
    # stop the PWM output
    for servo in servos:
        servo.stop()
    # reset the GPIO settings
    GPIO.cleanup()