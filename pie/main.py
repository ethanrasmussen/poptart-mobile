from flask import Flask
from flask import *
from flask import request
from flask import Flask
import gpiozero as gz


# motor assignment
FRONT_L_MOTOR = gz.OutputDevice(27)
FRONT_R_MOTOR = gz.OutputDevice(17)

# init Flask app
app = Flask(__name__)


# forward
@app.route('/f', methods=['GET'])
def forward():
    FRONT_L_MOTOR.on()
    FRONT_R_MOTOR.on()
    return True

# stop
@app.route('/s', methods=['GET'])
def stop():
    FRONT_L_MOTOR.off()
    FRONT_R_MOTOR.off()
    return True

# left
@app.route('/l', methods=['GET'])
def left():
    FRONT_L_MOTOR.on()
    FRONT_R_MOTOR.off()
    return True

# right
@app.route('/r', methods=['GET'])
def right():
    FRONT_L_MOTOR.off()
    FRONT_R_MOTOR.on()
    return True


# run app
if __name__ == '__main__':
    app.run(port=80)