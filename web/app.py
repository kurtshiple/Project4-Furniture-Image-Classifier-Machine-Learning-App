# import necessary libraries
from flask import Flask, render_template, jsonify, request, redirect, url_for
from werkzeug.utils import secure_filename
import os

# machine learning dependancies
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
from sklearn.preprocessing import LabelEncoder 
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

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
        # save image to img folder
        f = request.files['file']
        f.save(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(f.filename)))
        filename = f.filename
        
        # get image from img folder
        # model = load_model("testmodel2.h5")
        model = load_model("testmodel_2.h5")
        image_size = (100, 100)
        image_path = os.path.join("./static/img/", filename)
        img = image.load_img(image_path, target_size=image_size)

        # Preprocess image for model prediction
        # This step handles scaling and normalization for VGG19
        x = image.img_to_array(img)
        x = np.expand_dims(x, axis=0)
        
        # x = preprocess_input(x)
        x_ques = x.astype("float32")/255.0
        x_quest = x_ques.reshape(x_ques.shape[0], x_ques.shape[1],x_ques.shape[2],3)
        x_quest.shape
        model.predict(x_quest).round()

        # label_encoder=LabelEncoder()
        # label_encoder.classes_ = np.load('label_encoder.npy')
        # encoded_predictions = model.predict_classes(x_quest)
        # prediction_labels = label_encoder.inverse_transform(encoded_predictions)
        # k=int(prediction_labels[0])

        k = model.predict_classes(x_quest)[0]+1 # COMMENT ME OUT
        dg=pd.read_csv("B_reduced_labels.csv",encoding="utf-8")
        furn_type=dg[dg['label_id']==k]['text_id'].tolist()
        returnstring = f"I think this might be: {furn_type[0]}"
        
        # returnstring = f"I think this might be: {furn_type[0]}"
        # print(f"Predicted Class :  {k}")
        # print(f"Described Class :  {furn_type[0]}")

        return render_template("output.html", displaytext=returnstring, displayimg=image_path )
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
