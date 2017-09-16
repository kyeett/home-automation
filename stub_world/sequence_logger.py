
import sys
import zmq

#  Socket to talk to server
context = zmq.Context()
socket = context.socket(zmq.PULL)
socket.bind("tcp://*:5556")

log = []

while True:
   received_string = socket.recv_string()
   print("Received string: " + received_string)
   if "stop logging" in received_string:
      log.append(received_string)
      print("shutting down")
      break
   else:
      log.append(received_string)


print('sequenceDiagram')
for line in log:
   print("\t" + line)

