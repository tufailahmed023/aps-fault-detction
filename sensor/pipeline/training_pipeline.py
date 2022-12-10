from sensor.entity import config_entity
from sensor.components.data_ingestion import DataIngestion
from sensor.components.data_validation import DataValidation
from sensor.entity.artifact_entity import DataIngestionArtifact
from sensor.components.data_transformation import DataTransformation
from sensor.components.model_trainer import ModelTrainer
from sensor.components.model_evalutaion import ModelEvaluation
from sensor.entity.config_entity import ModelPusherConfig
from sensor.components.model_pusher import ModelPusher
from sensor.exception import SensorException
import sys,os

def start_training_pipeline():
    try :
        train = config_entity.TrainingPipelineConfig()

        #print(data.to_dict())
        print("=="*20)
        print("=="*20)
        print("=="*20)

        print("start of dataingestion"*10)

        data = config_entity.DataIngestionConfig(train)
        data_ingestion = DataIngestion(data)
        data_ingestion_artifact = data_ingestion.initiate_data_ingestion()

        print("=="*20)
        print("=="*20)
        print("=="*20)

        print("start of datavlidation"*10)

        data1 = config_entity.DataValidationConfig(train)
        obj = DataValidation(data1, data_ingestion_artifact = data_ingestion_artifact)
        data_validation_artifact = obj.initiate_data_validation()

        print("=="*20)
        print("=="*20)
        print("=="*20)

        print("start of datatransformation"*10)

        data2 = config_entity.DataTransformationConfig(train)
        obj_tran =  DataTransformation(data2, data_ingestion_artifact = data_ingestion_artifact)
        data_tansformation_artifact = obj_tran.initiate_data_transformation()

        print("=="*20)
        print("=="*20)
        print("=="*20)

        print("start of modeltraining"*10)

        data3 = config_entity.ModelTrainerConfig(train)
        obj_train = ModelTrainer(data3, data_transformation_artifact = data_tansformation_artifact)
        model_trainer_artifact = obj_train.initiate_model_trainer()

        print("=="*20)
        print("=="*20)
        print("=="*20)

        print("start of modelevaluation"*10)

        data4 = config_entity.ModelEvaluationConfig(train)
        obj_eval = ModelEvaluation(data4, data_ingestion_artifact = data_ingestion_artifact , 
                                data_transformation_artifact = data_tansformation_artifact, 
                                model_trainer_artifact = model_trainer_artifact)
        model_eval_artifact = obj_eval.initiate_model_evaluation()

        print("=="*20)
        print("=="*20)
        print("=="*20)

        print("start of modelpusher"*10)
        data5 = ModelPusherConfig(train)
        obj_pusher = ModelPusher(data5, data_transformation_artifact = data_tansformation_artifact, model_trainer_artifact = model_trainer_artifact)
        model_pusher_artifact = obj_pusher.initiate_model_pusher()
    except Exception as e:
        print(SensorException(e, error_detail = sys))