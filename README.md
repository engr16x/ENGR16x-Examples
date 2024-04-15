GitHub Organization
https://github.com/SethThMc/ENGR16x-Examples
There are 3 main folders in the GitHub: buildhat, basehat, and Examples. Buildhat has all of the code for the motors, basehat has all of the code for the sensors, and the Examples folder has examples for everything.

The other folder, projects-rpi-setup-6, has old imaging scripts as well as old example files, which are located under projects-rpi-setup-6/files/new_desktop/Examples.

Sensors
For each sensor, an existing Python class must be modified and an example script must be written.

Class Modification
Each sensor has an existing class made, but some of them are a little confusing. For example, the GroveButton class has confusing properties like “on_press” or “on_release” that makes using the sensor difficult, especially for students new to programming. Changing this class to simply return the value of the button at that moment would be much simpler. Whatever you think would be easiest for the student to understand, you should do that. 

Also, a lot of the sensor classes have “Grove” in front of it, or for the IMU, it is just a really long name. Rename all classes to be as simple as possible. Just make sure to add “Sensor” at the end of the class name. The files where you will write each class have been created for you, so as long as you follow the naming conventions of the file, you will be fine.

There is a file called template.py in the basehat folder of the GitHub. Follow this for documentation and commenting of each file. As an example, I completed all of the code and commenting for IRSensor.py and IRSensor_Example.py, so you may want to reference these often so we stay consistent.

Example File
The example files should be kept pretty simple. There are some examples attached in the GitHub repository from the old system, and I wrote an example for the IRSensor.py file. When possible, try to use “try:” and “except:” , which is demonstrated in the old example files and the one I wrote. Also, try to use a while True: loop for most of them with time.sleep() as well. These should be pretty easy.




Motors

Class Modification
There is no modification needed to the Motor class.

Example File
There will be two example files for the motors: one for the encoder functions and one for the movement functions. The movement function example file should have usage for the following movement functions: start, stop, run_for_degrees, run_for_rotations, run_for_seconds, run_to_position, and set_default_speed. An example file is provided for you for how all of these functions are accessed in the Run_Examples.py file. Make modifications to this example file so that the student can uncomment what function they want to run, and comment out the rest that they don’t want to run, all of this inside a while True: loop with a good amount of time.sleep()’s.

For the encoder example file, the following functions must be demonstrated: get_speed, get_apostion, and get_position. Just print the outputs of these functions in a while True: loop.

Assignments
The code you should be basing everything off of is linked in each file that you need to fill out. Here are the files you should be completing:

Noah:
basehat/IMUSensor.py
Examples/SensorExamples/IMUSensor_Example.py
basehat/LineFinder.py
Examples/SensorExamples/LineFinder_Example.py
basehat/UltrasonicSensor.py
Examples/SensorExamples/UltrasonicSensor_Example.py
Aayush
basehat/Button.py
Examples/SensorExamples/Button_Example.py
basehat/LightSensor.py
Examples/SensorExamples/LightSensor_Example.py
Examples/MotorExamples/Encoder_Examples.py
Examples/MotorExamples/Run_Examples.py

Submitting and Testing Code
When you are finished, go ahead and push to the GitHub repository, and text me you are finished. I will then test your code on the Pi. If there is something wrong and it is a quick fix, I will fix it real quick and then let you know if it works. If not, I will send you the errors and we’ll go from there.

Resources

BaseHAT:
https://wiki.seeedstudio.com/Grove_Base_Hat_for_Raspberry_Pi/
https://github.com/Seeed-Studio/grove.py

BuildHAT:
https://github.com/RaspberryPiFoundation/python-build-hat/

Motors:
https://github.com/RaspberryPiFoundation/python-build-hat/blob/main/test/motors.py
https://buildhat.readthedocs.io/en/latest/buildhat/motor.html

Light Sensor:
https://wiki.seeedstudio.com/Grove-Light_Sensor/
https://github.com/Seeed-Studio/grove.py/blob/master/grove/grove_light_sensor_v1_2.py

IMU:
https://github.com/Seeed-Studio/grove.py/blob/master/grove/grove_imu_9dof_icm20600_ak09918.py
https://wiki.seeedstudio.com/Grove-IMU_9DOF-lcm20600+AK09918/

LineFinder:
https://gpiozero.readthedocs.io/en/stable/api_input.html#gpiozero.LineSensor
https://github.com/gpiozero/gpiozero/blob/master/gpiozero/input_devices.py (search LineSensor)
https://wiki.seeedstudio.com/Grove-Line_Finder/

Button:
https://github.com/Seeed-Studio/grove.py/blob/master/grove/grove_button.py
https://wiki.seeedstudio.com/Grove-Button/

Ultrasonic Sensor:
https://github.com/Seeed-Studio/grove.py/blob/master/grove/grove_ultrasonic_ranger.py
https://wiki.seeedstudio.com/Grove-Ultrasonic_Ranger/

Template:
https://github.com/SethThMc/ENGR16x-Examples/blob/main/basehat/template.py
https://github.com/SethThMc/ENGR16x-Examples/blob/main/basehat/IRSensor.py
https://github.com/SethThMc/ENGR16x-Examples/blob/main/Examples/SensorExamples/IRSensor_Example.py
