'''
    created on: 14/09/2020
    creator: Carlos A. Silva

    This class provide conection to SQL Server instance

    In class contructor can provide a route with json structure with:

    {
        "servername":yourservername
        "database":database
        "username":user
        "password":password
    }

    In other case the connection start with localhost and generic python user.
    You may create the user in SQL server, in Security -> Logins
'''

import pyodbc
import json

class SQLServerConnect:
    
    servername = ""
    database = ""
    username = ""
    password = ""
    conexion = ""
    cursor = ""
    isError = False

    def __init__(self,route = ""):
        
        if route == "" :
            self.servername = "localhost"
            self.database = "master"
            self.username = "PythonDev"
            self.password = "PythonDev.2020*"
            pass
        else:
            self.__ReadJSONConfig(route)
            pass
        
        try:

            self.conexion = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+self.servername+';DATABASE='+self.database+';UID='+self.username+';PWD='+ self.password)

        except:
            
            print(f'The next error has ocurred: {self.conexion}')
            self.isError = True

        finally:
            
            if self.isError :
                print("Migrar mensajes de error en un futuro!!!")
                pass
            else:
                self.cursor = self.conexion.cursor()
                print(f'Conexión con {self.servername} iniciada exitosamente!')
                pass

        super().__init__()

    def __ReadJSONConfig(self, route):
        
        print(f'File detected!!!!   Try to open file: {route}')
        
        with open(route) as json_file:
            data = json.load(json_file)
            self.servername = data["servername"]
            self.database = data["database"]
            self.username = data["username"]
            self.password = data["password"]
        return

    def simplequery(self, fields = "*", table = "", condition = "1", print = False):
        instruct = """
            select
            {fields}
            from {table}
            where {condition}
        """
        print(instruct)
        # self.cursor.execute()
        return
