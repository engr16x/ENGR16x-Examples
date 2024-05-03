# for Button, follow this code:
# https://github.com/Seeed-Studio/grove.py/blob/master/grove/grove_button.py

# For most of these, you will simply just need to rename the class to make the name simpler.
# You may change property namees/functions to be more consistent or easier to remember, but 
# that is not 100% necessary all the time.
# If you are confused on how the class works, consider changing it to be more intuitive
# so it is also easier for students

# Created by Aayush Iyengar on behalf on the ENGR 16X Teaching Team
import time
from grove.button import Button
from grove.factory import Factory

class GroveButton:
    '''
    Grove Button class

    Arguments:
        pin ---> type: int: the number of gpio/slot your grove device connected.
    '''
    def __init__(self, pin):
        #Initialize the GroveButton instance with the Button class
        self.button = Button(pin)
        self.last_press_time = time.time()  #Record the last press time
        self.on_press_callback = None
        self.on_release_callback = None
        self.button.on_event(self.handle_event)

    def handle_event(self, event):
        #Take the button press and release it
        elapsed_time = event["time"] - self.last_press_time
        self.last_press_time = event["time"]
        if event["code"] == Button.EV_LEVEL_CHANGED:
            if event["pressed"] and callable(self.on_press_callback):
                self.on_press_callback(elapsed_time)
            elif not event["pressed"] and callable(self.on_release_callback):
                self.on_release_callback(elapsed_time)

    def set_on_press_callback(self, callback):
        #Set the callback function for button press event
        if callable(callback):
            self.on_press_callback = callback

    def set_on_release_callback(self, callback):
        #Set the callback function for button release event
        if callable(callback):
            self.on_release_callback = callback

def run_button_example():
    #Main function to run the button example
    pin = 5  #Assuming pin 5 for the Grove Button

    button = GroveButton(pin)  #Create a GroveButton instance

    def on_press(elapsed_time):
        #Callback function for button press event
        print('Button is pressed')

    def on_release(elapsed_time):
        #Callback function for button release event
        print("Button is released, pressed for {0} seconds".format(round(elapsed_time, 6)))

    #Assign the callback functions to the button instance
    button.set_on_press_callback(on_press)
    button.set_on_release_callback(on_release)

    #Main loop to continuously check button state
    while True:
        time.sleep(1)

#Run the example when this script is executed
if __name__ == '__main__':
    run_button_example()
