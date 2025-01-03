from dataclasses import dataclass


@dataclass
class DataIngestionArtifact:
    data_zip_file_path:str
    unzip_data_path:str

@dataclass
class DataValidationArtifact:
    status:bool

@dataclass
class ModelTrainingArtifact:
    trained_model_path: str
    training_logs_path: str
   



