from sequence_logger import SequenceLogger
from threading import Thread

from flask import Flask, render_template
log = []
app = Flask(__name__)
logger = SequenceLogger(log)



@app.route('/')
def main():
    return render_template('index.html')


@app.route('/log')
def log():
   return logger.get_sequence_diagram()

if __name__ == '__main__':
   
   thread = Thread(target = logger.start)
   thread.daemon = True
   thread.start()
   app.run()
