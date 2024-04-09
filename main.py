from flask import Flask, render_template, request, send_from_directory
from tensorflow.keras.applications import ResNet50, InceptionV3, Xception, VGG16, VGG19
from tensorflow.keras.applications import imagenet_utils
from tensorflow.keras.applications.inception_v3 import preprocess_input
from tensorflow.keras.preprocessing.image import img_to_array
import numpy as np
import pandas as pd
from PIL import Image
from io import BytesIO
import os

app = Flask(_name_)
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def home():

    return render_template('index.html')

model = ResNet50(weights="imagenet")

@app.route('/classify', methods=['POST'])
def classify():

    file = request.files['file']
    bytes_data = file.read()

    input_shape = (224, 224)
    preprocess = imagenet_utils.preprocess_input

    image = Image.open(BytesIO(bytes_data))
    image = image.convert("RGB")
    image = image.resize(input_shape)
    image = img_to_array(image)
    image = np.expand_dims(image, axis=0)
    image = preprocess(image)

    preds = model.predict(image)
    predictions = imagenet_utils.decode_predictions(preds)
    _, label, prob = predictions[0][0]

    # Save the image temporarily
    filename = os.path.join(app.config['UPLOAD_FOLDER'], 'image.jpg')
    with open(filename, 'wb') as f:
        f.write(bytes_data)

    return render_template('result.html', label=label, prob=prob*100, predictions=predictions)

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if _name_ == '_main_':
    app.run(debug=True, port=5000)
