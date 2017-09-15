#!/usr/bin/env python
#
#   Hello World client in Python
#   Connects REQ socket to tcp://localhost:5555
#   Sends "Hello" to server, expects "World" back
#

import zmq
import argparse

context = zmq.Context()

parser = argparse.ArgumentParser()
parser.add_argument("--server_addr", required=False, default='localhost', help="address to server")
args = parser.parse_args()

#  Socket to talk to server
print("Connecting to hello world server...")
socket = context.socket(zmq.REQ)
socket.connect("tcp://%s:5555" % args.server_addr)

#  Do 10 requests, waiting each time for a response
for request in range(10):
    print("Sending request %s ..." % request)
    socket.send(b"Hello")

    #  Get the reply.
    message = socket.recv()
    print("Received reply %s [ %s ]" % (request, message))