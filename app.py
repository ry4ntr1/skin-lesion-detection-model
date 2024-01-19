from lesion_detection.logger import logging
from lesion_detection.exception import CustomException

logging.info("app.py: running")

try:
    1/0
except Exception as e:
    raise CustomException("Error occured",e)