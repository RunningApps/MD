import HBridge as hb 
import UltraSonic as us

class StepMotor():
    hbridge = hb.HBridge()
    circumference = 0.05
    stepsize = 1.8  

    def step_per_revolution(self) -> int: # Berechnet die Anzahl der Schritte um sich 360 Grad zu drehen
        return 360 / self.stepsize

    # Bewegung in X-Richtung
    def move_x(self, distance: int, speed: int, direction: bool): 
        steps = self.steps_per_revolution() * distance / self.circumference 
        frequency = speed/60 

        # Schritte und Frequenz werden dem Schrittmotor übergeben
        self.hbridge.direction_step_x
        self.hbridge.step_x(steps, frequency)

    # Bewegung in Y-Richtung
    def move_y(self, distance: int, speed: int, direction: bool):
        steps = self.steps_per_revolution() * distance / self.circumference
        frequency = speed/60

        self.hbridge.direction_step_y
        self.hbridge.step_y(steps, frequency)

    
