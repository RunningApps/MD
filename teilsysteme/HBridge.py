import time
import SimulRPi.GPIO as GPIO

DELAY_SETUP  = 5*10**-6     # Delay time for internal circuitry to stabilize after Wake-Up (Mikrosekunde)

class HBridge():
    def __init__(self, pin_pul, pin_dir, pin_enable):
        self.PIN_PULS = pin_pul
        self.PIN_DIR = pin_dir
        self.PIN_ENABLE = pin_enable

        self.init_pins()
        self.enable()
        self.direction(True)
        self.step_size(2)

    def initialize_gpios(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.PIN_PULS, GPIO.OUT)
        GPIO.setup(self.PIN_ENABLE, GPIO.OUT)
        GPIO.setup(self.PIN_DIR, GPIO.OUT)

    def puls(self, steps, frequency):
        period = 1/frequency
        ton = period/2
        toff = ton
        
        for i in range(steps):
            GPIO.output(True, self.PIN_PULS)
            time.delay(ton)
            GPIO.output(False, self.PIN_PULS)
            time.elay(toff)
            
    def direction(self, dir: bool):
        GPIO.output(dir, self.PIN_DIR) # False: Clockwise, True: Counter Clockwise
        time.sleep(DELAY_SETUP)

    def turn_off(self):
        GPIO.output(self.PIN_ENABLE, False)
        time.sleep(DELAY_SETUP)

    def turn_on(self):
        GPIO.output(self.PIN_ENABLE, True)
        time.sleep(DELAY_SETUP)