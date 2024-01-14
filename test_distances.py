import random
import time
from multiprocessing import Process, Queue

def get_test_distance_data(q: Queue):
    while(True):
        l = str()

        for i in range(4):
            l += str(random .gauss(10,5))+";"

        time.sleep(1)
        q.put(l)
        