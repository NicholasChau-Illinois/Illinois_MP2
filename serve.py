from flask import Flask, request, jsonify
import subprocess
import socket

app = Flask(__name__)

@app.route("/", methods=["POST"])
def stress_cpu():
    subprocess.Popen(["python3", "stress_cpu.py"])
    return "", 200

@app.route("/", methods=["GET"])
def get_ip():
    private_ip = socket.gethostname()
    return jsonify(private_ip), 200

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=80)
