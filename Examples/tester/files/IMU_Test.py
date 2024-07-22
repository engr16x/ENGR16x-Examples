from basehat import IMUSensor
import time
import cmdgui

def IMU_Test():
        IMU = IMUSensor()

        imustage = cmdgui.stage('IMU Test',60,15)
        cmdgui.setstage(imustage)
        
        result = ['IMU_Test']

        cmdgui.writeline(imustage,'IMU will Read for 5 seconds, spin it!',1)
        
        zerovalue = False
        for i in range(10):

            accel_x,accel_y,accel_z = IMU.getAccel()

            if (accel_x == 0) or (accel_y == 0) or (accel_z == 0):
                zerovalue = True

            cmdgui.writeline(imustage,'X: ' + str(accel_x),3)
            cmdgui.writeline(imustage,'Y: ' + str(accel_y),4)
            cmdgui.writeline(imustage,'Z: ' + str(accel_z),5)
            
            time.sleep(0.5)

        if zerovalue:
                cmdgui.writeline(imustage,'ERROR: zero value detected',7)
                result.append('FAILED')
        else:
                cmdgui.writeline(imustage,'Non-zero values returned, good!',7)
                result.append('PASSED')
        cmdgui.writeline(imustage,str(result[0]+": " + result[1]),8)
        time.sleep(1)
        return(result)
