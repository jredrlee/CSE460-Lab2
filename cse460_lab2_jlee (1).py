import time
#motor code
from Motor import *
motor = Motor()

#LED code
from Led import *
led = Led()

#Buzzer code
from Buzzer import *
buzzer = Buzzer()


#Destroy function
def destroy():
    motor.setMotorModel(0,0,0,0)
    
#main code
if __name__ == '__main__':
    print("The Program is starting...")
    try:
        motor.setMotorModel(1000,1000,1000,1000)       #Forward
        print ("The car is moving forward")
        time.sleep(2)
        motor.setMotorModel(0,0,0,0)
        time.sleep(0.5)
        motor.setMotorModel(-1500,-1500,1500,1500)       #Forward
        print ("The car is turning 90 degrees left")
        time.sleep(1)
        led.ledIndex(0x01,255,0,0)      #Red
        
        motor.setMotorModel(1000,1000,1000,1000)       #Forward
        print ("The car is moving forward")
        time.sleep(2)
        motor.setMotorModel(0,0,0,0)
        time.sleep(0.5)
        motor.setMotorModel(-1500,-1500,1500, 1500)
        print ("The car is turning 90 degrees left")
        time.sleep(1)
        led.ledIndex(0x02,0,0,255)      #blue
        
        
        motor.setMotorModel(1000,1000,1000,1000)       #Forward
        print ("The car is moving forward")
        time.sleep(2)
        motor.setMotorModel(0,0,0,0)
        time.sleep(0.5)
        motor.setMotorModel(-1500,-1500,1500, 1500)
        print ("The car is turning 90 degrees left")
        time.sleep(1)
        led.ledIndex(0x04,0,225,0)      #blue
        
        
        motor.setMotorModel(1000,1000,1000,1000)       #Forward
        print ("The car is moving forward")
        time.sleep(2)
        motor.setMotorModel(0,0,0,0)
        time.sleep(0.5)
        motor.setMotorModel(-1500,-1500,1500, 1500)
        print ("The car is turning 90 degrees left")
        time.sleep(1)
        motor.setMotorModel(0,0,0,0)
        led.ledIndex(0x08,225,225,0)      #blue
        buzzer.run('1')
        time.sleep(3)
        
        led.colorWipe(led.strip, Color(0,0,0))  #turn off the light
        buzzer.run('0')
        print ("\nEnd of program")
        
    
    #stop program from executing
    except KeyboardInterrupt:
        destroy()
    
    