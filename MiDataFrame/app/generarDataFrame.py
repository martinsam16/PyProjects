import pandas as pd
from MiDataFrame.dao.DatosD import DatosD

class generarDataFrame():

    def __init__(self):
        self.datos=  DatosD()


    def desdeMiDB(self,consulta:str):
        self.datos.setQuery(consulta)
        return pd.DataFrame.from_dict(self.datos.accion())

    def desdeUrl(self, url:str):
        import requests
        return pd.DataFrame.from_dict(requests.get(url).json())
