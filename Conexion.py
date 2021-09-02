import mysql.connector

conexion = mysql.connector.connect(user='root', password='root',
                                    host='localhost',
                                    database='pruebapos',
                                    port='3307')
print(conexion)