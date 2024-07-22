from basehat import Button  # Import the simplified Button class
import time
import cmdgui

#https://tldp.org/HOWTO/Bash-Prompt-HOWTO/x361.html
def Button_Test():
        result = ['BPButton_Test']
        
        bpmotorstage = cmdgui.stage(title = 'BrickPi Button Test',width = 60, height = 15)
        cmdgui.setstage(bpmotorstage)
        
        zerovalue = True

        pin = 5  #Assuming pin 5 for the Button
        button = Button(pin)  #Create a Button instance
        time.sleep(0.25)

        starttime = time.time()

        cmdgui.writeline(bpmotorstage,'Press the button. Test will time out in 5 seconds.',1)

        temp = 0
        
        while True:
                if (time.time() - starttime)>temp:
                        cmdgui.writeline(bpmotorstage,"Timeout in %1d" % int(5 - (time.time() - starttime)),3)
                        temp += 1

                if button.value == 1:
                        zerovalue = False
                        cmdgui.writeline(bpmotorstage,'boop!',4)
                        break
                elif time.time() - starttime > 5:
                        cmdgui.writeline(bpmotorstage,'Timed Out :(',4)
                        break

        if zerovalue:
                cmdgui.writeline(bpmotorstage,"ERROR: zero value detected",6)
                result.append('FAILED')
        else:
                cmdgui.writeline(bpmotorstage,"Non-zero values returned, good!",6)
                result.append('PASSED')
        cmdgui.writeline(bpmotorstage,str(result[0]+": " + result[1]),7)
        time.sleep(1)
        return(result)
