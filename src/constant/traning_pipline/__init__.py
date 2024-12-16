import os
import sys

""" 
Define common constant variable for training pipeline
"""
ARTIFACTS_DIR:str="Artifacts"

NUM_CLASSES:int=10


'''
Data ingestion
'''
DATA_INGESTION_DIR_NAME:str="data_ingestion"

DATA_INGESTION_INGESTED_DATA_DIR:str="ingested"

DATA_INGESTION_ZIP_FILE_NAME:str='datset.zip'

DATA_SOURCE_URL:str='https://github.com/arpanchakraborty23/dataset/raw/refs/heads/main/Preventive%20Traffic%20Sign%20Detector.v11i.yolov5pytorch.zip'


"""Data validation"""

DATA_VALIDATION_DIR_NAME:str="data_validation"

DATA_VALIDATION_STATUS_FILE:str="status.txt"
DATA_VALIDATION_ALL_REQUIRED_FILES:list[str]=["train","test","valid"]   

"""
Model training
"""

MODEL_TRAINING_DIR_NAME:str="model_training"

MODEL_TRAINING_TRAINING_LOGS_NAME:str="training.log"

MODEL_PATH:str="model.pt"


MODEL_TRAINING_EPOCHS:int=1

MODEL_TRAINING_BATCH_SIZE:int=16

MODEL_TRAINING_PRETRAINED_WEIGHTS:str="yolov5s.pt"


DATASET_PATH:str="E:\Traffic-Sign-Detector-Yolov5\Artifacts\data_ingestion\ingested\data.yaml"












