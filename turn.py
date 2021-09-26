def on(num):
    print("Node {} and nearby light and fan are provided power".format(num))
def off(num):
    print("Node {} and nearby light and fan are turned off".format(num))
'''
import RPi.GPIO as GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.OUT)
GPIO.setup(13,GPIO.OUT)
GPIO.setup(15,GPIO.OUT)
GPIO.setup(19,GPIO.OUT)
def on(num):
    GPIO.output(num,1)
    print("Node {} and nearby light and fan are provided power".format(num))
def off(num):
    GPIO.output(num,0)
    print("Node {} and nearby light and fan are provided power".format(num))
'''