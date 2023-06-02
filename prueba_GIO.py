import RPi.GPIO as GPIO
import time

# we're going to use the BOARD pin-numbering scheme
GPIO.setmode() 

# define the GPIO pin numbers
servoPIN1 = 1

# set them as output
GPIO.setup(servoPIN1, GPIO.OUT)

# set all the pins to use PWM at 50 Hz
p1 = GPIO.PWM(servoPIN1, 50)

# initialization
p1.start(2.5)

try:
    while True:
        # Rotate servos to 0 degrees
        p1.ChangeDutyCycle(2.5)
        time.sleep(1)
        # Rotate servos to 90 degrees
        p1.ChangeDutyCycle(7.5)
        time.sleep(1)
        # Rotate servos to 180 degrees
        p1.ChangeDutyCycle(12.5)
        time.sleep(1)
        
except KeyboardInterrupt:
    # stop the PWM output
    p1.stop()

    # reset the GPIO settings
    GPIO.cleanup()
