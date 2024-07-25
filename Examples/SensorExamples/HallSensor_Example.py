# IRSensor_Example.py

# Created by Owen Bishop on behalf of the ENGR 16X Teaching Team

# More info and instruction on using this sensor can be found in the basehat folder
# on your Pi's Desktop 

# import the necessary packages for your sensor and code
from basehat import HallSensor
import time

def main():

    # set the pin to be used
    # if sensor is plugged into port A0, pin1 should be 0
    # make sure to only plug in Hall Sensor to analog ports of the Grove BaseHAT (A0, A2, A4, A6)
    pin = 5

    # initialize the sensor by naming the class instance and setting the pins to use
    # 'Hall' is the name of the instance, pin is the pin being used
    Hall = HallSensor(pin)
    print('Detecting magnetic fields...')

    try: 
        while True:
            try: 
                # update and read the value from the hall sensor
                value = Hall.value

                # print value
                print("Hall value: {}".format(value))

                time.sleep(0.5)

            except IOError:
                print ("\nError occurred while attempting to read values.")
                break
            
    except KeyboardInterrupt:
        print("\nCtrl+C detected. Exiting...")

if __name__ == '__main__':
    main()

