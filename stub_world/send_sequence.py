#
# A framework for messaging between programs
# 	and visualising the signaling
#

import zmq
import time
import random
import json

ctx = zmq.Context()


class Stub:

   def __init__(self, name):
      self.name = name
      self.socket = ctx.socket(zmq.PUSH)
      self.socket.connect("tcp://localhost:5556")

   def log_signaling(self, source, target, payload=None):
      log_entry = (source, target, payload)
      self.socket.send_string(json.dumps(log_entry))


class SpaceShip(Stub):

   def send_to_station(self, target, msg):
      self.log_signaling(source=self.name, target=target.name, payload=msg)

      # Send signal
      print("Sending from %s to %s" % (self.name, target.name))


class SpaceStation(Stub):

   def send_to_station(self, target, msg):
      self.log_signaling(source=self.name, target=target.name, payload=msg)

      # Send signal
      print("Sending from %s to %s" % (self.name, target.name))


if __name__ == '__main__':
   

   # Create units
   space_station_1 = SpaceStation(name='Earth Station')
   space_station_2 = SpaceStation(name='Mars Station')
   space_ship_v = SpaceShip(name='Starship Voyager')
   	
   # Start signaling
   while True:

   	msg = random.choice(['Hello Space!', 'Hello Earth', 'Where are you guys?', 'We are at the final fronter', 'We are done, stop!', 'No can do'])

   	source = random.choice([space_station_1, space_station_2, space_ship_v])
   	target = random.choice([space_station_1, space_station_2, space_ship_v])

   	source.send_to_station(target, msg)
   	time.sleep(1)

   #space_station_1.send_to_station(space_station_2, 'Hello Space!')
   #space_station_2.send_to_station(space_station_1, 'Hello Earth')
   #space_station_2.send_to_station(space_ship_v, 'Where are you guys?')
   #space_ship_v.send_to_station(space_station_1, )
   #space_ship_v.send_to_station(space_station_1, 'We are done, stop!')
   #space_station_2.send_to_station(space_ship_v, )
