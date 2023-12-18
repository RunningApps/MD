import time
import SimulRPi.GPIO as GPIO

DELAY_SETUP  = 5*10**-6     # Delay time for internal circuitry to stabilize after Wake-Up (Mikrosekunde)

class HBridge():
    def __init__(self, pin_pul, pin_dir, pin_enable) -> None:   # Takes corresponding pins for the X or the Y Stepmotor
        self.PIN_PULS = pin_pul
        self.PIN_DIR = pin_dir
        self.PIN_ENABLE = pin_enable

        self.initialize_gpios()        # initializes the pins
        self.turn_off()         # during instantiation the stepper is disabled
        self.direction(True)    # clockwise 

    def initialize_gpios(self) -> None:
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.PIN_PULS, GPIO.OUT)
        GPIO.setup(self.PIN_ENABLE, GPIO.OUT)
        GPIO.setup(self.PIN_DIR, GPIO.OUT)

    def puls(self, steps, frequency) -> None:
        period = 1/frequency
        ton = period/2
        toff = ton
        
        for i in range(steps):
            GPIO.output(self.PIN_PULS, True)
            time.sleep(ton)
            GPIO.output(self.PIN_PULS, False)
            time.sleep(toff)
            
    def direction(self, dir: bool) -> None:
        GPIO.output(self.PIN_DIR, dir) # False: Clockwise, True: Counter Clockwise
        time.sleep(DELAY_SETUP)

    def turn_off(self)-> None:
        GPIO.output(self.PIN_ENABLE, False)
        time.sleep(DELAY_SETUP)

    def turn_on(self)-> None:
        GPIO.output(self.PIN_ENABLE, True)
        time.sleep(DELAY_SETUP)