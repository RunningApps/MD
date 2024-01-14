from multiprocessing import Process, Queue

class ProcessHandler():
    def __init__(self):
        #super().__init__()
        print("Processhandler initialized...")

    def memory(self) -> Queue:
        return Queue()

    def start_process(self, fnc: str, *args: tuple) -> Process:
        if len(args) == 0:
            args = []
        else:
            args = list(args)

        process = Process(target=fnc, args=args)
        process.start()

        return process

    def terminate_process(self, process: Process) -> None:
        process.terminate()
        process.join() # The join() call ensures that subsequent lines of your code are not called before all the multiprocessing processes are completed.



