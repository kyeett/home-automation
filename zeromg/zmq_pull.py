# Server example
import zmq
import sys

class Server(object):
    def __init__(self):
        ctx = zmq.Context.instance()
        self.socket = ctx.socket(zmq.PULL)
        self.socket.bind("tcp://*:12345")

    def start(self):

    	while True:

    		received_message = self.socket.recv()
    		if received_message == "stop":
    			print("shutting down")
    			sys.exit(1)
    		else:
    			print(received_message)

if __name__ == '__main__':

	s = Server()
	s.start()