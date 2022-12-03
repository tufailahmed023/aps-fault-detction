from sensor.entity import artifact_entity
from sensor.entity import config_entiy
from sensor.logger import logging
from sensor.exception import SensorException
import os ,sys
from scipy.stats import ks_2samp
import pandas as pd
from typing import Optional

class DataValidation:
    def __init__(self,data_validation_config:config_entiy.DataValidationConfig):
        try:
            logging.info(f"{'>>'*20} Data Validation {'>>'*20} ")
            self.data_validation_config = data_validation_config
        except Exception as e:
            print(SensorException(e, error_detail= sys))

    def is_required_columns_exists(self,)->bool:...

    

          
