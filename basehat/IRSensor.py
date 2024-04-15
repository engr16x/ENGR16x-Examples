# IRSensor.py

# Created by Seth McConkey on behalf of the ENGR 16X Teaching Team

### DO NOT MODIFY CODE IN THIS FILE ###

'''
IR Sensor:
    Description:
        This sensor has two values that can be accessed: a value from 0 to 999 that is 
        proportional to the amount of infrared rays the left sensor is reading, and a value 
        from 0 to 999 that is proportional to the amount of infrared rays the left sensor is 
        reading. It is used to determine presence/distance of an infrared source, such as an 
        LED light or Infrared Beacon.

    Hardware:
        Connect this sensor to any analog port on the Grove BaseHAT: A0, A2, A4, or A6.
        Initialize the sensor using only the number of the port, DO NOT include the A.
        
        More info:
        https://wiki.seeedstudio.com/Grove_Base_Hat_for_Raspberry_Pi/
        https://wiki.seeedstudio.com/Grove-Infrared_Reflective_Sensor/


    Initialization:

        sensor_name = IRSensor(pin, pin + 1)

        If you plug your IR Sensor into A0 and want to name it 'IR', your initialization will
        look like this:

        IR = IRSensor(0, 1)
    
    IRSensor.valueL:
        Read the value from the left sensor. If your sensor's name is 'IR', accessing the left
        value will look like this:

        value_from_left_sensor = IR.valueL

    IRSensor.valueR:
        Read the value from the right sensor. If your sensor's name is 'IR', accessing the right
        value will look like this:

        value_from_right_sensor = IR.valueR
    
    IRSensor_Example.py: 
        Usage of this code is demonstrated in the example file for this sensor in the Examples
        folder on your Pi's desktop.
'''

### DO NOT MODIFY CODE BELOW THIS LINE ###

# original code for comparison:
# adapted from light sensor code:
# https://github.com/Seeed-Studio/grove.py/blob/master/grove/grove_light_sensor_v1_2.py

from grove.adc import ADC

class IRSensor(object):
    '''
    IR Sensor class

    Args:
        pin(int): number of the analog pin the sensor is connected to.
    '''
    def __init__(self, channel1, channel2):
        self.channel1 = channel1
        self.channel2 = channel2
        self.adc = ADC()

    @property
    def valueL(self):
        '''
        Get the infrared strength value, maximum value is 999

        Returns:
            (int): ratio, 0 - 999
        '''
        value = self.adc.read(self.channel1)
        return value

    @property
    def valueR(self):
        '''
        Get the infrared strength value, maximum value is 999

        Returns:
            (int): ratio, 0 - 999
        '''
        value = self.adc.read(self.channel2)
        return value
