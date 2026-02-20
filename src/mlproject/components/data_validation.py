import pandas as pd
from mlproject.entity.config_entity import DataValidationConfig



class DataValidation:
    def __init__(self,config:DataValidationConfig):
        self.config = None
        self.config = config


    def validate_all_columns(self) -> bool:
        try:
            validation_status = None

            all_schema = self.config.all_schema.keys()

            data = pd.read_csv(self.config.unzip_data_dir)
            all_cols = list(data.columns)



            for col in all_cols:
                if col not in all_schema:
                    validation_status = False
                    with open(self.config.STATUS_FILE,"w") as f:
                        f.write(f"Column: {col} Validation status: {validation_status}")
                else:
                    validation_status = True
                    with open(self.config.STATUS_FILE,"w") as f:
                        f.write(f"Column: {col} Validation status: {validation_status}")
            return  validation_status
        except Exception as e:
            raise  e
