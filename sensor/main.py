from sensor.entity import config_entiy
from sensor.components.data_ingestion import DataIngestion
train = config_entiy.TrainingPipelineConfig()

data = config_entiy.DataIngestionConfig(train)

print(data.to_dict())

data_ingestion = DataIngestion(data)
print(data_ingestion.initiate_data_ingestion())

