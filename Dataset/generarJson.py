
#"""
from Dataset.dao.DatosD import DatosD
import pandas as pd

def generarDeMiDB():
    demo = DatosD()
    demo.setQuery('SELECT * FROM PERSONA')
    return pd.DataFrame.from_dict(demo.accion())

dataset = generarDeMiDB()

print(dataset)
print(dataset.head())
print(dataset.shape)
print(dataset.count())
print(dataset.describe().max())



"""
import requests

for dni in range(72720455,77777777,1):
    pagina = "https://api.reniec.cloud/dni/"+str(dni)
    print(requests.get(pagina).json())
"""