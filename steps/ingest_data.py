import logging
import pandas as pd
from zenml import step

class IngestData:
    def __init__(self, data_path: str):
        self.data_path= data_path

    def get_data(self):
        logging.info(f"Ingesting Data from {self.data_path}")
        return pd.read_csv(self.data_path)
    
@step
def ingest_data(data_path: str )-> pd.DataFrame:
    """
    Ingesting data from the data_path

    Args:
        data_path:
    Returns:
        pd.Dataframe

    """
    try:
        ingest_data_obj = IngestData(data_path)
        df = ingest_data_obj.get_data()
        return df
    except Exception as e:
        logging.error(f"Error Ingesting Data: {str(e)}")
        return None
