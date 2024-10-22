import os
from flask import Flask, jsonify, request
from flask_cors import CORS

import psutil

app = Flask(__name__)
if "FLASK_DEBUG" in os.environ:
    CORS(app)

currentFolder = None

@app.route("/api/getDisk")
def getDisk():
    return jsonify(psutil.disk_partitions())
@app.route("/api/getListDir", methods=["POST"])
def getListDir():
    if request.method == "POST":
        return jsonify(os.listdir(request.get_json().get("path")))

if __name__ == '__main__':
    app.run(port=5333, debug="FLASK_DEBUG" in os.environ)
