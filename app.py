from flask import Flask, request, jsonify, render_template, send_file
from flask_cors import CORS
from ultralytics import YOLO
import os
import cv2
import numpy as np
from werkzeug.utils import secure_filename

# Flask App Configuration
app = Flask(__name__)
CORS(app)

# Paths and Directories
UPLOAD_FOLDER = "uploads"
RESULT_FOLDER = "results"
MODEL_PATH = "yolov8n.pt"  # Lightweight YOLO model
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(RESULT_FOLDER, exist_ok=True)

# Load YOLO Model
MODEL_PATH='E:\Traffic-Sign-Detector-Yolov5\Artifacts\model_training\model.pt'
model = YOLO(MODEL_PATH)


# ===================== UI ROUTES =====================
@app.route("/")
def home():
    """
    Render the home page with an upload form.
    """
    return render_template("index.html")


@app.route("/upload", methods=["POST"])
def upload_image():
    """
    Handle image upload from the user and display detection results.
    """
    try:
        # Check if the image file exists in the request
        if "image" not in request.files:
            return jsonify({"error": "No image file provided."}), 400
        
        file = request.files["image"]
        if file.filename == "":
            return jsonify({"error": "No file selected."}), 400

        # Save the uploaded image
        filename = secure_filename(file.filename)
        input_image_path = os.path.join(UPLOAD_FOLDER, filename)
        file.save(input_image_path)

        # Run object detection
        results = model.predict(input_image_path, save=True)

        # Extract detection results
        detections = []
        for result in results:
            for box in result.boxes:
                detections.append({
                    "class": int(box.cls[0]),       # Class ID
                    "confidence": round(float(box.conf[0]), 2),  # Confidence
                    "bbox": [                       # Bounding box
                        round(float(coord), 2) for coord in box.xyxy[0]
                    ]
                })

        # Find the saved annotated image path (YOLO saves it automatically)
        annotated_image_dir = os.path.join("runs", "detect", "predict")
        annotated_image_path = os.path.join(annotated_image_dir, filename)

        # Move the annotated image to the RESULT_FOLDER
        final_result_path = os.path.join(RESULT_FOLDER, filename)
        os.replace(annotated_image_path, final_result_path)

        # Return results
        return render_template(
            "results.html",
            detections=detections,
            annotated_image=final_result_path
        )

    except Exception as e:
        return jsonify({"error": str(e)}), 500


# ===================== API ROUTES =====================
@app.route("/predict", methods=["POST"])
def predict():
    """
    API endpoint to handle object detection and return JSON results.
    """
    try:
        # Check if image file exists
        if "image" not in request.files:
            return jsonify({"error": "No image file provided."}), 400
        
        file = request.files["image"]
        filename = secure_filename(file.filename)
        input_image_path = os.path.join(UPLOAD_FOLDER, filename)
        file.save(input_image_path)

        # Run YOLO model for object detection
        results = model.predict(input_image_path, save=True)

        # Process results into JSON format
        detections = []
        for result in results:
            for box in result.boxes:
                detections.append({
                    "class": int(box.cls[0]),
                    "confidence": round(float(box.conf[0]), 2),
                    "bbox": [
                        round(float(coord), 2) for coord in box.xyxy[0]
                    ]
                })

        # Find the annotated image path
        annotated_image_dir = os.path.join("runs", "detect", "predict")
        annotated_image_path = os.path.join(annotated_image_dir, filename)

        # Move annotated image to result folder
        final_result_path = os.path.join(RESULT_FOLDER, filename)
        os.replace(annotated_image_path, final_result_path)

        # Return JSON response
        response = {
            "detections": detections,
            "annotated_image": final_result_path
        }
        return jsonify(response)

    except Exception as e:
        return jsonify({"error": str(e)}), 500


# ===================== RUN THE APP =====================
if __name__ == "__main__":
    app.run(debug=True, port=5000)
