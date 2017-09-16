
import sys
import zmq
import json

class SequenceLogger:
   
   def __init__(self, log):
      self.context = zmq.Context()
      self.socket = self.context.socket(zmq.PULL)
      self.socket.bind("tcp://*:5556")
      self.log = log

   def format_data(self, source, target, payload):

      if payload:
         
         if isinstance(payload, basestring):
            data_string = '%s ->> %s: %s' % (source, target, payload)
         else:
            data_string = '%s ->> %s: %s|url:http://www.google.se' % (source, target, 'DATA_STRUCT')
            

      else:
         data_string = '%s ->> %s' % (source, target)

      return data_string

   def start(self):
      while True:
         received_data = json.loads(self.socket.recv_string())
         print(received_data)
         received_data_as_string = self.format_data(*received_data) 
         print("Received string: " + received_data_as_string)
         self.log.append(received_data_as_string)

   def get_sequence_diagram(self):
      return "\n".join(["sequenceDiagram"] + ["\t" + log_item for log_item in self.log])


   def print_sequence_diagram(self):
      print(self.get_sequence_diagram())


if __name__ == '__main__':
   log = []
   logger = SequenceLogger(log)
   logger.start()
   logger.print_sequence_diagram()
