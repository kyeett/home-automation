import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--server_addr", required=False, help="address to server")
args = parser.parse_args()

if args.server_addr:
	print args.server_addr