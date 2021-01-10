from flask import *
from flask_ngrok import run_with_ngrok
import requests
import os


# init Flask app
app = Flask(__name__)
run_with_ngrok(app)


# webpage / index
@app.route('/')
def index():
    return render_template('index.html')

# forward button
@app.route('/forward', methods=['POST'])
def forward_btn():
    print("Sending RPi API request to move forward...")
    requests.get(f"http://{RPI_API}/f")
    return render_template('index.html')

# stop button
@app.route('/stop', methods=['POST'])
def stop_btn():
    print("Sending RPi API request to stop movement...")
    requests.get(f"http://{RPI_API}/s")
    return render_template('index.html')

# left button
@app.route('/left', methods=['POST'])
def left_btn():
    print("Sending RPi API request to move left...")
    requests.get(f"http://{RPI_API}/l")
    return render_template('index.html')

# right button
@app.route('/right', methods=['POST'])
def right_btn():
    print("Sending RPi API request to move right...")
    requests.get(f"http://{RPI_API}/r")
    return render_template('index.html')



# run & get RPi API URL/URI
if __name__ == '__main__':
    print("Please enter URL/URI for RPi API:")
    RPI_API = input()
    app.run()