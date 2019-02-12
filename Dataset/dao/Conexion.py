import pymysql

class Conexion():
    def __init__(self):
        self.__usr = 'root'
        self.__pssw = ''
        self.__db = 'iVentas'
        self.__host = 'localhost'

    def conectar(self):
        self.__cnn = pymysql.connect(self.__host, self.__usr,self.__pssw, self.__db,cursorclass=pymysql.cursors.DictCursor)
        return self.__cnn.cursor()

    def desconectar(self):
        self.__cnn.close()
