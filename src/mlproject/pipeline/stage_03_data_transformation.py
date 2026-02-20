from mlproject import  logger
from mlproject.components.data_transformation import DataTransformation
from mlproject.config.configuration import ConfigurationManager

STAGE_NAME = "Data Validation stage"

class DataTransformationPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_transformation_config = config.get_data_transformation_config()
        data_transformation = DataTransformation(config=data_transformation_config)
        data_transformation.train_test_split()



if __name__ == "__main__":
    try:
        logger.info(f">>>>>>>> stage {STAGE_NAME} started <<<<<<<<")
        obj = DataTransformationPipeline()
        obj.main()
        logger.info(f">>>>>>>> stage {STAGE_NAME} completed <<<<<<<<")
        print("x" + "="*50 + "x")
    except Exception as e:
        logger.exception(e)
        raise e