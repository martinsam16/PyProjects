from Dataset.dao.Conexion import Conexion


class DatosD(Conexion):
    def __init__(self):
        self.__sql =''

    def setQuery(self,query):
        self.__sql=query

    def getQuery(self):
        return self.__sql

    def accion(self):
        cnn = Conexion()
        cursor = cnn.conectar()
        cursor.execute(self.__sql)
        if self.getQuery().upper().startswith('SELECT'):
            personas = cursor.fetchall()
        else:
            personas=None

        cnn.desconectar()
        cursor.close()
        return personas
