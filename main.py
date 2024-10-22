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
        files = walk_directory(request.get_json().get("path"))
        print(files)
        return jsonify(files)
def walk_directory(directory_name):
    typingdir = []
    typingfile = []
    # Получаем список всех объектов в указанной директории
    for entry in os.listdir(directory_name):
        fullpathname = os.path.join(directory_name, entry)
        if os.path.isdir(fullpathname):
            typingdir.append({"path": entry, "isDir": True, "isFile": False})
        else:
            typingfile.append({"path": entry, "isDir": False, "isFile": True})
    return typingdir + typingfile


if __name__ == '__main__':
    app.run(port=5333, debug="FLASK_DEBUG" in os.environ)
