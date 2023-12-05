import Verfahrwege

def Verfahrweg():
    p1 = multiprocessing.Process(target=task)
    p1.start() 

    check_distance(p1)

    print("Exiting main process...")

if name == "main":
    Verfahrweg()