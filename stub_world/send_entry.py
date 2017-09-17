#
# A framework for messaging between programs
#  and visualising the signaling
#

import zmq
import time
import random
import sys

from send_sequence import Stub
from protobuf_examples.protobuf_decoder import ProtobufDecoder
import protobuf_examples.example
import json

# Smallest viable stub
class EmptyStub(Stub): 

   def send_to(self, target, payload):
      self.log_signaling(self.name, target.name, payload)


try:
   a = sys.argv[1]
except IndexError as e:
   a = 'A'

try:
   b = sys.argv[2]
except IndexError as e:
   b = 'B'

try:
   msg = sys.argv[3]
except IndexError as e:

   msg = random.choice([
            #json.dumps({'key':'value'}),                 # Basic dict
            protobuf_examples.example.serialized_object  # Basic protobuf signal 
      ])

   print(protobuf_examples.example.serialized_object)
   print(msg, type(msg))


a_stub = EmptyStub(name=a)
b_stub = EmptyStub(name=b)


a_stub.send_to(b_stub,msg)

