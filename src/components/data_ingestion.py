# It is done to read the data from a data source might be a local, cloud or database, or API

import os
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd

from sklearn.model_selection import train_test_split
from dataclasses import dataclass     # Used to create class variables

# This class is basically create for inputs
@dataclass
class DataIngestionConfig:
    train_data_path: str=os.path.join('artifacts',"train.csv")  #the train.csv file containing all the training data will be saved in this artifacts folder
    test_data_path: str=os.path.join('artifacts',"test.csv") # The test data
    raw_data_path: str=os.path.join('artifacts',"data.csv") # The raw data


class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()  # The three paths will get saved into this variable

    def initiate_data_ingestion(self):  #This class is used to read the data if it is stored in some databases like mongoDB etc.,
        logging.info("Entered the data ingestion method or component")
        try:
            df = pd.read_csv('Notebook\data\stud.csv')
            logging.info('Read the dataset as dataframe')

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True)  # creating a directory for artifacts folder and 

            df.to_csv(self.ingestion_config.raw_data_path, index =False, header=True)  # The raw data path is saved in the artifacts folder

            logging.info("Train test split initiated")
            train_set,test_set = train_test_split(df,test_size=0.2,random_state=42)

            train_set.to_csv(self.ingestion_config.train_data_path, index =False, header=True) # The training set data is saved in the artifacts folder
            test_set.to_csv(self.ingestion_config.test_data_path, index =False, header=True) # The test set data is saved in the artifacts folder

            logging.info('Ingestion of the data is completed')

            # This is returned as these paths will be required in the data transformation process
            return(    
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )
        except Exception as e:
            raise CustomException(e,sys)
        

if __name__== '__main__':
    obj = DataIngestion()
    obj.initiate_data_ingestion()