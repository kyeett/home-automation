
import sys
import zmq

class SequenceLogger:
   
   def __init__(self, log):
      self.context = zmq.Context()
      self.socket = self.context.socket(zmq.PULL)
      self.socket.bind("tcp://*:5556")
      self.log = log

   def start(self):
      while True:
         received_string = self.socket.recv_string()
         print("Received string: " + received_string)
         if "stop logging" in received_string:
            self.log.append(received_string)
            print("shutting down")
            break
         else:
            self.log.append(received_string)

   def get_sequence_diagram(self):
      return "\n".join(["sequenceDiagram"] + ["\t" + log_item for log_item in self.log])


   def print_sequence_diagram(self):
      print(self.get_sequence_diagram())


if __name__ == '__main__':
   log = []
   logger = SequenceLogger(log)
   logger.start()
   logger.print_sequence_diagram()
