import os
import json
from flask import Flask, request, jsonify, render_template, send_file
from flask_cors import CORS
from ultralytics import YOLO
import cv2
import base64

# Flask app configuration
APP_HOST = '0.0.0.0'
APP_PORT = 8080

# Ensure the directory exists
os.makedirs('./data', exist_ok=True)

app = Flask(__name__)
CORS(app)

class ClientApp:
    def __init__(self):
        self.input_filename = "./data/inputImage.jpg"
        self.output_filename = "./data/outputImage.jpg"
        self.model = YOLO("Artifacts\\model_training\\model.pt")  # Load the YOLO model 

clApp = ClientApp()

def decodeImage(image_data, file_path):
    try:
        with open(file_path, "wb") as file:
            file.write(base64.b64decode(image_data))
    except Exception as e:
        print(f"Error decoding image: {e}")

def encodeImageIntoBase64(file_path):
    try:
        with open(file_path, "rb") as file:
            return base64.b64encode(file.read())
    except Exception as e:
        print(f"Error encoding image: {e}")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=['POST'])
def predict():
    try:
        # Decode image from request
        image_data = request.json.get('image')
        if not image_data:
            return jsonify({"error": "No image data provided"}), 400

        # Save the input image
        decodeImage(image_data, clApp.input_filename)

        # Perform object detection using YOLO
        results = clApp.model.predict(source=clApp.input_filename, save=False, conf=0.5)

        # Get the annotated image from the results
        annotated_frame = results[0].plot()  # Draw bounding boxes on the image

        # Save the annotated image
        cv2.imwrite(clApp.output_filename, annotated_frame)

        # Extract bounding boxes and labels
        boxes = results[0].boxes.xyxy  # Get bounding boxes in xyxy format
        confidences = results[0].boxes.conf  # Confidence scores
        labels = results[0].names  # Class labels

        # Prepare bounding box data
        bounding_boxes = []
        for i in range(len(boxes)):
            box = boxes[i].tolist()
            confidence = confidences[i].item()
            label = labels[int(results[0].boxes.cls[i].item())]
            bounding_boxes.append({
                "label": label,
                "confidence": confidence,
                "box": box  # [x_min, y_min, x_max, y_max]
            })

        # Encode the output image to base64
        encoded_output = encodeImageIntoBase64(clApp.output_filename)

        # Prepare JSON file data
        bounding_box_data = {
            "message": "Image processed successfully!",
            "image": encoded_output.decode('utf-8'),  # Base64 encoded output image
            "bounding_boxes": bounding_boxes  # List of bounding boxes with labels and confidence
        }

        # Save the bounding box data to a JSON file
        json_filename = "./data/output_data.json"
        with open(json_filename, 'w') as json_file:
            json.dump(bounding_box_data, json_file)

 

        # Return the result with bounding box data in JSON format
        return jsonify(bounding_box_data), 200

    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"error": "Internal server error"}), 500

@app.route("/download_json", methods=['GET'])
def download_json(json_filename):
    try:
        json_filename = "./data/output_data.json"
        if os.path.exists(json_filename):
            return send_file(json_filename, as_attachment=True)
        else:
            return jsonify({"error": "No JSON file found"}), 404
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"error": "Internal server error"}), 500

if __name__ == "__main__":
    app.run(host=APP_HOST, port=APP_PORT)
