#No line sensors - DONE
#Add IR sensor
#Change motor duration - DONE (note this is applied in the BPMotor_Test.py file and as such applies to the V1 testfile too)

import basehat
import buildhat
import sys
import time

import cmdgui
from IMU_Test import *
from Ultrasonic_Test import *
from Button_Test import *
from Motor_Test import *
from IR_Test import *
from printresults import *

if __name__ == "__main__":
        try:
                testresults = []
                testresults.append(IMU_Test())
                testresults.append(Ultrasonic_Test())
                testresults.append(IR_Test())
                testresults.append(Button_Test())
                testresults.append(Motor_Test())

                printresults(testresults)

                while True:
                        if KeyboardInterrupt:
                                sys.exit

        except KeyboardInterrupt:
                sys.exit()

