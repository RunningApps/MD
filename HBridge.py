import time
import SimulRPi.GPIO as GPIO

# Pin-Definitionen für Motor X
PIN_STEP_MX = 1
PIN_ENABLE_MX = 2
PIN_SLEEP_MX = 3
PIN_RESET_MX = 4
PIN_DIR_MX = 5
PIN_M0_MX = 6
PIN_M1_MX = 7
PIN_M2_MX = 8

# Pin-Definitionen für Motor Y
PIN_STEP_MY = 10
PIN_ENABLE_MY = 11
PIN_SLEEP_MY = 12
PIN_RESET_MY = 13
PIN_DIR_MY = 14
PIN_M0_MY = 15
PIN_M1_MY = 16
PIN_M2_MY = 17

class HBridge:
    def __init__(self, pwm_pin, pin_step, pin_enable, pin_sleep, pin_reset, pin_dir, pin_m0, pin_m1, pin_m2):
        self.PIN_STEP = pin_step
        self.PIN_ENABLE = pin_enable
        self.PIN_SLEEP = pin_sleep
        self.PIN_RESET = pin_reset
        self.PIN_DIR = pin_dir
        self.PIN_M0 = pin_m0
        self.PIN_M1 = pin_m1
        self.PIN_M2 = pin_m2

        self.reset()
        self.enable(False)
        self.sleep(True)
        self.direction(True)
        self.pwm_pin = pwm_pin
        GPIO.setup(self.pwm_pin, GPIO.OUT)
        self.pwm = GPIO.PWM(self.pwm_pin, 1000)  # 1000 Hz Frequenz, du kannst die Frequenz anpassen
        self.pwm.start(0)  # Starte PWM mit einem Duty Cycle von 0

    def step_x(self, steps, frequency):
        for i in range(steps):
            period = 1/frequency
            ton = period/2
            toff = ton

            GPIO.output(True, PIN_STEP_MX)
            time.delay(ton)
            GPIO.output(False, PIN_STEP_MX)
            time.elay(toff)

    def step_y(self, steps, frequency):
        for i in range(steps):
            period = 1/frequency
            ton = period/2
            toff = ton

            GPIO.output(True, PIN_STEP_MX)
            time.delay(ton)
            GPIO.output(False, PIN_STEP_MX)
            time.delay(toff)
            

    def direction_stepX(dir: bool):
        GPIO.output(dir, PIN_DIR_MX) # False: Clockwise, True: Counter Clockwise


    def active_driver(self):
        # Ansteuerung des GPIOS
        # GPIO.output(motor_pin, GPIO.HIGH)
        pass