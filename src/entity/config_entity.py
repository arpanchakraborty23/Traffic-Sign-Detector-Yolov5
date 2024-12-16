from datetime import datetime
import os
from src.constant import traning_pipline


class TraningPiplineConfig:
    def __init__(self)->None:
        self.timestamp=datetime.now().strftime("%d_%m_%Y_%H_%M_%S")
        self.artifacts_name=traning_pipline.ARTIFACTS_DIR
        self.artifacts_dir=os.path.join(self.artifacts_name)


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

class DataValidationConfig:
    def __init__(self,traning_pippline_config:TraningPiplineConfig)->None:

        ## creating data validation dir inside artifacts dir
        self.data_validation_dir:str=os.path.join(
            traning_pippline_config.artifacts_dir,traning_pipline.DATA_VALIDATION_DIR_NAME
        )
        ## creating status file inside data validation dir
        self.status_file_path:str=os.path.join(
            self.data_validation_dir,traning_pipline.DATA_VALIDATION_STATUS_FILE
        )
        ## list of all required files
        self.all_required_files:list[str]=traning_pipline.DATA_VALIDATION_ALL_REQUIRED_FILES


class ModelTrainingConfig:
    def __init__(self, training_pipeline_config: TraningPiplineConfig) -> None:

        # Create model training directory inside artifacts
        self.model_training_dir: str = os.path.join(
            training_pipeline_config.artifacts_dir, traning_pipline.MODEL_TRAINING_DIR_NAME
        )

        # Trained model file path
        self.trained_model_path: str = os.path.join(
            self.model_training_dir, traning_pipline.MODEL_PATH
        )

        # Logs path for training
        self.training_logs_path: str = os.path.join(
            self.model_training_dir, traning_pipline.MODEL_TRAINING_TRAINING_LOGS_NAME
        )

        # Training hyperparameters
        self.model_training_batch_size: int = traning_pipline.MODEL_TRAINING_BATCH_SIZE
        # number of epochs
        self.model_training_epochs: int = traning_pipline.MODEL_TRAINING_EPOCHS

        # Pretrained weights file path
        self.pretrained_weights_file_path: str = traning_pipline.MODEL_TRAINING_PRETRAINED_WEIGHTS

        # Dataset path
        self.dataset_path: str = traning_pipline.DATASET_PATH

        # Number of classes
        self.num_classes: int = traning_pipline.NUM_CLASSES
       
