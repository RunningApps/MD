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
        
    def check_border(move, sensor_type):
        match sensor_type:
            case top:
                while(True):
                    if ultrasonic_top.distance > 0.1:
                        move.terminate()
                        move.join() 
                        return

            case bottom:
                while(True):
                    if ultrasonic_bottom.distance > 0.1:
                        move.terminate()
                        move.join() 
                        return    

            case left:
                while(True):
                    if ultrasonic_left.distance > 0.1:
                        move.terminate()
                        move.join() 
                        return

            case right:
                while(True):
                    if ultrasonic_right.distance > 0.1:
                        move.terminate()
                        move.join() 
                        return

            case all:
                case left:
                while(True):
                    if  or (ultrasonic_bottom.distance > 0.1)  or (ultrasonic_left.distance > 0.1) or (ultrasonic_right.distance > 0.1):
                        hbridge.enable(False)
                        move.terminate()
                        move.join() 
                        return

            case default:
                print("Not available")

    def reference():
        move = multiprocessing.Process(target = move_x)
        move.start()
        check_border(move)        

        move = multiprocessing.Process(target = move_y)
        move.start()
        check_border(move) 

    def start_check_border(sensor_type: string):
        move = multiprocessing.Process(target = move_x)
        move.start()
        check_border(move, sensor_type)
        
    def route_1():
        while(ultrasonic_right < 0.1):
            if(ultrasonic_top.distance > 0.1):
                stepmotor.move_y(self.panel_height)
                start_check_border()
                stepmotor.move_x(self.brush_length)
                start_check_border()  
            else if(ultrasonic_bottom.distance > 0.1):
                stepmotor.move_y(-self.panel_height)
                start_check_border()
                stepmotor.move_x(self.brush_length)
                start_check_border()
        if(ultrasonic_top.distance > 0.1):
                stepmotor.move_y(self.panel_height)
                return
        else if(ultrasonic_bottom.distance > 0.1):
                stepmotor.move_y(-self.panel_height)
                return

    def route_2():
        int progress = 0
        stepmotor.move_y(self.panel_height)
        stepmotor.move_y(-self.panel_height)
        stepmotor.move_x(self.panel_height)
        progress = progress + self.brush_length
        while(ultrasonic_right < 0.1):
            if(ultrasonic_left < 0.1):
                if(ultrasonic_top.distance > 0.1):
                    stepmotor.move_y(self.panel_height)
                    start_check_border()
                    stepmotor.move_x(-progess)
                    start_check_border()
                    progress = progress + self.brush_length
            if(ultrasonic_left > 0.1): 
                if(ultrasonic_bottom.distance > 0.1):
                    stepmotor.move_y(-self.panel_height)
                    start_check_border()
                    stepmotor.move_x(progess)
                    start_check_border() 
        if(ultrasonic_top.distance > 0.1):
                    stepmotor.move_y(self.panel_height)
                    start_check_border()
                    stepmotor.move_x(-progess)
                    start_check_border()  
                    stepmotor.move_y(-self.panel_height)
                    stepmotor.move_y(self.panel_height)
                    return

    def route_3():
        stepmotor.move_x(self.panel_height):

    def route_4():
        stepmotor.move_x(self.panel_height):