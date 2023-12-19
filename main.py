from teilsysteme import StepMotor as SM
from teilsysteme import Verfahrwege as vw

if __name__ == '__main__':
    #x_move = SM.StepMotor(2, 4, 6)
   # y_move = SM.StepMotor(8, 10, 12)

    #x_move.move(0.02, "Right", 1000)

    v = vw.Verfahrwege()
    v.route_1()
