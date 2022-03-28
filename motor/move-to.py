import vpimotor
import sys


if (len(sys.argv) != 2):
	print("missing parameter: steps");
	sys.exit();


steps = int(sys.argv[1])
#print("steps: " + str(steps))

currentPosition = vpimotor.moveTo(steps)
print(currentPosition)
