from dataclasses import dataclass

@dataclass
class IngestionArtifact:
    zip_path: str
    feature_store: str

@dataclass
class ValidationArtifact:
    status: bool

@dataclass
class TrainerArtifact:
    model_path: str
