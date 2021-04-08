from flask import Flask
import flask
from threading import Thread
app = Flask('')



@app.route('/')
def hello_name():
   return 'Hello'


@app.route("/get/<images>")
def send(images):
    return flask.send_file(f'/app/downloads/{images}')

def run():
    app.run(host='0.0.0.0' , port=8337)

def keep_alive():
    server = Thread(target=run)
    server.start()
