# Testet die Parallelität von multiprocessing
import multiprocessing
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
            print(f"p2: {i}")
            time.sleep(0.1)

    # Terminate p1
    p1.terminate()
    p1.join()

def Verfahrweg():
    process = multiprocessing.Process(target=move_x)    # Erschafft den Prozess zum Bewegen des Schrittmotors in x-Richtung
    process.start()                                     # Startet den Process move_x
    check_border(process)                               # Diese Funktion läuft parallel zu move_x 

    #args = [ 1]
    #results = multiprocessing.starmap(move_x, args(2))
    print("Exiting main process...")

if __name__ == "__main__":
    Verfahrweg()