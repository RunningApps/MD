# Testet die Parallelität von multiprocessing
import multiprocessing
from itertools import product
import time

def move_x():
    i = 1
    while True:
        print(f"p1: {i}")
        i += 1
        time.sleep(0.1)

    print(j)

def check_border(p1):
    for i in range(101):
            if i == 50:
                break
            print(i)
            time.sleep(0.1)

    # Terminate p1
    p1.terminate()
    p1.join()

def Verfahrweg():
    process = multiprocessing.Process(target=move_x) 
    process.start() 

    check_border(process) # Ruft die Funktion check_distance auf

    print("Exiting main process...")

if __name__ == "__main__":
    Verfahrweg()