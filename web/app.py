# import necessary libraries
from flask import Flask, render_template, jsonify
from werkzeug import secure_filename
import requests
import os

# create instance of Flask app
app = Flask(__name__)

# create route that renders index.html template
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/input/<img>")
def input():
    return render_template("index.html")

# @app.route("/input")
# def upload_file():
#     if request.method =='POST':
#         file = request.files['file[]']
#         if file:
#             filename = secure_filename(file.filename)
#             file.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
#     return render_template('file_upload.html')

@app.route("/output")
def output():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
