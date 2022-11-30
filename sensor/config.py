import pymongo
import pandas as pd
import json
import os 
from dataclasses import  dataclass
@dataclass
class EnviromentVariable:
    mongo_db_url = os.getenv("MONGO_DB_URL")

evr_var = EnviromentVariable()
mongo_client = pymongo.MongoClient(evr_var.mongo_db_url)

