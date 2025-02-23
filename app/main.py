import os
from flask import Flask, request, jsonify
import socket
import os
import time

app=Flask(__name__)
app.config['DEBUG'] = True

start_time = time.time()

@app.route('/')
def home():
    return f"Running on {socket.gethostname()}"

@app.route('/info')
def info():
    return jsonify({
        "hostname": socket.gethostname(),
        "uptime": time.time() - start_time,
        "env": dict(os.environ)
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)