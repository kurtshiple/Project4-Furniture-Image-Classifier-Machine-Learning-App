# import necessary libraries
from flask import Flask, render_template, jsonify, request, redirect, url_for
from werkzeug.utils import secure_filename
import os

# create instance of Flask app
app = Flask(__name__)

UPLOAD_FOLDER = '/path/to/the/uploads'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
app.config['UPLOAD_FOLDER'] = "./static/img/"

# create route that renders index.html template
@app.route("/")
def home():
    return render_template("index.html")

# @app.route("/input/<img>")
# def input():
#     return render_template("index.html")

@app.route("/upload", methods=['GET','POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        f.save(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(f.filename)))
        return render_template("output.html")
    return render_template("output.html")

    # if request.method == 'POST':
    #     file = request.files['file[]']
    # if file:
    #         filename = secure_filename(file.filename)
    #         file.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
    #         return render_template('output.html')
    # return render_template('output.html')

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

# @app.route("/output")
# def output():
#     return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
