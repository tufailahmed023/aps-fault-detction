import os
from sensor.entity.config_entity import TRANSFORMER_OBJECT_FILE_NAME,MODEL_FILE_NAME,TARGET_ENCODER_OBJECT_FILE_NAME
from glob import glob
from typing import Optional
import os

class ModelResolver:
    
    def __init__(self,model_registry:str = "saved_models",
                transformer_dir_name="transformer",
                target_encoder_dir_name = "target_encoder",
                model_dir_name = "model"):

        self.model_registry=model_registry
        os.makedirs(self.model_registry,exist_ok=True)
        self.transformer_dir_name = transformer_dir_name
        self.target_encoder_dir_name=target_encoder_dir_name
        self.model_dir_name=model_dir_name

    def get_latest_dir_path(self)->Optional[str]:
        """This function will give us the latest folder in the saved model folder if there is None they it 
        will return None """
        try:
            dir_names = os.listdir(self.model_registry)
            if len(dir_names)==0:
                return None
            dir_names = list(map(int,dir_names))
            latest_dir_name = max(dir_names)
            return os.path.join(self.model_registry,f"{latest_dir_name}")
        except Exception as e:
            raise e

    def get_latest_model_path(self):
        """This function will give the latest model folder inside the saved model folder
        """
        try:
            latest_dir = self.get_latest_dir_path()
            if latest_dir is None:
                raise Exception(f"Model is not available")
            return os.path.join(latest_dir,self.model_dir_name,MODEL_FILE_NAME)
        except Exception as e:
            raise e
    
    def get_latest_transformer_path(self):
        """This function will give the latest transformer folder inside the saved model folder
        """
        try:
            latest_dir = self.get_latest_dir_path()
            if latest_dir is None:
                raise Exception(f"Transformer is not available")
            return os.path.join(latest_dir,self.transformer_dir_name,TRANSFORMER_OBJECT_FILE_NAME)
        except Exception as e:
            raise e
    
    def get_latest_target_encoder_path(self):
        """This function will give the latest target folder inside the saved model folder
        """
        try:
            latest_dir = self.get_latest_dir_path()
            if latest_dir is None:
                raise Exception(f"Target encoder is not available")
            return os.path.join(latest_dir,self.target_encoder_dir_name,TARGET_ENCODER_OBJECT_FILE_NAME)
        except Exception as e:
            raise e
    

    def get_latest_save_dir_path(self)->str:
        """This function will make the folder inside the saved model folder if there is no folder inside the saved folder then it will create one with name 0 
        """
        try:
            latest_dir = self.get_latest_dir_path()
            if latest_dir==None:
                return os.path.join(self.model_registry,f"{0}")
            latest_dir_num = int(os.path.basename(self.get_latest_dir_path()))
            return os.path.join(self.model_registry,f"{latest_dir_num+1}")
        except Exception as e:
            raise 


    def get_latest_save_model_path(self):
        """This function will make the folder inside the newly created folder for to store the model file 
        """
        try:
            latest_dir = self.get_latest_save_dir_path()
            return os.path.join(latest_dir,self.model_dir_name,MODEL_FILE_NAME)
        except Exception as e:
            raise e
    
    def get_latest_save_transformer_path(self):
        """This function will make the folder inside the newly created folder for to store the transformer file 
        """
        try:
            latest_dir = self.get_latest_save_dir_path()
            return os.path.join(latest_dir,self.transformer_dir_name,TRANSFORMER_OBJECT_FILE_NAME)
        except Exception as e:
            raise 

    def get_latest_save_target_encoder_path(self):
        """This function will make the folder inside the newly created folder for to store the target encorder file 
        """
        try:
            latest_dir = self.get_latest_save_dir_path()
            return os.path.join(latest_dir,self.target_encoder_dir_name,TARGET_ENCODER_OBJECT_FILE_NAME)
        except Exception as e:
            raise e