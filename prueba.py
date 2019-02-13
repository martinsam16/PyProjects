from MiDataFrame.app.generarDataFrame import generarDataFrame as gdf
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

demo = gdf()
demo.datos.setCredenciales(usuario='root',contrasena='',host='localhost',baseDeDatos='iVentas')
sql = "SELECT VENTA.CODPER_COMVEN AS COMPRADOR, VENTA.CODPER_VENVEN AS VENDEDOR, DAY(FECVEN) AS DIAVENTA, IF(TIPVEN='B',0,1) AS TIPOVENTA FROM VENTA"

df = demo.desdeMiDB(consulta=sql)

##Predecir quien será el próximo comprador xd

#DIAVENTA, TIPOVENTA: 0 = boleta 1: factura, codigoVendedor
datos= df[df.columns[-3:]].values
#codigoComprador
comprador= df[df.columns[-4]].values

datosTrain, datosTest, compradorTrain, compradorTest = train_test_split(datos, comprador)
rl = LogisticRegression()
rl.fit(datosTrain,compradorTrain)

print(rl.score(datosTest,compradorTest))

nuevo=[[1,1,3]]
print(rl.predict(nuevo))


