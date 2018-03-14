"""
Flask: File upload
"""

import os
from flask import Flask, render_template, request, redirect, url_for, flash, send_from_directory
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = "uploads"
ALLOWED_EXTENSIONS = ["txt", "pdf", "png", "jpg", "jpeg", "gif"]

app = Flask(__name__)
app.debug = True
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
app.secret_key = 'some_secret'  # needed for flashing


def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)


@app.route("/upload_file", methods=["POST"])
def upload_file():
    if "file" not in request.files:
        flash("No file part")
        return redirect(url_for("index"))
    file = request.files["file"]
    # if user does not select file, browser also
    # submit a empty part without filename
    if file.filename == "":
        flash("No selected file")
        return redirect(url_for("index"))
    if file and allowed_file(file.filename):
        # "secure" the filename (form input may be forged and filenames can be dangerous)
        filename = secure_filename(file.filename)
        # save the file to the upload folder
        file.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))
        return render_template("success.html", filename=filename)
    else:
        flash("Not allowed file type")
        return redirect(url_for("index"))


@app.route("/")
def index():
    return render_template("form.html")


if __name__ == "__main__":
    app.run()
