from cnnClassifier import logger
from cnnClassifier.pipeline.Stage_01_Data_Ingestion import DataIngestionTrainingPipeline
from cnnClassifier.pipeline.Stage_02_Pre_Trained_Model import PrepareBaseModelTrainingPpeline
from cnnClassifier.pipeline.Stage_03_Model_Training import ModelTrainingPipeline


# ----------------------------------------IMPORTING___DATA---------------------------------------------#
STAGE_NAME="Data Ingestion stage"

try:
     logger.info(f">>>>>> stage{STAGE_NAME} started<<<<<<")
     obj=DataIngestionTrainingPipeline()
     obj.main()
     logger.info(f">>>>>>> stage {STAGE_NAME} completed <<<<<<<<\n\nx=========x")
except Exception as e:
     logger.exception(e)
     raise e


#----------------------------------------IMPORTING___PRE-TRAINED__MODEL----------------------------------#
STAGE_NAME="Import Pre-Trained Model"

try:
     logger.info(f">>>>>> stage{STAGE_NAME} started<<<<<<")
     obj=PrepareBaseModelTrainingPpeline()
     obj.main()
     logger.info(f">>>>>>> stage {STAGE_NAME} completed <<<<<<<<\n\nx=========x")
except Exception as e:
     logger.exception(e)
     raise e



#------------------------------------------MODEL___TRAINING-----------------------------------------------#
STAGE_NAME="Model Training"

try:
    logger.info(f"*******************")
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = ModelTrainingPipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e
