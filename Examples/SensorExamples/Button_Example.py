# Created by Aayush Iyengar on behalf on the ENGR 16X Teaching Team

from grove_button import GroveButton  # Import the simplified GroveButton class
#connecting with the grove button for the button connected in pin 5 (this is customizable below)

def on_press(elapsed_time):
    #Callback function for button press event
    print('Button is pressed')

def on_release(elapsed_time):
    #Callback function for button release event
    print("Button is released, pressed for {0} seconds".format(round(elapsed_time, 6)))

def main():
    #Main function
    pin = 5  #Assuming pin 5 for the Grove Button

    button = GroveButton(pin)  #Create a GroveButton instance

    #Assign the callback functions to the button instance
    button.set_on_press_callback(on_press)
    button.set_on_release_callback(on_release)

    #Main loop to continuously check button state
    while True:
        #The button events will trigger the callback functions
        pass  #keep the program running

if __name__ == '__main__':
    main()