from sensor.entity import config_entity
from sensor.components.data_ingestion import DataIngestion
from sensor.components.data_validation import DataValidation
from sensor.entity.artifact_entity import DataIngestionArtifact
from sensor.components.data_transformation import DataTransformation
train = config_entity.TrainingPipelineConfig()

data = config_entity.DataIngestionConfig(train)

print(data.to_dict())
print("start of dataingestion"*10)
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


# import os
# import pandas as pd
# base  =  os.path.join(r"C:\Users\KIIT\Desktop\aps-falut-detction\aps-fault-detction\aps_failure_training_set1.csv")
# pd.read_csv(base)