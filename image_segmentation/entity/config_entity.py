import os
from dataclasses import dataclass
from image_segmentation.constant.training_pipeline import *

@dataclass
class PipelineConfig:
    artifacts_dir: str = ARTIFACTS_DIR

pipeline_config = PipelineConfig()

@dataclass
class IngestionConfig:
    dir: str = os.path.join(pipeline_config.artifacts_dir, INGESTION_DIR)
    feature_store_path: str = os.path.join(dir, FEATURE_STORE_DIR)
    download_url: str = DOWNLOAD_URL

@dataclass
class ValidationConfig:
    dir: str = os.path.join(pipeline_config.artifacts_dir, VALIDATION_DIR)
    status_file_path: str = os.path.join(dir, STATUS_FILE)
    required_files = VALIDATION_FILES

@dataclass
class TrainerConfig:
    dir: str = os.path.join(pipeline_config.artifacts_dir, TRAINING_DIR)
    pretrained_weight = PRETRAINED_WEIGHT
    epochs = EPOCHS
    batch_size = BATCH_SIZE
