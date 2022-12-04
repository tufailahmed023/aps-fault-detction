from sensor.entity import config_entiy
from sensor.components.data_ingestion import DataIngestion
from sensor.components.data_validation import DataValidation
from sensor.entity.artifact_entity import DataIngestionArtifact

train = config_entiy.TrainingPipelineConfig()

data = config_entiy.DataIngestionConfig(train)

print(data.to_dict())
print(" Insitation of Dataingestion"*20)
data_ingestion = DataIngestion(data)
data_ingestion.initiate_data_ingestion()
print(" end of Dataingestion"*20)

print("======================"*20)


print("start of datavlidation"*20)

data1 = config_entiy.DataValidationConfig(train)
obj = DataValidation(data1,DataIngestionArtifact(data.feature_store_file_path,data.train_file_path,data.test_file_path))

obj.initiate_data_validation()


# import os
# import pandas as pd
# base  =  os.path.join(r"C:\Users\KIIT\Desktop\aps-falut-detction\aps-fault-detction\aps_failure_training_set1.csv")
# pd.read_csv(base)