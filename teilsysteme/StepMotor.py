import HBridge as hb 
import UltraSonic as us

class StepMotor():
    hbridge = hb.HBridge()
    self.circumference = 0.05
    self.stepsize = 1.8  
    self.frequency = 10

    def step_per_revolution(self) -> int: 
        return 360 / self.stepsize

    def amount_of_steps(self, distance:int):
        steps = self.steps_per_revolution() * distance / self.circumference 

    def set_speed_x(speed: int):  
        self.frequency = speed/60

    def set_speed_y(speed: int):  
        self.frequency = speed/60

    def set_direction_x(dir: bool):
        self.hbridge.set_x_direction(True)

    def set_direction_x(dir: bool):
        self.hbridge.set_y_direction(True)

    def move_x(self, distance: int): 
        steps = self.amount_of_steps(distance)
        self.hbridge.pwm_x(steps, self.frequency)

    def move_y(self, distance: int):
        steps = self.amount_of_steps(distance)
        self.hbridge.pwm_y(steps, self.frequency)

    
