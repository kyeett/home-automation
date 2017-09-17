
import sys
import zmq
import json
from protobuf_examples.protobuf_decoder import ProtobufDecoder

class SequenceLogger:
   
   def __init__(self, log, protobuf_modules=None):

      if protobuf_modules == None:
         protobuf_modules = []

      self.context = zmq.Context()
      self.socket = self.context.socket(zmq.PULL)
      self.socket.bind("tcp://*:5556")
      self.log = log
      self.proto_decoder = ProtobufDecoder(protobuf_modules)

   def format_data(self, source, target, payload):

      if payload:
         
         if isinstance(payload, basestring):
            print('Is basestring')
            # Try to decode as protobuf
            decoded = self.proto_decoder.deserialize_string(payload)
            if not (decoded is None):
               print('Decoded!')
               data_string = '%s ->> %s: %s|url:http://www.google.se' % (source, target, 'DECODED_DATA_STRUCT')            
            else:
               print('Not decoded!')
               data_string = '%s ->> %s: %s' % (source, target, payload)
         else:
            print('Is not basestring')
            data_string = '%s ->> %s: %s|url:http://www.google.se' % (source, target, 'DATA_STRUCT')
            

      else:

         print('No payload')
         data_string = '%s ->> %s' % (source, target)

      return data_string

   def start(self):
      while True:
         received_data = self.socket.recv()
         received_data = received_data.split("|")
         received_data_as_string = self.format_data(*received_data) 
         print("Received string: " + received_data_as_string)
         self.log.append(received_data_as_string)

   def get_sequence_diagram(self):
      return "\n".join(["sequenceDiagram"] + ["\t" + log_item for log_item in self.log])


   def print_sequence_diagram(self):
      print(self.get_sequence_diagram())


if __name__ == '__main__':
   log = []
   import protobuf_examples.basic_pb2 as basic
   logger = SequenceLogger(log, [basic])
   logger.start()
   logger.print_sequence_diagram()
