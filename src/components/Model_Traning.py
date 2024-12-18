import os
from src.logging import logging
from src.constant import traning_pipline
from src.entity.config_entity import ModelTrainingConfig
from src.entity.artifacts_entity import (
    DataIngestionArtifact,
    ModelTrainingArtifact
)
from ultralytics import YOLO

class ModelTraining:
    def __init__(self, data_ingestion_artifact: DataIngestionArtifact,
                 model_training_config: ModelTrainingConfig):
        self.model_training_config = model_training_config
        self.data_ingestion_artifact = data_ingestion_artifact

    def initiate_model_training(self):
        try:
            # Extract dataset path from artifacts
            dataset_path = self.data_ingestion_artifact.unzip_data_path
            if not os.path.exists(dataset_path):
                raise FileNotFoundError(f"Dataset path {dataset_path} does not exist.")
            logging.info(f"Dataset found at {dataset_path}")

            # Extract number of classes from config
            num_classes = self.model_training_config.num_classes
            logging.info(f"Number of classes in dataset: {num_classes}")

            # Load the YOLO model with pretrained weights
            logging.info("Loading YOLO model with pretrained weights.")
            model = YOLO(self.model_training_config.pretrained_weights_file_path)
            logging.info("Model loaded successfully.")

            # Check if training directory exists and create it if not
            training_dir = self.model_training_config.dataset_path
            if not os.path.exists(training_dir):
                raise FileNotFoundError(f"Training directory {training_dir} not found.")
            logging.info(f"Training data directory found at {training_dir}")

            # Start model training
            logging.info("Starting model training.")
            model.train(
                data=training_dir,
                epochs=self.model_training_config.model_training_epochs,
                batch=self.model_training_config.model_training_batch_size
            )
            logging.info("Model training completed successfully.")

            # Ensure the directory for saving the model exists
            trained_model_dir = os.path.dirname(self.model_training_config.trained_model_path)
            os.makedirs(trained_model_dir, exist_ok=True)

            # Save the trained model
            logging.info("Saving trained model.")
            model.save(self.model_training_config.trained_model_path)
            logging.info(f"Trained model saved at: {self.model_training_config.trained_model_path}")

            # Create and return ModelTrainingArtifact
            model_training_artifact = ModelTrainingArtifact(
                trained_model_path=self.model_training_config.trained_model_path,
                training_logs_path=self.model_training_config.training_logs_path
            )
            logging.info("ModelTrainingArtifact created successfully.")
            return model_training_artifact

        
        except Exception as e:
            logging.error(f"An unexpected error occurred during model training: {e}")
            print(f"An unexpected error occurred during model training: {e}")
