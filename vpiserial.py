#!/usr/bin/env python3
import serial
import time
if __name__ == '__main__':
    ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
    ser.reset_input_buffer()
    ser.write(b"1001180\n")
    #while True:
        #line = ser.readline().decode('utf-8').rstrip()
        #if(line == "done"):
        #    print("done")
        #time.sleep(1)
