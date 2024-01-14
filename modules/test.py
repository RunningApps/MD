import multiprocessing

class MyFancyClass(object):
    
    def __init__(self, name):
        self.name = name
    
    def do_something(self):
        proc_name = multiprocessing.current_process().name
        print ('Doing something fancy in %s for %s!' % (proc_name, self.name))


def worker():
    pass

if __name__ == '__main__':
    queue = multiprocessing.Queue()
    aargs = []
    p = multiprocessing.Process(target=worker, args=(aargs))
    p.start()
    

    
def h(*args):
    print(list(args))
