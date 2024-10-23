import os
from io import BytesIO

from flask import Flask, jsonify, request, send_from_directory, send_file
from flask_cors import CORS

import psutil
from PIL import Image


app = Flask(__name__)
if "FLASK_DEBUG" in os.environ:
    CORS(app)

currentFolder = None


@app.route("/api/getDisk")
def getDisk():
    return jsonify(psutil.disk_partitions())


@app.route("/api/getListDir", methods=["POST"])
def getListDir():
    global currentFolder
    if request.method == "POST":
        currentFolder = request.get_json().get("path")
        files = walk_directory(currentFolder)
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
            typingfile.append({"path": entry, "isDir": False, "isFile": True, "ext": entry.split(".")[-1]})
    return typingdir + typingfile


@app.route("/api/img/<path:name>")
def getImage(name):
    global currentFolder
    return send_from_directory(currentFolder, name)

@app.route("/api/it/<int:size>/<path:name>")
def getImageThumbian(size, name):
    global currentFolder
    pathToFile = currentFolder+name
    img = Image.open(pathToFile)
    # img.thumbnail((32, 32))
    buffer = BytesIO()
    img.thumbnail((size, size))
    img = img.convert("RGB")
    img.save(buffer, format='jpeg')
    buffer.seek(0)
    return send_file(buffer, mimetype="image/jpeg")

if __name__ == '__main__':
    app.run(port=5333, debug="FLASK_DEBUG" in os.environ)
