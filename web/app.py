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

# @app.route("/input/<img>")
# def input():
#     return render_template("index.html")

@app.route("/upload/",methods=['GET','POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file[]']
    if file:
            filename = secure_filename(file.filename)
            file.save(os.path.join('../static/img',filename))
            return render_template('output.html')
    return render_template('output.html')
# def upload_file():
#     if request.method =='POST':
#         file = request.files['file']
#         if file:
#             filename = secure_filename(file.filename)
#             file.save(os.path.join('../static/img',filename))
#     return render_template('output.html')

# def contact():
#     if request.method == 'POST':
#         if request.form['submit_button'] == 'Do Something':
#             pass # do something
#         elif request.form['submit_button'] == 'Do Something Else':
#             pass # do something else
#         else:
#             pass # unknown
#     elif request.method == 'GET':
#         return render_template('contact.html', form=form)

@app.route("/output")
def output():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
