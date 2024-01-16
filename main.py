from modules import *
from multiprocessing import Process, Queue
import test_distances as test

def get_and_unpack_data(incoming: Queue, outgoing: Queue):
   datastream = DataStream()

   while(True):   # Simulates incoming data from Arduino
      data = incoming.get()
      #print(data)
      unpacked_data = datastream.unpack_arduino_data(data)
      outgoing.put(unpacked_data)
      
if __name__ == '__main__':
   vw = Verfahrwege()
   vw.x_step.move(100,"Left", 120)
''' 
   processhandler = ProcessHandler()
   incoming = processhandler.memory()
   outgoing = processhandler.memory()

   processhandler.start_process(test.get_test_distance_data, incoming)
   processhandler.start_process(get_and_unpack_data, incoming, outgoing)

   while(True):
      print(outgoing.get())
'''



