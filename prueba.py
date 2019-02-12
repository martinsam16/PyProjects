from MiDataFrame.app.generarDataFrame import generarDataFrame as gdf

demo = gdf()
demo.datos.setCredenciales(usuario='root',contrasena='',host='localhost',baseDeDatos='iVentas')

df = demo.desdeMiDB(consulta='SELECT VENTA.*, VENTA_DETALLE.* FROM VENTA_DETALLE INNER JOIN VENTA ON VENTA_DETALLE.VENTA_CODVEN_VENVEN = VENTA.CODVEN')
print(df.describe())
#print(df.head(n=5))
print('(filas, columnas): ',df.shape)