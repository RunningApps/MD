from .stepmotor import *
from .ultrasonic import *
from .ProcessHandler import *
from .datastream import *

import time
    
class Verfahrwege():
    def __init__(self) -> None:
        self.processhandler = ProcessHandler()
        self.ultra_sonic  = UltraSonic()
        self.x_step = StepMotor(21, 20, 16) # Raspi GPIO pins
        self.y_step = StepMotor(8, 10, 12)
    
    def check_border(self, move: Process) -> None:
        while(True):
            if  (self.ultra_sonic.distance_bottom() > 0.1)  or (self.ultra_sonic.distance_left() > 0.1)  or (self.ultra_sonic.distance_right() > 0.1) or (self.ultra_sonic.distance_top() > 0.1):
                self.x_step.disable()
                self.y_step.disable()
                self.processhandler.terminate_process(move) 
                return

    def reference(self):
        print("X-Stepmotor now active")
        move = self.processhandler.start_process(self.x_step.move, 10000, "Right", 60)
        self.check_border(move)        
        print("X-Stepmotor now disabled")

        print("Y-Stepmotor now active")
        move = self.processhandler.start_process(self.y_step.move, 10000, "Right", 60)
        self.check_border(move)  
        print("Y-Stepmotor now disabled")

    def route_1(self):  
        pass    

    def route_2(self):
        pass

    def route_3(self):
         pass  

    def route_4(self):
        pass