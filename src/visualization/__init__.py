import pandas as pd
from src.exceptions import CustomException


class Visualiser:
    def __init__(self,url:str) -> None:
        try:
            if not isinstance(url,str):
                raise TypeError("Only String Url's are allowed")
        except TypeError as e:
            message = type(e).__name__
            CustomException(message=message).CreateException()
        else:
            self.url = url

    def GetShape(self):
        df = pd.read_csv(self.url)
        return df.shape