
# Traffic Sign Detector using YOLOv5

## **Overview**
The Traffic Sign Detector is a web application powered by YOLOv5, designed to detect and classify traffic signs from images or live camera feeds. It leverages deep learning techniques for object detection and aims to aid in traffic analysis, autonomous driving, or road safety applications.

---

## **Project Structure**
Below is the recommended directory structure for your project:

```bash
Traffic-Sign-Detector-Yolov5/
├── app.py
├── requirements.txt
├── README.md                   
├── Dockerfile
├── experiments--> expariment.ipynb 
├── env
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
├── templates/index.html   
├── templates.py 
```

---

## **Data Ingestion**
The **data ingestion** pipeline is responsible for loading,and storing datasets for further model building processing.  

### **Steps**:
1. **Dataset Source**:
   - Traffic sign images were sourced from roboflow.
   - Annotations were provided in **pytorch yolov5** format.

2. **Ingestion Process**:
   - The `Data Ingestion.py` script downloads and organizes the dataset into the `Artifacts/data_ingestion/` directory.
   - Example datasets can include:
     - Training dataset (`train/`)
     - Validation dataset (`val/`)
     - Test dataset (`test/`)

3. **Annotation Handling**:
   - Labels and bounding boxes were parsed and converted to YOLO format using the `roboflow` tool.

4. **Script Execution**:
   ```bash
   python src\pipline\Traning_pipline.py
   ```

---

## **Data Validation**
Data validation ensures the all requuired files are present in the dataset used for training and inference.  

### **Key Checks**:
1. **File Format Validation**:
   - Ensures all images are in `.jpg`.
   - Validates annotation files for YOLO compatibility.

2. **Label Accuracy**:
   - Confirms bounding box coordinates are within image dimensions.
   - Checks for missing or misaligned labels.

3. **Script Execution**:
   The `data_validation.py` script performs these checks:
   ```bash
   python src\pipline\Traning_pipline.py
   ```

4. **Output**:
   - Errors are logged in `Artifacts/data_validation/`.
   - A summary of validation results is displayed.

---

## **Model Building**
Model training and evaluation are implemented using **YOLOv5**.

### **Steps**:
1. **Setup YOLOv5**:
   - ultralytics is used for the model building.
     ```bash
     pip install ultralytics
     ```
     - Load pretrain model *yolov5su.pt* from ultralytics.
     ```bash
     model = YOLO('yolov5su.pt')
     ```
     - Load the dataset from the `Artifacts/data_ingestion/` directory.
     ```bash
     model.train(
                data=training_dir,
                epochs=1,
                batch=16
            )
     ```
5. **Output**:
   - The best-trained weights are saved in the `Artifacts/model_training/` directory.
   - The training logs are saved in the `Artifacts/model_training/training.log` directory.

---

## **Web App**
The web application provides an interface for users to upload images and get predictions.

### **Backend**:
- Developed using **Flask**.
- Implements REST APIs for:
  - Uploading images.
  - Running inference with the trained model.
  - Returning detected objects and confidence scores.

### **Frontend**:
- Built with **HTML**, **CSS**.
- Features:
  - An image upload section.
  - Display of detected traffic signs with bounding boxes.

### **Running the App**:
1. **Local Environment**:
   ```bash
   python src/app.py
   ```
   Access the app at `http://127.0.0.1:5000`.

2. **Dockerized Deployment**:
   - Build and run the Docker container:
     ```bash
     docker build -t traffic-sign-detector .
     docker run -p 5000:5000 traffic-sign-detector
     ```

---

## **Key Features**
1. **Customizable YOLOv5 Training**:
   - Easily retrain the model with new traffic sign datasets.

2. **Real-time Detection**:
   - Supports live camera feeds for real-time traffic sign detection.

3. **Scalable Deployment**:
   - Deployable on cloud platforms ..

---

## **Dependencies**
Install dependencies from the `requirements.txt`:
```bash
pip install -r requirements.txt
```

---

## **Conclusion**
This project demonstrates the application of YOLOv5 for object detection in traffic scenarios. The modular structure allows for easy adaptation and retraining on other datasets.

For questions or contributions, feel free to reach out!
