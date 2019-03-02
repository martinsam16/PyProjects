from pandas import DataFrame as df
from MiLib.MiDataFrame.dao.DatosD import DatosD

class generarDataFrame():

    def __init__(self):
        self.datos=  DatosD()


    def desdeMiDB(self,consulta:str):
        self.datos.setQuery(consulta)
        return df.from_dict(self.datos.accion())

    def desdeUrl(self, url:str):
        import requests
        return df.from_dict(requests.get(url).json())
