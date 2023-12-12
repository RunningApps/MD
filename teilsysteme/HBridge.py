import time
import SimulRPi.GPIO as GPIO

DELAY_SETUP  = 5*10**-6     # Delay time for internal circuitry to stabilize after Wake-Up (Mikrosekunde)

class HBridge():
    def __init__(self, pin_pul, pin_dir, pin_enable, pin_sw5, pin_sw6, pin_sw7, pin_sw8):
        self.PIN_STEP = pin_pul
        self.PIN_DIR = pin_dir
        self.PIN_ENABLE = pin_enable
        self.PIN_SW5 = pin_sw5
        self.PIN_SW6 = pin_sw6
        self.PIN_SW7 = pin_sw7
        self.PIN_SW8 = pin_sw8

        self.init_pins()
        self.enable()
        self.direction(True)
        self.step_size(2)

    def init_pins(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.PIN_STEP, GPIO.OUT)
        GPIO.setup(self.PIN_ENABLE, GPIO.OUT)
        GPIO.setup(self.PIN_SLEEP, GPIO.OUT)
        GPIO.setup(self.PIN_RESET, GPIO.OUT)
        GPIO.setup(self.PIN_DIR, GPIO.OUT)
        GPIO.setup(self.PIN_M0, GPIO.OUT)
        GPIO.setup(self.PIN_M1, GPIO.OUT)
        GPIO.setup(self.PIN_M2, GPIO.OUT)

    def puls(self, steps, frequency):
        for i in range(steps):
            period = 1/frequency
            ton = period/2
            toff = ton

            GPIO.output(True, PIN_PUL)
            time.delay(ton)
            GPIO.output(False, PIN_PUL)
            time.elay(toff)
            
    def direction(dir: bool):
        GPIO.output(dir, PIN_DIR) # False: Clockwise, True: Counter Clockwise
        time.sleep(DELAY_SETUP)

    def turn_off(self):
        GPIO.output(self.PIN_ENABLE, False)
        time.sleep(DELAY_SETUP)

    def turn_on(self)
        GPIO.output(self.PIN_ENABLE, True)
        time.sleep(DELAY_SETUP)

    def step_size(microstep: int):
        match microstep:
            case 2:
                GPIO.output(False, PIN_SW5)
                GPIO.output(True, PIN_SW6)
                GPIO.output(True, PIN_SW7)
                GPIO.output(True, PIN_SW8)
            
            case 4:
                GPIO.output(True, PIN_SW5)
                GPIO.output(False, PIN_SW6)
                GPIO.output(True, PIN_SW7)
                GPIO.output(True, PIN_SW8)

            case 8:
                GPIO.output(False, PIN_SW5)
                GPIO.output(False, PIN_SW6)
                GPIO.output(True, PIN_SW7)
                GPIO.output(True, PIN_SW8)

            case 16:
                GPIO.output(True, PIN_SW5)
                GPIO.output(True, PIN_SW6)
                GPIO.output(False, PIN_SW7)
                GPIO.output(True, PIN_SW8)

            case 32:
                GPIO.output(False, PIN_SW5)
                GPIO.output(True, PIN_SW6)
                GPIO.output(False, PIN_SW7)
                GPIO.output(True, PIN_SW8)

            case 64:
                GPIO.output(True, PIN_SW5)
                GPIO.output(False, PIN_SW6)
                GPIO.output(False, PIN_SW7)
                GPIO.output(True, PIN_SW8)

            case 128:
                GPIO.output(False, PIN_SW5)
                GPIO.output(False, PIN_SW6)
                GPIO.output(False, PIN_SW7)
                GPIO.output(True, PIN_SW8)