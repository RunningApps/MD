import StepMotor as sm
import HBridge as hb

class Verfahrwege:
    def __init__():
        stepmotor = sm.StepMotor() 
        hbridge_x = hb.HBridge()
        hbridge_y = hb.HBridge()

        panel_width = 300
        panel_height = 600
        brush_height = 10
        brush_length = 50
        
    def check_border(self, move, sensor_type):
        match sensor_type:
            case "top":
                while(True):
                    if self.ultrasonic_top.distance > 0.1:
                        move.terminate()
                        move.join() 
                        return

            case "bottom":
                while(True):
                    if self.ultrasonic_bottom.distance > 0.1:
                        move.terminate()
                        move.join() 
                        return    

            case "left":
                while(True):
                    if self.ultrasonic_left.distance > 0.1:
                        move.terminate()
                        move.join() 
                        return

            case "right":
                while(True):
                    if self.ultrasonic_right.distance > 0.1:
                        move.terminate()
                        move.join() 
                        return

            case "all":
                while(True):
                    if  (self.ultrasonic_bottom.distance > 0.1)  or (self.ultrasonic_left.distance > 0.1) or (self.ultrasonic_right.distance > 0.1):
                        self.hbridge.enable(False)
                        move.terminate()
                        move.join() 
                        return

            case default:
                print("Not available")

    def reference(self):
        move = multiprocessing.Process(target = move_x)
        move.start()
        self.check_border(move)        

        move = multiprocessing.Process(target = move_y)
        move.start()
        self.check_border(move) 

    def start_check_border(self, sensor_type: string):
        move = multiprocessing.Process(target = move_x)
        move.start()
        self.check_border(move, sensor_type)
        
    def route_1(self):
        while(self.ultrasonic_right < 0.1):

            if(self.ultrasonic_top.distance > 0.1):
                self.stepmotor.move_y(self.panel_height)
                self.start_check_border()
                self.stepmotor.move_x(self.brush_length)
                self.start_check_border()  

            elif(self.ultrasonic_bottom.distance > 0.1):
                self.stepmotor.move_y(-self.panel_height)
                self.start_check_border()
                self.stepmotor.move_x(self.brush_length)
                self.start_check_border()

        if(self.ultrasonic_top.distance > 0.1):
                self.stepmotor.move_y(self.panel_height)
                return
        
        elif (self.ultrasonic_bottom.distance > 0.1):
                self.stepmotor.move_y(-self.panel_height)
                return

    def route_2(self):
        progress = 0
        self.stepmotor.move_y(self.panel_height)
        self.stepmotor.move_y(-self.panel_height)
        self.stepmotor.move_x(self.panel_height)
        self.progress = progress + self.brush_length

        while(self.ultrasonic_right < 0.1):
            if(self.ultrasonic_left < 0.1):
                if(self.ultrasonic_top.distance > 0.1):
                    self.stepmotor.move_y(self.panel_height)
                    self.start_check_border()
                    self.stepmotor.move_x(-progress)
                    self.self.start_check_border()
                    progress = progress + self.brush_length

            if(self.ultrasonic_left > 0.1): 
                if(self.ultrasonic_bottom.distance > 0.1):
                    self.stepmotor.move_y(-self.panel_height)
                    self.start_check_border()
                    self.stepmotor.move_x(progress)
                    self.start_check_border() 

        if(self.ultrasonic_top.distance > 0.1):
                    self.stepmotor.move_y(self.panel_height)
                    self.start_check_border()
                    self.stepmotor.move_x(-progress)
                    self.start_check_border()  
                    self.stepmotor.move_y(-self.panel_height)
                    self.stepmotor.move_y(self.panel_height)
                    return

    def route_3(self):
        self.stepmotor.move_x(self.panel_height):

    def route_4():
        stepmotor.move_x(self.panel_height):