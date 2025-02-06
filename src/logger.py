import logging 
import os
from datetime import datetime

LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"  #This is basically the name of the log file  
# datatime.now() it generates the current date and time and .strftime() formats it in the format mentioned in the format inside the bracket()

logs_path = os.path.join(os.getcwd(),"logs",LOG_FILE)    # using this the logs directory will be created with getcwd() meaning current working directory and it will be of name "logs",LOG_FILE
# logs_path is the directory name
os.makedirs(logs_path,exist_ok=True)  # It will create a directory with the path name as logs_path and if it already exists it will return an error

LOG_FILE_PATH = os.path.join(logs_path,LOG_FILE)

logging.basicConfig(
    filename = LOG_FILE_PATH,   #This is the name of the log file
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s", #this is the contents inside the log file
    level = logging.INFO,  #This sets the logging level
)

if __name__ =="__main__":
    logging.info("Logging has started")