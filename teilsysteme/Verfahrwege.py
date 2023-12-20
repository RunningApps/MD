from teilsysteme import StepMotor as sm
from teilsysteme import UltraSonic as us
from multiprocessing import Process
import multiprocessing
import time

class ProcessHandler():
    def __init__(self):
        super().__init__()
        
    def terminate_process(self, process: Process) -> None:
        process.terminate()
        process.join()
    
class Verfahrwege(ProcessHandler):
    def __init__(self) -> None:
        super().__init__()

        self.x_step = sm.StepMotor(2, 4, 6)
        self.y_step = sm.StepMotor(8, 10, 12)

        self.right_ultra_sonic  = us.UltraSonic()
        self.left_ultra_sonic  = us.UltraSonic()
        self.top_ultra_sonic  = us.UltraSonic()
        self.bottom_ultra_sonic  = us.UltraSonic()

        self.panel_width = 300
        self.panel_height = 600
        self.brush_height = 100
    
    def start_process(self, fnc: str, args: list) -> Process:
        dist, dir, speed = args
        process = multiprocessing.Process(target=eval(fnc), args=(dist, dir, speed)) 
        process.start()
        return process
    
    def check_border(self, move, sensor_type):
        match sensor_type:
            case "top":
                while(True):
                    if self.top_ultra_sonic.distance > 0.1:
                        self.terminate_process(move) 
                        return

            case "bottom":
                while(True):
                    if self.bottom_ultra_sonic.distance > 0.1:
                        self.terminate_process(move)  
                        return    

            case "left":
                while(True):
                    if self.left_ultra_sonic.distance > 0.1:
                        self.terminate_process(move)  
                        return

            case "right":
                while(True):
                    if self.right_ultra_sonic.distance() > 0.1:
                        self.terminate_process(move) 
                        return

            case "all":
                while(True):
                    if  (self.bottom_ultra_sonic.distance > 0.1)  or (self.top_ultra_sonic.distance > 0.1)  or (self.right_ultra_sonic.distance > 0.1) or (self.left_ultra_sonic.distance > 0.1):
                        self.hbridge.enable(False)
                        self.terminate_process(move) 
                        return

            case default:
                print("Not available")
                return None

    def reference(self):
        move = multiprocessing.Process(target = self.x_step)
        move.start()
        self.check_border(move)        

        move = multiprocessing.Process(target = self.y_step)
        move.start()
        self.check_border(move) 
        
    def route_1(self):    
        args = [1, "Right", 60]
        process = self.start_process("self.x_step.move", args)
        self.check_border(process, "right")

