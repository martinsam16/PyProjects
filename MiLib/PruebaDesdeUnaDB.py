from MiLib.MiDataFrame.app.generarDataFrame import generarDataFrame as gdf
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

demo = gdf()
demo.datos.setCredenciales(usuario='root',contrasena='',host='localhost',baseDeDatos='iVentas')
sql = "SELECT VENTA.CODPER_COMVEN AS COMPRADOR, VENTA.CODPER_VENVEN AS VENDEDOR, DAY(FECVEN) AS DIAVENTA, IF(TIPVEN='B',0,1) AS TIPOVENTA FROM VENTA"

df = demo.desdeMiDB(consulta=sql)

#print(df.describe())
#print(df.keys())
##Predecir quien será el próximo comprador xd

#DIAVENTA, TIPOVENTA: 0 = boleta 1: factura, codigoVendedor
datos= df[df.columns[-3:]].values
#codigoComprador
comprador= df[df.columns[-4]].values

datosTrain, datosTest, compradorTrain, compradorTest = train_test_split(datos, comprador)
rl = LogisticRegression()
rl.fit(datosTrain,compradorTrain)

print("Precisión del modelo: "+str(rl.score(datosTest,compradorTest)))

diaVenta = int(input("Ingrese el dia de Venta (1-31) "))
tipoVenta = int(input("Ingrese el tipo de venta, 0: boleta, 1: factura "))
codigoVendedor = int(input("Ingrese el codigo del vendedor "))

nuevo=[[diaVenta,tipoVenta,codigoVendedor]]
print("\nSu siguiente cliente será: "+str(rl.predict(nuevo)))


