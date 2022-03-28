import RPi.GPIO as GPIO
import sys
import time

GPIO.setmode(GPIO.BOARD)

# TB6600 Treiber Setup
DIR = 11
PUL = 13
ENA = 15

# POS
POS = 0
BUSY = 0

DIR_Left = GPIO.HIGH
DIR_Right = GPIO.LOW

ENA_Locked = GPIO.LOW
ENA_Released = GPIO.HIGH

GPIO.setwarnings(False)
GPIO.setup(DIR, GPIO.OUT)
GPIO.setup(PUL, GPIO.OUT)
GPIO.setup(ENA, GPIO.OUT)

# Motor Setup
STEP_ANGLE = 1.8 # degree
RAMP_LENGTH = 600 # steps
MIN_RPM = 250
MAX_RPM = 3200
STEP_CAL = 5000

# Frequenzberechnung
stepsPerRevolution = 360 / STEP_ANGLE

minFrequency = 1 / (MAX_RPM / 60 * stepsPerRevolution)
maxFrequency = 1 / (MIN_RPM / 60 * stepsPerRevolution)

rampSlope = (maxFrequency - minFrequency) / RAMP_LENGTH

def calculateStepsDestination(iDestination, iDirection, iOver):
    steps = 0
    global POS
    global BUSY
    direction = int(iDirection)
    destination = int(iDestination)
    over = int(iOver)

    if direction == 1:
        #CW
        print("Direciton is 1")
        if destination > POS:
            steps = destination - POS
        elif destination < POS:
            steps = 360 - POS + destination
        elif destination == POS:
            steps = 0

    elif direction == 0:
        # CCW
        print("Direciton is 0")
        if destination > POS:
            steps = 360 - destination + POS
        elif destination < POS:
            steps = POS - destination
        elif destination == POS:
            steps = 0

    # Drüberdrehen wie oft
    #if over != 0:
        #steps = steps + over * 360

    if direction == 0:
        steps = steps * -1
    print("line 67 - STEPS: ")
    print(steps)
    
    if BUSY == 0:
        moveBy(steps)
    else:
        print("Motor is Busy")

def setCueStartPoint(destination):
    steps = 0
    if POS > destination:
        calculateStepsDestination(destination, 0, 0)
    else:
        calculateStepsDestination(destination, 1, 0)


def moveBy(steps):
    global BUSY
    BUSY = 1
    print ("Steps: ")
    print (steps)
    print (" x ")
    print (STEP_CAL)
    steps = steps * STEP_CAL
    print (" = ")
    print (steps)

    global POS

    GPIO.output(ENA, ENA_Locked)
    currentFreqency = maxFrequency

    for i in range(abs(steps)):

    # Richtung festlegen
        if (steps < 0):
            GPIO.output(DIR, DIR_Right)
        else:
            GPIO.output(DIR, DIR_Left)

        # Schritt ausführen
        GPIO.output(PUL, GPIO.HIGH)
        time.sleep(currentFreqency / 2)

        GPIO.output(PUL, GPIO.LOW)
        time.sleep(currentFreqency / 2)

        # aktuelle Schrittposition mitzählen
        if (steps < 0):
            POS -= 1
            #print(POS / (200.*16))
        else:
            POS += 1
            #print(POS / (200.*16))


        # Rampensteigung auf aktuelle Frequenz anwenden
        if (abs(steps) > 2 * RAMP_LENGTH):
            if (i < RAMP_LENGTH):
                currentFreqency -= rampSlope
            else:
                if (i > abs(steps) - RAMP_LENGTH):
                    currentFreqency += rampSlope
        else:
            if (i < abs(steps) / 2):
                currentFreqency -= rampSlope
            else:
                currentFreqency += rampSlope

    GPIO.output(ENA, ENA_Released)
    BUSY = 0