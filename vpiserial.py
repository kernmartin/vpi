#!/usr/bin/env python3
import serial
import time
if __name__ == '__main__':
    ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
    ser.reset_input_buffer()
    einmal = 0
    while True:
        if(einmal == 0):
            ser.write(str("1001180\n").encode('utf-8'))
            einmal = einmal + 1
        line = ser.readline().decode('utf-8').rstrip()
        print(line)
        time.sleep(1)
