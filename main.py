from teilsysteme import Verfahrwege as vw
from teilsysteme import StepMotor as sm
import SimulRPi.GPIO as GPIO

if __name__ == '__main__':
    #x_stepmotor = sm.StepMotor(2, 4, 6)
    #y_stepmotor = sm.StepMotor(8, 10, 12)
   
    #x_stepmotor.move(0.02, "Right", 1000)
    #y_stepmotor.move(0.02, "Left", 1000)

    #print("Exiting main process...")
    #GPIO.cleanup()
    
    vw = vw.Verfahrwege()
    vw.route_1()

    GPIO.cleanup()
