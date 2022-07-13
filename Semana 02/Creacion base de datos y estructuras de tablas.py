import mysql.connector
import time
import datetime
import mysql
import pymysql
'''Creación conexión a la base de datos'''
try:
        conexion=mysql.connector.connect(host="localhost",
                                            user="root", passwd="")
        cursor=conexion.cursor()
    	
        print("Conexión correcta")
except (mysql.err.OperationalError, mysql.err.InternalError) as e:
	print("Ocurrió un error al conectar: ", e)

'''Creación a la base de datos'''
try:
	conexion = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             )
	try:
		with conexion.cursor() as cursor:
			#Creamos la base de datos y  la ponemos en funcionamiento
			cursor.execute("CREATE DATABASE IF NOT EXISTS EcomerceBrazil;")
			cursor.execute("USE EcomerceBrazil;")
		conexion.commit()
	finally:
		conexion.close()
except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
	print("Ocurrió un error al conectar: ", e)

'''Creación de estructuras de tablas'''
try:
	conexion = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             db='EcomerceBrazil')
	try:
		with conexion.cursor() as cursor:
			#Creamos las estructuras de las tablas en la base de datos
			TablaCustomer="CREATE TABLE IF NOT EXISTS cliente  (IdCliente VARCHAR(50), Unique_IdCliente Varchar(50), ZipCode INT) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish_ci;"
			cursor.execute(TablaCustomer)
			TablaGeolocation="CREATE TABLE IF NOT EXISTS geolocalizacion  (ZipCode INT, Latitud DOUBLE(13,2), Longitud DOUBLE(13,2), City  VARCHAR(250), State VARCHAR(5)) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish_ci;"
			cursor.execute(TablaGeolocation)
			TablaOrder1="CREATE TABLE IF NOT EXISTS pedido (IdOrder VARCHAR(50), Cantidad  INT, IdProduct  VARCHAR(50), IdVendedor VARCHAR(50), FechalEmbar DATE, Precio DOUBLE, ValorFlete  DOUBLE ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish_ci;"
			cursor.execute(TablaOrder1)
			TablaPago="CREATE TABLE IF NOT EXISTS Pago (IdPago INT, IdOrder VARCHAR(50), IdTPago  INT, TipoPago VARCHAR(30), NCUOTAS INT, VALOR DOUBLE) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish_ci;"
			cursor.execute(TablaPago)
			Tablastatusorder="CREATE TABLE IF NOT EXISTS statusorder (IdStatusOrder INT, IdOrder VARCHAR(50), IdCliente VARCHAR(50), StatusOrder VARCHAR(150), FechaCompra DATE, FechaAprob DATE, FechaEntreTr DATE, FechaEntreCli DATE, FechaEstiEntreg DATE ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish_ci;"
			cursor.execute(Tablastatusorder)
			TablaReview="CREATE TABLE IF NOT EXISTS review (IdReview INT, IdOrder VARCHAR(50), Puntaje INT, TComentario VARCHAR(150), Mensaje VARCHAR(300), FechaCreación DATE, FechaRespuesta DATE) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish_ci;"
			cursor.execute(TablaReview)
			TablaProducto="CREATE TABLE IF NOT EXISTS producto (IdProduct VARCHAR(50), IdCategoria INT, LongNombProd DOUBLE, LongDescProducto DOUBLE, CantFotos INT, PesoG DOUBLE, LongCent DOUBLE, AltoC DOUBLE, AnchoC Double ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish_ci;"
			cursor.execute(TablaProducto)
			TablaVendedor="CREATE TABLE IF NOT EXISTS vendedor (IdVendedor VARCHAR(50), ZipCode INT) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish_ci;"
			cursor.execute(TablaVendedor)
			TablaCategoria="CREATE TABLE IF NOT EXISTS categoria (IdCatergoria INT, Categoria VARCHAR(50), CategIngles VARCHAR(100)) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish_ci;"
			cursor.execute(TablaCategoria)
			TablaTratoC="CREATE TABLE IF NOT EXISTS tratocerrado (IdClientePot VARCHAR(50), IdVendedor VARCHAR(50), IdRepDesarr VARCHAR(50), IdRepVentas VARCHAR(50),FechaCierre DATE, SegmentoLider VARCHAR(40), TipoCliePot VARCHAR(40), PerfilComp VARCHAR(40), TieneEmpresa BOOL, TieneCodBarras BOOL, PromInventario DOUBLE, TipoNegocio VARCHAR(40),TamañoProduct DOUBLE, EvalMensual DOUBLE ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish_ci;"
			cursor.execute(TablaTratoC)
			TablaMarketing="CREATE TABLE IF NOT EXISTS marketing (IdClientePot VARCHAR(50), FechaPrcontacto DATE, IdPagina VARCHAR(50), Origen VARCHAR (40)) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish_ci;"
			cursor.execute(TablaMarketing)
			
		conexion.commit()
	finally:
		conexion.close()
except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
	print("Ocurrió un error al conectar: ", e)

'''Creación de la Función Calendario'''


'''Creación de llaves Primarias y Foraneas'''

