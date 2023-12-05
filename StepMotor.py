import HBridge as hb 
import UltraSonic as us
import multiprocessing
import time

class StepMotor():
    circumference = 0.05
    stepsize = 1.8
    hbridge = hb.HBridge()
    ultrasonic_top = us.UltraSonic()
    ultrasonic_bottom = us.UltraSonic()
    ultrasonic_left = us.UltraSonic()
    ultrasonic_right = us.UltraSonic()

    def step_per_revolution(self) -> int:
        return 360 / self.stepsize

    def move_x(distance: int):
        steps = self.steps_per_revolution() * distance / self.circumference
        self.hbridge.step(steps)

    def move_y(distance: int):
        steps = self.steps_per_revolution() * distance / self.circumference
        self.hbridge.step(steps)

    
