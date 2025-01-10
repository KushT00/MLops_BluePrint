import logging
from abc import ABC ,  abstractmethod
from typing import Union

import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split # type: ignore

class DataStrategy(ABC):
    """
    Abstract Base Classs Defining strategy for handling data
    """
    @abstractmethod
    def handle_data(self,data: pd.DataFrame)-> Union[pd.DataFrame,pd.Series]:
        pass
    