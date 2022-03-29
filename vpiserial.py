#!/usr/bin/env python3
import serial
import time
import sys

if __name__ == '__main__':
    ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
    ser.reset_input_buffer()
    einmal = 0
    print("HELLO SLEEP")
    time.sleep(5)
    ser.write(str("1001180\n").encode('utf-8'))
    time.sleep(5)
    sys.exit()

    while True:
        line = ser.readline().decode('utf-8').rstrip()
        print(line)
        time.sleep(1)
        einmal = einmal + 1
