# 
# A framework for messaging between programs
# 	and visualising the signaling
#


log = []

class Stub:

	def __init__(self, name):
		self.name = name

	def log_signaling(self, source, target, payload=None):

		if payload:
			log.append('"%s" --> "%s" [label = "%s"]' % (source, target, payload))
		else:
			log.append('"%s" --> "%s"' % (source, target))

		print(source, target, payload)


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

# Create units
space_station_1 = SpaceStation(name='Earth Station')
space_station_2 = SpaceStation(name='Mars Station')
space_ship_v = SpaceShip(name='Starship Voyager')

# Start signaling
space_station_1.send_to_station(space_station_2, 'Hello Space!')
space_station_2.send_to_station(space_station_1, 'Hello Earth')
space_station_2.send_to_station(space_ship_v, 'Where are you guys?')
space_ship_v.send_to_station(space_station_1, 'We are at the final fronter')


print('{')
for line in log:
	print("\t" + line + ";")
print('}')

