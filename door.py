import RPi.GPIO as GPIO
Pin=11
freq=50
GPIO.setmode(Pin,GPIO.OUT)
ServoGate=GPIO.PWM(Pin,freq)
def unlock():
    ServoGate.start(0)
    time.sleep(0.5)
    ServoGate.ChangeDutyCycle(2)
    time.sleep(0.5)
    ServoGate.ChangeDutyCycle(7)
    time.sleep(0.5)
    ServoGate.ChangeDutyCycle(0)
    time.sleep(0.5)
    ServoGate.ChangeDutyCycle(12)
    time.sleep(0.5)
    ServoGate.ChangeDutyCycle(0)

def lock():
    ServoGate.start(0)
    time.sleep(0.5)
    ServoGate.ChangeDutyCycle(12)
    time.sleep(0.5)
    ServoGate.ChangeDutyCycle(7)
    time.sleep(0.5)
    ServoGate.ChangeDutyCycle(0)
    time.sleep(0.5)
    ServoGate.ChangeDutyCycle(2)
    time.sleep(0.5)
    ServoGate.ChangeDutyCycle(0)
