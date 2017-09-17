from sequence_logger import SequenceLogger
from threading import Thread

from flask import Flask, render_template, jsonify
import protobuf_examples.basic_pb2 as basic
import json

log = []
app = Flask(__name__)
logger = SequenceLogger(log, [basic])



@app.route('/')
def main():
    return render_template('index.html')


@app.route('/log')
def log():
   return logger.get_sequence_diagram()

@app.route('/data/<int:index>')
def data(index):
   return jsonify(logger.get_payload(index))
   #return json.dumps(logger.get_payload(index), indent=4, sort_keys=False)



if __name__ == '__main__':
   
   thread = Thread(target = logger.start)
   thread.daemon = True
   thread.start()
   app.run()
