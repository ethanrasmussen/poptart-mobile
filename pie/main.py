from flask import Flask
from flask import *
from flask import request
from flask import Flask
import gpiozero as gz


# motor assignment
L_MOTOR = gz.OutputDevice(27)
R_MOTOR = gz.OutputDevice(17)

# init Flask app
app = Flask(__name__)


# forward
@app.route('/f', methods=['GET'])
def forward():
    L_MOTOR.on()
    R_MOTOR.on()
    return True

# stop
@app.route('/s', methods=['GET'])
def stop():
    L_MOTOR.off()
    R_MOTOR.off()
    return True

# left
@app.route('/l', methods=['GET'])
def left():
    L_MOTOR.on()
    R_MOTOR.off()
    return True

# right
@app.route('/r', methods=['GET'])
def right():
    L_MOTOR.off()
    R_MOTOR.on()
    return True


# run app
if __name__ == '__main__':
    app.run(port=80)