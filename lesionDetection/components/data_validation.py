import os, sys
import shutil
from lesionDetection.logger import logging
from lesionDetection.exception import CustomException
from lesionDetection.entity.config_entity import DataValidationConfig
from lesionDetection.entity.artifacts_entity import DataIngestionArtifact, DataValidationArtifact

class DataValidation:
    def __init__(
        self,
        data_ingestion_artifact: DataIngestionArtifact,
        data_validation_config: DataValidationConfig,
    ):
        try:
            self.data_ingestion_artifact = data_ingestion_artifact
            self.data_validation_config = data_validation_config
        except Exception as e:
            raise CustomException(e, sys)

    def validate_all_files_exist(self) -> bool:
        try:
            all_files = os.listdir(self.data_ingestion_artifact.feature_store_path)
            missing_files = [file for file in self.data_validation_config.required_file_list if file not in all_files]
            
            validation_status = not missing_files
            os.makedirs(self.data_validation_config.data_validation_dir, exist_ok=True)
            with open(self.data_validation_config.valid_status_file_dir, 'w') as f:
                f.write(f"Validation status: {validation_status}")
            
            return validation_status

        except Exception as e:
            raise CustomException(e, sys)

    def initiate_data_validation(self) -> DataValidationArtifact: 
        logging.info("Entered initiate_data_validation method of DataValidation class")
        try:
            status = self.validate_all_files_exist()
            data_validation_artifact = DataValidationArtifact(validation_status=status)

            logging.info("Exited initiate_data_validation method of DataValidation class")
            logging.info(f"Data validation artifact: {data_validation_artifact}")

            if status:
                shutil.copy(self.data_ingestion_artifact.data_zip_file_path, os.getcwd())

            return data_validation_artifact

        except Exception as e:
            raise CustomException(e, sys)
