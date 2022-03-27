import os
from flask import Flask, jsonify, abort, render_template, request
from werkzeug.utils import secure_filename
import sys, signal
import db


app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = "/home/mikhail/Programming/Python/web-file-sharing/uploads"


@app.route("/api/upload", methods=["POST", "GET"])
def upload():
    if request.method == "POST":
        if "file" not in request.files:
            return jsonify({"error": "No file in body"}), 400

        file = request.files["file"]

        if file.filename == "":
            return jsonify({"error", "No file in body"}), 400

        if file:
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))

            db.add_file(filename)

            return jsonify({
                "status": "OK - File uploaded",
                "filename": filename
            })

    else:
        result = db.get_files()
        return render_template("upload.html", files=result)



@app.route("/api/uploads", methods=["GET"])
def get_upload():
    return jsonify({"message": "OK"})


def exit_handler(signal, frame):
    db.close_db()
    print("CTRL-C Pressed - QUITTING")
    sys.exit(0)

if __name__ == "__main__":
    # Cleanly exit on CTRL-C
    signal.signal(signal.SIGINT, exit_handler)
    
    db = db.FilesWrapper("files.db")
    app.run(host="127.0.0.1", port=5050)
