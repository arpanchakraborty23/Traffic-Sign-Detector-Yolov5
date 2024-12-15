from datetime import datetime
import os
from src.constant import traning_pipline


class TraningPiplineConfig:
    def __init__(self)->None:
        self.timestamp=datetime.now().strftime("%d_%m_%Y_%H_%M_%S")
        self.artifacts_name=traning_pipline.ARTIFACTS_DIR
        self.artifacts_dir=os.path.join(self.artifacts_name,self.timestamp)


class DataIngestionConfig:
    def __init__(self,traning_pippline_config:TraningPiplineConfig)->None:
        # creating Data ingestion dir inside artifacts dir
        self.data_ingestion_dir:str=os.path.join(
            traning_pippline_config.artifacts_dir,traning_pipline.DATA_INGESTION_DIR_NAME
        ) 
        # zip data location
        self.download_zip_file_path:str=os.path.join(
            self.data_ingestion_dir,traning_pipline.DATA_INGESTION_ZIP_FILE_NAME
        )
        # unzip data path
        self.ingested_data:str=os.path.join(
            self.data_ingestion_dir,traning_pipline.DATA_INGESTION_INGESTED_DATA_DIR
        )

        self.data_source_url:str=traning_pipline.DATA_SOURCE_URL   


