import pymysql

class Conexion():
    def __init__(self):
        self.__usr = ''
        self.__pssw = ''
        self.__db = ''
        self.__host = ''

    def setCredenciales(self,usuario:str,contrasena:str,host:str,baseDeDatos:str):
        self.__usr=usuario
        self.__pssw=contrasena
        self.__host=host
        self.__db=baseDeDatos

    def getCredenciales(self):
        return str(self.__usr),str(self.__pssw),str(self.__host),str(self.__db)

    def conectar(self):
        self.__cnn = pymysql.connect(self.__host, self.__usr,self.__pssw, self.__db,cursorclass=pymysql.cursors.DictCursor)
        return self.__cnn.cursor()

    def desconectar(self):
        self.__cnn.close()
