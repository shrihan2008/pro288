from controller import Robot
from controller import Keyboard

robot = Robot()
kb = Keyboard()

# create unique identifier for each device

motorA=robot.getDevice("A motor")
motorA_pos=0

timestep = int(robot.getBasicTimeStep())
kb.enable(timestep)


# - perform simulation steps until Webots is stopping the controller
while robot.step(timestep) != -1:
    key_pressed = kb.getKey()   
    
    
    if(key_pressed==49):
        motorA_pos+=0.005
    
    if(key_pressed==50):
        motorA_pos-=0.005
        
     
    motorA.setPosition(motorA_pos)



    # write code to move the joints with keyboard
