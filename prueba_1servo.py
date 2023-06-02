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
        #    kit.servo[1].angle = 40
        #    kit.servo[2].angle = 40
        #    kit.servo[3].angle = 40
        #    kit.servo[4].angle = 40

        # else:
        #    finger.append(0)


        fingers=[]
        # for id in range(0,4):
        #     if a[tip[id]][2:] < a[tip[id]-2][2:]:

        #        print(b[tipname[id]])

        #        if a[tip[2]] < a[tip[2]-2]:
        #            kit.servo[0].angle = 50
        #        fingers.append(1)
        #     else:
        #        fingers.append(0)
               #MY ADDITIONS
        kit.servo[0].angle = 120
        # kit.servo[1].angle = 140
        # kit.servo[2].angle = 130
        # kit.servo[3].angle = 160
        # kit.servo[4].angle = 140
    #  x=fingers + finger
    #  c=Counter(x)
    #  up=c[1]
    #  down=c[0]
    #  print(up)
    #  print(down)
    #  cv2.imshow("Frame", frame1);
    #  key = cv2.waitKey(1) & 0xFF
    #  if key == ord("q"):
    #     speak("sir you have"+str(up)+"fingers up  and"+str(down)+"fingers down")
    #  if key == ord("s"):
    #    break
