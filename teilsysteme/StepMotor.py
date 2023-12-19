from teilsysteme import HBridge as hb

class StepMotor():
    def __init__(self, pin_pul, pin_dir, pin_enable):
        self.hbridge = hb.HBridge(pin_pul, pin_dir, pin_enable)
        self.circumference = 0.05
        self.stepsize = 1.8  

    def steps_per_revolution(self) -> int: 
        return 360 / self.stepsize

    def amount_of_steps(self, distance:int):
        steps = self.steps_per_revolution() * distance / self.circumference 
        return int(steps)

    def set_speed(self, speed: int) -> float:  
        return speed/60

    def set_direction_clockwise(self) -> None:
        self.hbridge.direction(True)

    def set_direction_anti_clockwise(self) -> None:
        self.hbridge.direction(False)

    def move(self, distance: int, direction: str, speed: int) -> None: 
        match direction:
            case "Right":
                self.set_direction_clockwise()
            
            case "Left":
                self.set_direction_anti_clockwise()

            case _:
                print("Not valid direction")
                return 
            
        steps = self.amount_of_steps(distance)
        frequency = self.set_speed(speed)
        self.hbridge.puls(steps, frequency)