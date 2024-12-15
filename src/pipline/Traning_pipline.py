import os,sys
from src.logging import logging
from src.components.Data_Ingestion import DataIngestion
from src.components.Data_Validation import DataValidation
from src.entity.config_entity import DataIngestionConfig,TraningPiplineConfig,DataValidationConfig
from src.entity.artifacts_entity import DataIngestionArtifact,DataValidationArtifact

class TraningPipline:
    def __init__(self):
        self.traning_pipline=TraningPiplineConfig()
        
    def Start_Data_Ingstion(self):
        try:
            logging.info('******************************** Data Ingestion ***********************************')
            data_ingestion_config=DataIngestionConfig(traning_pippline_config=self.traning_pipline)
            data_ingestion=DataIngestion(data_ingestion_config=data_ingestion_config)
            self.data_ingestion_artifacts=data_ingestion.initate_data_ingestion()
            logging.info('******************************** Data Ingestion Completed *******************************')

        except Exception as e:
            logging.info(f'Error in Data Ingestion: {str(e)}')
            raise e
        
    def Start_Data_Validation(self):
        try:
            logging.info('******************************** Data Validation ***********************************')
            data_validation_config=DataValidationConfig(traning_pippline_config=self.traning_pipline)
            data_validation=DataValidation(data_validation_config=data_validation_config,
                                           data_ingestion_artifact=self.data_ingestion_artifacts)
            data_validation_artifacts=data_validation.intiate_data_validation()
            logging.info('******************************** Data Validation Completed *******************************')
        except Exception as e:
            logging.info(f'Error in Data Validation: {str(e)}')
            raise e
    
    def run_pipline(self):
        try:
            logging.info('<================================== Traning Pipline ====================================>')
            self.Start_Data_Ingstion()
            self.Start_Data_Validation()
            logging.info('<================================== Traning Pipline Completed ====================================>')
        except Exception as e:
            logging.info(f'Error in Traning Pipline')
            raise e
        
if __name__=='__main__':
    obj=TraningPipline()
    obj.run_pipline()