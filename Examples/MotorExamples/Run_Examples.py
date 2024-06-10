# Run_Examples.py

# Created by Noah Grzegorek on behalf of the ENGR 16X Teaching Team

# More info and instruction on using this sensor can be found in the buildhat folder
# on your Pi's Desktop 

# import the necessary packages for your sensor and code
import time
from buildhat import Motor

def main():
    
    # set the pin to be used
    # if sensor is plugged into port A, pin should be 'A'
    # make sure to only plug in the motors to motor ports of the Grove BuildHat ('A', 'B', 'C', 'D')
    motor = Motor('A')
    print("Initiating BuildHAT and motors")
    print("this may take a while (~10 seconds)")

    # uncomment to use Motor B
    # motorb = Motor('B')

    # Function to print the current speed, position and absolute position of the motors
    def handle_motor(speed, pos, apos):
        """Motor data

        :param speed: Speed of motor
        :param pos: Position of motor
        :param apos: Absolute position of motor
        """
        print("Motor", speed, pos, apos)

    try: 
        while True:
            try:
                # Any of these two to five line blocks can be uncommented to test and play with the functionality
                # of the various motor functions that are available with the motors
                print("Motor Testing")

                # Leave these lines uncommented because they print the current speed, position and absolute position
                # of the motors and set the default speed
                #motor.when_rotated = handle_motor
                #motor.set_default_speed(50)

                # print("Run for degrees 360")
                # motor.run_for_degrees(360)
                # time.sleep(3)

                # print("Run for degrees -360")
                # motor.run_for_degrees(-360)
                # time.sleep(3)

                # print("Start motor")
                # motor.start()
                # time.sleep(3)
                # print("Stop motor")
                # motor.stop()
                # time.sleep(1)

                # print("Run for degrees - 180")
                # motor.run_for_degrees(180)
                # time.sleep(3)

                # print("Run for degrees - 90")
                # motor.run_for_degrees(90)
                # time.sleep(3)

                # print("Run for rotations - 2")
                # motor.run_for_rotations(2)
                # time.sleep(3)

                # print("Run for seconds - 5")
                # motor.run_for_seconds(5)
                # time.sleep(3)

                # print("Run both")
                # motor.run_for_seconds(5, blocking=False)
                # motorb.run_for_seconds(5, blocking=False)
                # time.sleep(10)

                # print("Run to position -90")
                # motor.run_to_position(-90)
                # time.sleep(3)

                # print("Run to position 90")
                # motor.run_to_position(90)
                # time.sleep(3)

                # print("Run to position 180")
                # motor.run_to_position(180)
                # time.sleep(3)

            except IOError:
                print ("\nError occurred while attempting to read values.")
                break

    except KeyboardInterrupt:
        print("\nCtrl+C detected. Exiting...")

if __name__ == '__main__':
    main()
