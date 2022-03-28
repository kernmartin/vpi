import RPi.GPIO as GPIO
import sys
import time
from RpiMotorLib import RpiMotorLib

GPIO.setmode(GPIO.BOARD)

# TB6600 Treiber Setup
DIR = 11
PUL = 13
ENA = 15


# POS
POS = 0
BUSY = 0
STOP = 0

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
RAMP_LENGTH = 300 # steps
MIN_RPM = 150
MAX_RPM = 250
STEP_CAL = 3200 * 180
DEGREE_STEP = STEP_CAL / 360
WORM_GEAR = 180
STEPS_REV = 288500
# WORM 180 * 3200
# STEPS 3200 pro 360
# Frequenzberechnung
stepsPerRevolution = 3200

minFrequency = 1 / (MAX_RPM / 60 * stepsPerRevolution)
maxFrequency = 1 / (MIN_RPM / 60 * stepsPerRevolution)

rampSlope = (maxFrequency - minFrequency) / RAMP_LENGTH



def calculateStepsDestination(iDestination, iDirection, iOver):

    steps = 0
    direction = int(iDirection)
    destination = int(iDestination)
    over = int(iOver)
    global POS
    global STOP
    global BUSY

    print("STARTING AT ", POS, " GOING TO: ", destination)

    if BUSY == 1:
        stopMotor()
        STOP = 0
        BUSY = 0

    if direction == 1:
        #CW
        print("Direction is 1 CW")
        if destination > POS:
            steps = destination - POS
            print("CW destination > POS")
        elif destination < POS:
            steps = 360 - POS + destination
            print("CW Destination < POS")
        elif destination == POS:
            steps = 0
            print("POS already on position")

    elif direction == 0:
        # CCW
        print("Direction is 0 CCW")
        if destination > POS:
            steps = 360 - destination + POS
            print("CCW destination > POS")
        elif destination < POS:
            steps = POS - destination
            print("destination < POS")
        elif destination == POS:
            steps = 0
            print("Already on position")

    # Drüberdrehen wie oft
    if over != 0:
        steps = steps + over * 360

    if direction == 0:
        steps = steps * -1

    moveBy(int(steps))

def setCueStartPoint(destination):
    steps = 0
    if POS > destination:
        calculateStepsDestination(destination, 0, 0)
    else:
        calculateStepsDestination(destination, 1, 0)


def moveBy(steps):
    print("moveBY DEGREE incoming: ", steps)
    global BUSY
    global POS
    global STOP
    BUSY = 1
    print("HARDCODED STEPS ", steps)

    counter = 0

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
            time.sleep(minFrequency)

            GPIO.output(PUL, GPIO.LOW)
            time.sleep(minFrequency)

            # aktuelle Schrittposition mitzählen
            if (steps < 0):
                POS -= 1
                print("Position: ", POS)
            else:
                POS += 1
                print("Position: ", POS)


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
    POS = round(POS)
    BUSY = 0
    STOP = 0
    print("Finished at POS: ", POS)

def stopMotor():
    print("def StopMotor: ")
    global STOP
    global POS
    global BUSY
    STOP = 1
    POS = round(POS)
    print("Motor stopped at Position: ", POS)
