import os
import sys

""" 
Define common constant variable for training pipeline
"""
ARTIFACTS_DIR:str="Artifacts"


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




