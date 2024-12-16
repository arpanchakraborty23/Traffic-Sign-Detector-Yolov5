from flask import Flask, render_template, request, redirect, url_for
import os
import torch
from PIL import Image

# Initialize Flask app
app = Flask(__name__)

# Upload folder
UPLOAD_FOLDER = 'static/uploads/'
RESULT_FOLDER = 'static/results/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['RESULT_FOLDER'] = RESULT_FOLDER

# Load YOLOv5 model
model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)

# Route for object detection
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'image' not in request.files:
            return redirect(url_for('index'))

        file = request.files['image']
        if file.filename == '':
            return redirect(url_for('index'))

        # Save uploaded file
        filename = file.filename
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)

        # Perform object detection
        results = model(filepath)
        results.save(app.config['RESULT_FOLDER'])

        # Extract detected objects and their confidence scores
        detections = results.pandas().xyxy[0]
        detected_objects = detections[['name', 'confidence']].to_dict(orient='records')

        # Get result image path
        result_image_path = os.path.join(app.config['RESULT_FOLDER'], filename)

        return render_template('index.html', uploaded_image=filepath, result_image=result_image_path, detections=detected_objects)

    return render_template('index.html')

if __name__ == '__main__':
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)
    os.makedirs(RESULT_FOLDER, exist_ok=True)
    app.run(debug=True)
