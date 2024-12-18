# Object Detection API with YOLOv5

## Project Summary
This project implements a REST API service for real-time object detection using YOLOv5 (You Only Look Once version 5). The model is trained to detect traffic signs in real-time from images or live webcam feeds.This repository includes the following:

* YOLOv5 model for traffic sign detection
* Docker for containerization
* CI/CD pipeline for automated testing and deployment
* Live Detection for real-time traffic sign detection from a webcam feed
* Data Ingestion, Validation, and Model Training Process

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
  
- **Detection Capabilities**:
  - Bounding box coordinates (x, y, width, height)
  - Confidence scores
  - Object class labels
- **Input Support**:
  - Image uploads (JPEG, PNG)
  - Real-time webcam feed
- **Response Format**: JSON with structured detection results

## Project Structure
```bash
Traffic-Sign-Detector-Yolov5/
├── app.py
├── requirements.txt
├── README.md                   
├── Dockerfile
├── experiments--> expariment.ipynb 
├── .env
├── .gitignore
├── setup.py
├── .github/workflows/main.yml
├── src
│   ├── __init__.py
│   ├── components
│   │   ├── data_ingestion
│   │   ├── data_validation
│   │   ├── model_training
│   │  
│   ├── utils
│   ├── constants
│   ├── config
│   ├── entity
│   ├── logging
│   ├── pipeline
│   ├── traning_pipeline
│  
│   
```

## Requirements

See `requirements.txt` for complete list of dependencies. Key requirements:

- Python 3.8+
- PyTorch >= 1.8.0
- YOLOv5 (via ultralytics)
- OpenCV >= 4.1.1
- Flask
- NumPy >= 1.23.5
- Pillow >= 10.3.0

## RUN CODE
1. Create Env
   ```bash
   conda create -p env python==3.11 -y
   conda activate ./env
   ```

2. Clone the repository:
   ```bash
   git clone https://github.com/arpanchakraborty23/Traffic-Sign-Detector-Yolov5.git
   cd Traffic-Sign-Detector-Yolov5
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Start the server:
   ```bash
   python app.py
   ```

2. API Endpoints:
   - Image Detection: `POST http://localhost:8080`
   - Download Json:    `POST  http://localhost:8080/download_json  `

## Run Web App with Docker
## Set Up the Docker Container
### Build Docker Image
```bash
docker build -t traffic-sign-detector .
```
## Run the Docker Container
```bash 
docker run -p 8080:8080 traffic-sign-detector
```
Once the container is running, you can access the app at http://localhost:8080.


**Response**:

### Contributing
Feel free to fork this repository and submit issues or pull requests with improvements or bug fixes.