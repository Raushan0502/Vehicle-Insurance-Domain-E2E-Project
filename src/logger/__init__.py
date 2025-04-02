import logging
import os
from logging.handlers import RotatingFileHandler 
from from_root import from_root
from datetime import datetime

#constants for log configuration
LOG_DIR = 'logs'
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
MAX_LOG_SIZE = 5 *1024*1024 #5MB
BACKUP_COUNT = 5 #keep 5 backup logs

#Construct log file path
log_dir_path = os.path.join(from_root(), LOG_DIR)
os.makedirs(log_dir_path, exist_ok=True)
log_file_path = os.path.join(log_dir_path, LOG_FILE)    

#Configure logging
def configure_logging():
    """
    Configures the logging settings for the application.            "
    """
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    
    # Create a rotating file handler
    #handler = RotatingFileHandler(log_file_path, maxBytes=MAX_LOG_SIZE, backupCount=BACKUP_COUNT)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    #handler.setFormatter(formatter)

    #File handler with rotation
    file_handler = RotatingFileHandler(log_file_path, maxBytes=MAX_LOG_SIZE, backupCount=BACKUP_COUNT)
    file_handler.setFormatter(formatter)    
    file_handler.setLevel(logging.DEBUG)    


    #Console handler
    console_handler = logging.StreamHandler()   
    console_handler.setFormatter(formatter) 
    console_handler.setLevel(logging.INFO)  # Set console log level to INFO 

    # Add the handler to the logger
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)  

#Configure the logger
configure_logging()