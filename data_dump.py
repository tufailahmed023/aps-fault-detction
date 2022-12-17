

import pymongo
import pandas as pd
import json
from sensor.config import mongo_client
client = mongo_client
#print(client)

#print(pd.read_csv('aps_failure_training_set1.csv'))
DATABASE_NAME = "aps"
COLLECTION_NAME  = 'sensor'


if __name__ == "__main__":
    df = pd.read_csv('aps_failure_training_set1.csv')
    print(f"Rows and Columns: {df.shape}")

    #Convert to JSON format

    df.reset_index(drop=True,inplace = True)

    json_record = list(json.loads(df.T.to_json()).values())
    
    #Insertion into MongoDB
    client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)