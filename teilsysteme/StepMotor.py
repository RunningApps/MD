import HBridge as hb 
import UltraSonic as us

class StepMotor():
    def __init__(self, pin_pul, pin_dir, pin_enable, pin_sw5, pin_sw6, pin_sw7, pin_sw8);
        hbridge = hb.HBridge(pin_pul, pin_dir, pin_enable, pin_sw5, pin_sw6, pin_sw7, pin_sw8)

    def step_per_revolution(self) -> int: 
        return 360 / self.stepsize

    def amount_of_steps(self, distance:int):
        steps = self.steps_per_revolution() * distance / self.circumference 

    def set_speed(speed: int):  
        self.frequency = speed/60

    def set_direction(dir: bool):
        self.hbridge.direction(True)

    def move(self, point: str, distance: int): 
        steps = self.amount_of_steps(distance)
        self.hbridge.puls(steps, self.frequency)

    def