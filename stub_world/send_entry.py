#
# A framework for messaging between programs
#  and visualising the signaling
#

import zmq
import time
import random
import sys

from send_sequence import Stub

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
   msg = 'data'


a_stub = EmptyStub(name=a)
b_stub = EmptyStub(name=b)


a_stub.send_to(b_stub,msg)

