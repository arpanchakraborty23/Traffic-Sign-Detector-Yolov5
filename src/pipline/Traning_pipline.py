import os,sys
from src.logging import logging
from src.components.Data_Ingestion import DataIngestion
from src.entity.config_entity import DataIngestionConfig,TraningPiplineConfig
from src.entity.artifacts_entity import DataIngestionArtifact

class TraningPipline:
    def __init__(self):
        self.traning_pipline=TraningPiplineConfig()
        
    def Start_Data_Ingstion(self):
        try:
            logging.info('******************************** Data Ingestion ***********************************')
            data_ingestion_config=DataIngestionConfig(traning_pippline_config=self.traning_pipline)
            data_ingestion=DataIngestion(data_ingestion_config=data_ingestion_config)
            data_ingestion.initate_data_ingestion()
            logging.info('******************************** Data Ingestion Completed *******************************')

        except Exception as e:
            logging.info(f'Error in Data Ingestion: {str(e)}')
            raise e
        
    def run_pipline(self):
        try:
            logging.info('<================================== Traning Pipline ====================================>')
            self.Start_Data_Ingstion()
            logging.info('<================================== Traning Pipline Completed ====================================>')
        except Exception as e:
            logging.info(f'Error in Traning Pipline')
            raise e
        
if __name__=='__main__':
    obj=TraningPipline()
    obj.run_pipline()