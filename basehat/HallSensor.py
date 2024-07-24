# HallSensor.py

# Created by Owen Bishop on behalf of the ENGR 16X Teaching Team

### DO NOT MODIFY CODE IN THIS FILE ###

'''
Hall Sensor:
    Description:
        This sensor has only one value that can be accessed: a value from 0 to 999 that is 
        dependent on the strength of magnetic field present at the sensor. 

    Hardware:
        Connect this sensor to any analog port on the Grove BaseHAT: A0, A2, A4, or A6.
        Initialize the sensor using only the number of the port, DO NOT include the A.
        
        More info:
        https://wiki.seeedstudio.com/Grove_Base_Hat_for_Raspberry_Pi/
        https://wiki.seeedstudio.com/Grove-Hall_Sensor/


    Initialization:

        sensor_name = HallSensor(pin)

        If you plug your Hall Sensor into A0 and want to name it 'Hall', your initialization will
        look like this:

        Hall = HallSensor(0)
    
    HallSensor.value:
        Read the value from the sensor. If your sensor's name is 'Hall', accessing the value will
        look like this:

        value_from_sensor = Hall.value
        
    
    HallSensor_Example.py: 
        Usage of this code is demonstrated in the example file for this sensor in the Examples
        folder on your Pi's desktop.
        
'''

### DO NOT MODIFY CODE BELOW THIS LINE ###

from grove.adc import ADC

class HallSensor(object):
    '''
    Hall Sensor class

    Args:
        pin(int): number of the analog pin the sensor is connected to.
    '''
    def __init__(self, pin):
        self.pin = pin
        self.adc = ADC()

    @property
    def value(self):
        '''
        Get the magnetic strength value, maximum value is 999, with lower values representing stronger mangetic fields
        Returns:
            (int): ratio, 0 - 999
        '''
        value = self.adc.read(self.port)
        return value
