import os
import sys

from networksecurity.expection.exception import NetworkSecurityException
from networksecurity.logger.logger import logging

from networksecurity.pipeline.traning_pipeline import TraningPipeline


def start_training():
    try:
        pass
    except Exception as e:
        raise NetworkSecurityException(e, sys)


if __name__ == "__main__":
    start_training()
