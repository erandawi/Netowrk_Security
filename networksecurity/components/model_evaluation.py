from networksecurity.expection.exception import NetworkSecurityException
from networksecurity.logger.logger import logging
import os, sys
from networksecurity.entity.artifact_entity import (
    DataValidationArtifact,
    ModelTrainerArtifact,
    ModelEvaluationArtifact,
)
from networksecurity.entity.config_entity import ModelEvaluationConfig
from networksecurity.utils.ml_utils.metric.classification_metric import (
    get_classification_score,
)
from networksecurity.utils.ml_utils.model.estimator import NetworkModel
from networksecurity.utils.main_utils.utils import (
    save_object,
    load_object,
    write_yaml_file,
)
from networksecurity.utils.ml_utils.model.estimator import ModelResolver
from networksecurity.constant.training_pipeline import TARGET_COLUMN
import pandas as pd


class ModelEvaluation:
    def __init__(
        self,
        model_eval_config: ModelEvaluationConfig,
        data_validation_artifact: DataValidationArtifact,
        model_trainer_artifact: ModelTrainerArtifact,
    ):
        try:
            self.model_eval_config = model_eval_config
            self.data_validation_artifact = (data_validation_artifact,)
            self.model_trainer_artifact = model_trainer_artifact

        except Exception as e:
            raise NetworkSecurityException(e, sys)

    def initiate_model_evaluation(self) -> ModelEvaluationArtifact:
        try:
            valid_train_train_path = self.data_validation_artifact.valid_train_file_path
            valid_test_file_path = self.data_validation_artifact.valid_test_file_path
            
        except Exception as e:
            raise NetworkSecurityException(e, sys)
