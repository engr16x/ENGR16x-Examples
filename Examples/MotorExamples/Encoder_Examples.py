# Encoder_Examples.py

# Created by Noah Grzegorek on behalf of the ENGR 16X Teaching Team

### DO NOT MODIFY CODE IN THIS FILE ###

from buildhat import motors
import time

def main():

    # set the pin to be used
    # if sensor is plugged into port A, pin should be 'A'
    # make sure to only plug in the motors to motor ports of the Grove BuildHat ('A', 'B', 'C', 'D')
    pin = 'A'

    # Initializing the motor so the functions within the class can be used
    motor = motors(pin)

    try: 
        while True:
            try: 
                # update and read the values of the motor
                speed = motor.get_speed()
                absPosition = motor.get_aposition()
                position = motor.get.get_position()

                # print values
                print("Motor speed: {}".format(speed))
                print("Absolute Position: {}".format(absPosition))
                print("Position: {}".format(position))

                time.sleep(1)

            except IOError:
                print ("\nError occurred while attempting to read values.")

    except KeyboardInterrupt:
        print("\nCtrl+C detected. Exiting...")
        break

if __name__ == '__main__':
    main()

