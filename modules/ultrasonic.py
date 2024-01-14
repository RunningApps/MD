import time
from .datastream import *

class UltraSonic():
    def __init__(self) -> None:
        self.datastream = DataStream()
        #self.distance_up,  self.distance_down,  self.distance_right,  self.distance_left = self.datastream.unpack_arduino_data()

        print("Ultrasonic initialized...")

    def distance_bottom(self):
        time.sleep(5)

        return 100
    
    def distance_top(self):
        return 0.1#self.distance_top
    
    def distance_left(self):
        return 0.1#self.distance_left
    
    def distance_right(self):
        return 0.1#self.distance_right
    
