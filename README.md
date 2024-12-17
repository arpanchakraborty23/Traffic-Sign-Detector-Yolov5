# Object Detection API with YOLOv5

## Project Summary
This project implements a REST API service for real-time object detection using YOLOv5 (You Only Look Once version 5). The API provides endpoints for both image-based detection and live camera feeds, making it versatile for various applications like surveillance, retail analytics, and automated inspection systems.

## YOLOv5 Model Overview
YOLOv5 is a state-of-the-art object detection model that offers excellent performance and speed:

- **Architecture**: Single-stage detector that processes images in one pass
- **Pre-trained Models**: Comes with various sizes (nano, small, medium, large, extra-large)
- **Performance**: 
  - Speed: 7-160 FPS depending on model size
  - Accuracy: 37.4-56.0 AP50-95 on COCO dataset
- **Supported Objects**: Detects 80 different object classes in default configuration
- **Custom Training**: Supports training on custom datasets

## Features

- **REST API Endpoints**:
  - `/detect`: POST endpoint for image file detection
  - `/live`: GET endpoint for live camera feed detection
- **Detection Capabilities**:
  - Bounding box coordinates (x, y, width, height)
  - Confidence scores
  - Object class labels
- **Input Support**:
  - Image uploads (JPEG, PNG)
  - Real-time webcam feed
- **Response Format**: JSON with structured detection results

## Requirements

See `requirements.txt` for complete list of dependencies. Key requirements:

- Python 3.8+
- PyTorch >= 1.8.0
- YOLOv5 (via ultralytics)
- OpenCV >= 4.1.1
- Flask
- NumPy >= 1.23.5
- Pillow >= 10.3.0

## Installation

1. Clone the repository:
   ```bash
   git clone [repository-url]
   cd [project-directory]
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Start the server:
   ```bash
   python app.py
   ```

2. API Endpoints:
   - Image Detection: `POST http://localhost:5000/detect`
   - Live Camera: `GET http://localhost:5000/live`

## API Documentation

### Project Structure

**Request**:
- Method: POST
- Content-Type: multipart/form-data
- Body: image file

**Response**:

