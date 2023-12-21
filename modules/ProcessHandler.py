from multiprocessing import Process

class ProcessHandler():
    def __init__(self):
        super().__init__()

    def start_process(self, fnc: str, args: list) -> Process:
        dist, dir, speed = args
        process = Process(target=eval(fnc), args=(dist, dir, speed)) 
        process.start()
        return process
        
    def terminate_process(self, process: Process) -> None:
        process.terminate()
        process.join()

    