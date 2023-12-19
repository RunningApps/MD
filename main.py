from teilsysteme import StepMotor as SM

if __name__ == '__main__':
    x_move = SM.StepMotor(2, 4, 6)
    y_move = SM.StepMotor(8, 10, 12)

    x_move.move(5, "Right", 500)