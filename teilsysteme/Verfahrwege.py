import teilsysteme.StepMotor as sm
import multiprocess
import HBridge as hb
from multiprocessing import Process
import os

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

    def start_check_border(self, sensor_type: string, m):
        m.start()
        self.check_border(m, sensor_type)
        
    def route_1(self): #Route oben unten
        #while(self.ultrasonic_right < 0.1): #solagne rechter Rand nicht erreicht

         #   if(self.ultrasonic_top.distance > 0.1): #Falls am oberen Rand
                move = multiprocessing.Process(target = move_y, args=(panel_hight,))#bewegung runter
                self.start_check_border("bottom", move)#abbruch bei unterem Rand
                move = multiprocessing.Process(target = move_x, args=(brush_length,))#bewegung nach rechts
                self.start_check_border("right", move) #abbruch am rechten rand  

            elif(self.ultrasonic_bottom.distance > 0.1): #Falls am unteren Rand
                move = multiprocessing.Process(target = move_y, args=(-panel_hight,)) #bewegung nach oben
                self.start_check_border("top", move)#abbruch am oberen rand
                move = multiprocessing.Process(target = move_x, args=(brush_length,))#bewegung
                self.start_check_border("right", move)#abbruch am rechten rand

        if(self.ultrasonic_top.distance > 0.1):#Falls am oberen rechten Rand
                move = multiprocessing.Process(target = move_y, args=(panel_hight,))#bewegung nach unten
                self.start_check_border("bottom", move)#abbruch bei unterem Rand
                return
        
        elif (self.ultrasonic_bottom.distance > 0.1):#Falls am unteren rechten Rand
                move = multiprocessing.Process(target = move_y, args=(-panel_hight,))#bewegung nach oben
                self.start_check_border("top", move)#abbruch am oberen rand
                return

    def route_2(self):
        progress = 0 #Fortschritt des Weges in x Richtung
    
        self.progress = progress + self.brush_length #Fortschritt um Buerstenlaenge addiert

        while(self.ultrasonic_right < 0.1): #solange der rechte Rand NICHT erreicht wurde
            if(self.ultrasonic_left < 0.1): #Falls die Position NICHT am linken Rand ist
                if(self.ultrasonic_top.distance > 0.1): #Falls die Position am oberen Rand ist
                    self.stepmotor.move_y(self.panel_height) #Bewegung nach unten
                    self.start_check_border(bottom) #Abbruch bei untere Rand
                    self.stepmotor.move_x(-progress) #Bewegeung nach links
                    self.self.start_check_border(left) #Abbruch bei linkem Rand 
                    progress = progress + self.brush_length #Fortschritt um Buerstenlaenge erweitert

            if(self.ultrasonic_left > 0.1): #Falls am linken Rand
                if(self.ultrasonic_bottom.distance > 0.1): #Falls am unteren Rand
                    self.stepmotor.move_y(-self.panel_height) #Bewegung nach oben
                    self.start_check_border(top) #Abbruch bei oberer Rand
                    self.stepmotor.move_x(progress) #Bewegung nach rechts
                    self.start_check_border(right) #Abbruch bei rechtem Rand

        if(self.ultrasonic_top.distance > 0.1): #Falls beim oberen Rand
                    self.stepmotor.move_y(self.panel_height) #Bewegung nach unten
                    self.start_check_border(bottom) #Abbruch beim unteren Rand
                    self.stepmotor.move_x(-progress) #Bewegung nach links
                    self.start_check_border(left) #Abbruch beim linken Rand
                    self.stepmotor.move_y(-self.panel_width) #Bewegung nach oben
                    self.stepmotor.move_y(self.panel_width) #Bewegung nach unten
                    return

    def route_3(self):#oben unten 90 grad gedreht
        while(self.ultrasonic_bottom < 0.1): #solagne untere Rand nicht erreicht

            if(self.ultrasonic_left.distance > 0.1): #wenn linker rand 
                self.stepmotor.move_x(self.panel_width)#nach rechts
                self.start_check_border(right)#abbruch rechts
                self.stepmotor.move_y(self.brush_length)# nach unten
                self.start_check_border(bottom) #abbruch unten

            elif(self.ultrasonic_right.distance > 0.1): #wenn rechts
                self.stepmotor.move_x(-self.panel_width) #nach links
                self.start_check_border(left)#abbruch links
                self.stepmotor.move_y(self.brush_length)#bewegung nach unten
                self.start_check_border(bottom)#abbruch unten

        if(self.ultrasonic_left.distance > 0.1):#Falls  links
                self.stepmotor.move_x(self.panel_width)#nach rechts
                return
        
        elif (self.ultrasonic_right.distance > 0.1):#Falls rechts
                self.stepmotor.move_x(-self.panel_width)#nach links
                return

    def route_4(self):
        progress = 0 #Fortschritt des Weges in y Richtung
    
        self.progress = progress + self.brush_length #Fortschritt um Buerstenlaenge addiert

        while(self.ultrasonic_bottom < 0.1):#waehrend noch NICHT unten
            if(self.ultrasonic_top < 0.1): #wenn nicht oben
                if(self.ultrasonic_left.distance > 0.1): #wenn links
                    self.stepmotor.move_x(self.panel_width) #nach rechts
                    self.start_check_border(right) #abbruch rehts
                    self.stepmotor.move_y(-progress) #nach oben
                    self.self.start_check_border(top) # abbruch oben
                    progress = progress + self.brush_length 

            if(self.ultrasonic_top > 0.1): #wenn oben
                if(self.ultrasonic_right.distance > 0.1): #Falls rechts
                    self.stepmotor.move_x(-self.panel_width) #nach links
                    self.start_check_border(left) #Abbruch links
                    self.stepmotor.move_y(progress) #nach unten
                    self.start_check_border(bottom) #Abbruch unten

        if(self.ultrasonic_left.distance > 0.1): #Falls links
                    self.stepmotor.move_x(self.panel_width) #nach rechts
                    self.start_check_border(right) #Abbruch rechts
                    self.stepmotor.move_y(-progress) #Bewegung nach oben
                    self.start_check_border(top) #Abbruch oben
                    self.stepmotor.move_x(-self.panel_width) #Bewegung nach links
                    self.stepmotor.move_x(self.panel_width) #Bewegung nach rechts
                    return