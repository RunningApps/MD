from teilsysteme import StepMotor as SM
<<<<<<< HEAD

if __name__ == '__main__':
    x_move = SM.StepMotor(2, 4, 6)
    y_move = SM.StepMotor(8, 10, 12)

    x_move.move(5, "Right", 500)
=======
from teilsysteme import Verfahrwege as vw

if __name__ == '__main__':
    #x_move = SM.StepMotor(2, 4, 6)
   # y_move = SM.StepMotor(8, 10, 12)

    #x_move.move(0.02, "Right", 1000)

    v = vw.Verfahrwege()
    v.route_1()
>>>>>>> 1b623393ec1d64c888f585d9d8daaa4e7b4c54bc
