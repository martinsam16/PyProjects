from MiDataFrame.dao.Conexion import Conexion

conexion = Conexion
class DatosD(conexion):
    def __init__(self):
        self.__sql =''
        self.__cnn = conexion()

    def getCredenciales(self)->str:
        return self.__cnn.getCredenciales()

    def setCredenciales(self,usuario:str,contrasena:str,host:str,baseDeDatos:str)->None:
        self.__cnn.setCredenciales(usuario=usuario,contrasena=contrasena,host=host,baseDeDatos=baseDeDatos)

    def setQuery(self,query:str)->None:
        self.__sql=query

    def getQuery(self)->str:
        return self.__sql

    def accion(self):
        cursor = self.__cnn.conectar()
        cursor.execute(self.__sql)
        if self.getQuery().upper().startswith('SELECT'):
            personas = cursor.fetchall()
        else:
            personas=None

        self.__cnn.desconectar()
        cursor.close()
        return personas

