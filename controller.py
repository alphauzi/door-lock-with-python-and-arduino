from pyfirmata2 import Arduino, SERVO
import time

port = 'COM19'
pin=10

board=Arduino(port)
board.digital[pin].mode=SERVO

def rotateServo(pin, angle):
    board.digital[pin].write(angle)


def doorAutomate(val):
    if val==0:
        rotateServo(pin, 50)
        time.sleep(3)
    elif val==1:
        rotateServo(pin, 150)
