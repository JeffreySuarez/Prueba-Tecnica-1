
# ********************************************************************************-

from pydal import DAL, Field    # Importamos las librerias necesarias


class DataSource:

    db = ""                 # Conector Base de datos

    # Constructor
    def __init__(self, host, user, passw, database, port, tipo_bd):

        # validamos si hay cambio de puerto BD
        if port != "":
            port = ":" + port

        # dal de conexion
        dalConection = user + ":" + passw + "@" + host + port + "/" + database

        # ******************** Conexiones DB *************************************

        # Conector Sqlite
        if tipo_bd == "sqlite":
            self.db = DAL("sqlite://" + database + ".db")

        # Conector Mysql
        elif tipo_bd == "mysql":
            self.db = DAL("mysql://" + dalConection)

        # Conector Postgresql
        elif tipo_bd == "postgres":
            self.db = DAL("postgres://" + dalConection)

        # Conector Sql server
        elif tipo_bd == "sqlserver":
            self.db = DAL("mssql4://" + dalConection)

        # Conector Firebird
        elif tipo_bd == "firebird":
            self.db = DAL("firebird://" + dalConection)

        # Conector Oracle
        elif tipo_bd == "oracle":
            self.db = DAL("oracle://" + dalConection)

        # Conector BD2
        elif tipo_bd == "db2":
            self.db = DAL("db2://" + dalConection)

        # Conector Ingress
        elif tipo_bd == "ingres":
            self.db = DAL("ingres://" + dalConection)

    """
        Otros 
        Sybase	sybase://usuario:contraseña@localhost/nombrebd
        Informix	informix://usuario:contraseña@nombrebd
        Teradata	teradata://DSN=dsn;UID=usuario;PWD=contraseña;DATABASE=nombrebd
        Cubrid	cubrid://usuario:contraseña@localhost/nombrebd
        SAPDB	sapdb://usuario:contraseña@localhost/nombrebd
        IMAP	imap://user:contraseña@server:port
        MongoDB	mongodb://usuario:contraseña@localhost/nombrebd
        
    """

    # funcion para la ejecucion de consultas sql tipo insert, delete, update
    def query(self, sql):
        try:
            self.db.executesql(sql)
            self.db.commit()
            return True
        except:
            return False

    # funcion para la ejecucion de transancciones (multiples consultas sql)
    def transaction(self, list):
        try:
            for l in list:
                self.db.executesql(l)
            self.db.commit()
            return True
        except:
            return False

    # funcion para la ejecucion de consultas sql tipo select (obtener datos)
    def getData(self, sql):
        q = self.db.executesql(sql)
        self.db.commit()
        return q
