from flask import Flask
from flask import *
from flask import request
from flask import Flask
import gpiozero as gz


# motor assignment
left = gz.OutputDevice(27)
right = gz.OutputDevice(17)

# init Flask app
app = Flask(__name__)


# forward
@app.route('/f', methods=['GET'])
def forward():
    left.on()
    right.on()
    return True

# stop
@app.route('/s', methods=['GET'])
def stop():
    left.off()
    right.off()
    return True

# left
@app.route('/l', methods=['GET'])
def left():
    left.on()
    right.off()
    return True

# right
@app.route('/r', methods=['GET'])
def right():
    left.off()
    right.on()
    return True


# run app
if __name__ == '__main__':
    app.run(port=80)