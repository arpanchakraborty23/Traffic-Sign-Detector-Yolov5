from dataclasses import dataclass
import os
import requests
from src.logging import logging
from src.entity.config_entity import DataIngestionConfig
from src.entity.artifacts_entity import DataIngestionArtifact
import zipfile

class DataIngestion:
    def __init__(self,data_ingestion_config:DataIngestionConfig):
        self.config=data_ingestion_config

    def download_data(self,dataset_url,zip_data_path):
        try: 
            # download data
            response=requests.get(dataset_url)
            if response.status_code==200:
                logging.info('request response succesfully')
                os.makedirs(os.path.dirname(zip_data_path),exist_ok=True)

                with open(zip_data_path,'wb') as file:
                    file.write(response.content)
                    logging.info('Data downloaded successfully')
            else:
                logging.error('Data Not Founded')

                logging.info(f"Downloaded data from {dataset_url} into file {zip_data_path}")

            

        except Exception as e:
            print(e)
        
    def unzip_data(self,unzip_data_path,zip_data_path):
        try:
            
            os.makedirs(unzip_data_path, exist_ok=True)
            with zipfile.ZipFile(zip_data_path, 'r') as zip_ref:
                zip_ref.extractall(unzip_data_path)
            logging.info(f"Extracting zip file: {zip_data_path} into dir: {unzip_data_path}")


        except Exception as e:
            print(e)

    def initate_data_ingestion(self):
        try:
            data_url=self.config.data_source_url
            unzip_data_path=self.config.ingested_data
            zip_data_path=self.config.download_zip_file_path

            self.download_data(dataset_url=data_url,zip_data_path=zip_data_path)
            logging.info('data download completed')

            self.unzip_data(unzip_data_path=unzip_data_path,zip_data_path=zip_data_path)

            data_ingestion_artifacts=DataIngestionArtifact(
                data_zip_file_path=zip_data_path,
                unzip_data_path=unzip_data_path
            )
            return data_ingestion_artifacts

        except Exception as e:
            logging.error('error in data ingistion')
            print(e)