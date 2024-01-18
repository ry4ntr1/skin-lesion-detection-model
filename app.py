from image_segmentation.logger import logging
from image_segmentation.exception import CustomException

logging.info("app.py: running")

try:
    1/0
except Exception as e:
    raise CustomException("Error occured",e)