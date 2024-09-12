from dataclasses import dataclass


@dataclass
class DataIngestionArtifact:
    trained_file_path: str
    test_file_path: str


@dataclass
class DataValidationArtifact:
    pass


@dataclass
class DataTransformationArtifact:
    pass


@dataclass
class ModelTranierArtifact:
    pass


@dataclass
class ModelEvaluationArtifact:
    pass


@dataclass
class ModelPusherArtifact:
    pass
