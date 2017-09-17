
import sys
import zmq
import json
from protobuf_examples.protobuf_decoder import ProtobufDecoder
from threading import Lock
from google.protobuf.json_format import MessageToJson


class SequenceLogger:
   
   def __init__(self, log, protobuf_modules=None):

      if protobuf_modules == None:
         protobuf_modules = []

      self.context = zmq.Context()
      self.socket = self.context.socket(zmq.PULL)
      self.socket.bind("tcp://*:5556")
      self.log = log
      self.proto_decoder = ProtobufDecoder(protobuf_modules)
      self.lock = Lock()

   def decode_json(self, value):
      try:
         return json.loads(value)
      except ValueError as e:
         return None

   def format_data(self, source, target, payload):

      if payload:
         
         
         decoded_protobuf = self.proto_decoder.deserialize_string(payload)
         decoded_json = self.decode_json(payload)
         
         if decoded_protobuf is not None:
            print('Decoded!')
            data_string = '%s ->> %s: %s (decoded)|url:replace_with_index' % (source, target, decoded_protobuf.__class__.__name__)
            decoded_payload = MessageToJson(decoded_protobuf)

            print(decoded_payload,type(decoded_payload))
         
         elif decoded_json is not None:
            print('Decoded JSON!')
            data_string = '%s ->> %s: %s (decoded)|url:replace_with_index' % (source, target, 'JSON')          
            decoded_payload = payload
#            print(decoded_payload,type(decoded_payload))
#            print(payload,type(payload))

         else:
            print('Not decoded!')
            data_string = '%s ->> %s: %s' % (source, target, payload)
            decoded_payload = payload


      else:
         print('No payload') 
         data_string = '%s ->> %s' % (source, target)
         decoded_payload = None

      return data_string, decoded_payload


   def start(self):
      while True:
         received_data = self.socket.recv()
         received_data = received_data.split('|')

         received_data_as_string, decoded_payload = self.format_data(*received_data) 
         print("Received string: " + received_data_as_string)
   
         with self.lock:
            # Add index as url, only done for complex datastructures
            index = str(len(self.log))
            received_data_as_string = received_data_as_string.replace('replace_with_index', '/data/'+index)

            self.log.append( { 'text': received_data_as_string,
                               'payload': decoded_payload } )  


   def get_sequence_diagram(self):
      return "\n".join(["sequenceDiagram"] + ["\t" + log_item['text'] for log_item in self.log])

   def get_payload(self, index):
      return self.log[index]['payload']

   def print_sequence_diagram(self):
      print(self.get_sequence_diagram())


if __name__ == '__main__':
   log = []
   import protobuf_examples.basic_pb2 as basic
   logger = SequenceLogger(log, [basic])
   logger.start()
   logger.print_sequence_diagram()
