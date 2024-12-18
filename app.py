import os
import json
from flask import Flask, request, jsonify, render_template, send_file, Response
from flask_cors import CORS
from ultralytics import YOLO
import cv2
from src.utils.utils import decodeImage, encodeImageIntoBase64, download_json
from src.constant.traning_pipline import MODEL_PATH

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
        self.model = YOLO('Artifacts/model_training/model.pt')  # Load the YOLO model 

clApp = ClientApp()

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
        annotated_frame = results[0].plot()  # Draw predictions on the image

        # Save the annotated image
        cv2.imwrite(clApp.output_filename, annotated_frame)

        # Encode the output image to base64
        encoded_output = encodeImageIntoBase64(clApp.output_filename)

        # Prepare response data
        response_data = {
            "message": "Image processed successfully!",
            "image": encoded_output.decode('utf-8')  # Base64 encoded output image
        }
        

        # Return the result
        return jsonify(response_data), 200

    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"error": "Internal server error"}), 500

@app.route("/download_json", methods=['GET'])
def download_json():
    try:
        json_filename = "./data/output_data.json"
        if os.path.exists(json_filename):
            return send_file(json_filename, as_attachment=True)
        else:
            return jsonify({"error": "No JSON file found"}), 404
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"error": "Internal server error"}), 500

# Live detection route using the webcam
@app.route("/live_detection")
def live_detection():
    def generate():
        cap = cv2.VideoCapture(0)  # Access the webcam (0 for default webcam)

        while True:
            ret, frame = cap.read()
            if not ret:
                break

            # Perform object detection on the frame
            results = clApp.model.predict(source=frame, conf=0.5)
            annotated_frame = results[0].plot()  # Annotate the frame with predictions

            # Convert frame to JPEG for streaming
            _, jpeg = cv2.imencode('.jpg', annotated_frame)
            frame_bytes = jpeg.tobytes()

            # Yield the frame as a part of a multipart HTTP response
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')

        cap.release()

    return Response(generate(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == "__main__":
    app.run(host=APP_HOST, port=APP_PORT)
