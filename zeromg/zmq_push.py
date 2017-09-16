# Client example
import zmq
import random

class Client(object):
    def __init__(self):
        self.client_id = random.randint(0,100)
        ctx = zmq.Context.instance()
        self.socket = ctx.socket(zmq.PUSH)
        self.socket.connect("tcp://localhost:12345")

    def send_heartbeat(self):
        self.socket.send(str(self.client_id))

    def send_shutdown(self):
    	self.socket.send("stop")


if __name__ == '__main__':
	c = Client()
	c2 = Client()
	c.send_heartbeat()
	c.send_heartbeat()
	c2.send_heartbeat()
	c2.send_heartbeat()

	# Shut down server
	c.send_shutdown()