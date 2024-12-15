import os
from src.logging import logging
from src.entity.config_entity import DataValidationConfig
from src.entity.artifacts_entity import DataValidationArtifact,DataIngestionArtifact
from src.components.Data_Ingestion import DataIngestion

class DataValidation:
    def __init__(self,data_validation_config:DataValidationConfig,
                 data_ingestion_artifact:DataIngestionArtifact)->None:
        
        self.data_validation_config=data_validation_config
        self.data_ingestion_artifact=data_ingestion_artifact

    def validate_all_files_exist(self)->bool:
        try:
            validation_status=None

            all_files=os.listdir(self.data_ingestion_artifact.unzip_data_path)

            for file in self.data_validation_config.all_required_files:
                if file not in all_files:
                    validation_status=False
                    
                    with open(self.data_validation_config.status_file_path,'w') as f:
                        f.write(f'validation status: {validation_status}')
                    break
                else:
                    validation_status=True
                    with open(self.data_validation_config.status_file_path,'w') as f:
                        f.write(f'validation status: {validation_status}')

            return validation_status
        except Exception as e:
            print(e)

    def intiate_data_validation(self)->DataValidationArtifact:
        try:
            os.makedirs(self.data_validation_config.data_validation_dir,exist_ok=True)
            status=self.validate_all_files_exist()
            data_validation_artifacts=DataValidationArtifact(
                status=status
            )
            return data_validation_artifacts
            
        except Exception as e:
            logging.error('error in data validation')
            print(e)

