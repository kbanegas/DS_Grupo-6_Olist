import mysql.connector
import time
import datetime
#import mysql
import pymysql
'''Creación conexión a la base de datos y creaciòn de tablas'''
class Creacion_ambiente:
		
	def Coneccion(self):
		try:
				self.conexion=mysql.connector.connect(host="localhost",
													user="root", passwd="")
				cursor=self.conexion.cursor()
				
				print("Conexión correcta")
		except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
			print("Ocurrió un error al conectar: ", e)

	def Creacion_base(self):
	
		try:
			with self.conexion.cursor() as self.cursor:
				#Creamos la base de datos y  la ponemos en funcionamiento
				Tabla="DROP DATABASE IF EXISTS EcomerceBrazil;"
				self.cursor.execute(Tabla)
				self.cursor.execute("CREATE DATABASE IF NOT EXISTS EcomerceBrazil;")
				self.cursor.execute("USE EcomerceBrazil;")
			self.conexion.commit()
		finally:
			#self.conexion.close()
			pass
		
		
	'''Creación a la base de datos'''
	def Creacion_Tablas(self):
		
		try:
			with self.conexion.cursor() as self.cursor:
				#Creamos las estructuras de las tablas en la base de datos
				
				Tabla="DROP TABLE IF EXISTS cliente;"
				self.cursor.execute(Tabla)
				TablaCustomer1="CREATE TABLE IF NOT EXISTS cliente  (IdCliente VARCHAR(50), Unique_IdCliente Varchar(50), ZipCode INT) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish_ci;"
				self.cursor.execute(TablaCustomer1)
				Tabla="DROP TABLE IF EXISTS geolocalizacion;"
				self.cursor.execute(Tabla)
				TablaGeolocation="CREATE TABLE IF NOT EXISTS geolocalizacion  (ZipCode INT, Latitud DOUBLE(13,2), Longitud DOUBLE(13,2), City  VARCHAR(250), State VARCHAR(5)) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish_ci;"
				self.cursor.execute(TablaGeolocation)
				Tabla="DROP TABLE IF EXISTS pedido;"
				self.cursor.execute(Tabla)
				TablaOrder1="CREATE TABLE IF NOT EXISTS pedido (IdOrder VARCHAR(50), Cantidad  INT, IdProduct  VARCHAR(50), IdVendedor VARCHAR(50), FechalEmbar DATE, Precio DOUBLE, ValorFlete  DOUBLE ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish_ci;"
				self.cursor.execute(TablaOrder1)
				Tabla="DROP TABLE IF EXISTS Pago;"
				self.cursor.execute(Tabla)
				TablaPago="CREATE TABLE IF NOT EXISTS Pago (IdPago INT, IdOrder VARCHAR(50), IdTPago  INT, TipoPago VARCHAR(30), NCUOTAS INT, VALOR DOUBLE) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish_ci;"
				self.cursor.execute(TablaPago)
				Tabla="DROP TABLE IF EXISTS statusorder;"
				self.cursor.execute(Tabla)
				Tablastatusorder="CREATE TABLE IF NOT EXISTS statusorder (IdStatusOrder INT, IdOrder VARCHAR(50), IdCliente VARCHAR(50), StatusOrder VARCHAR(150), FechaCompra DATE, FechaAprob DATE, FechaEntreTr DATE, FechaEntreCli DATE, FechaEstiEntreg DATE ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish_ci;"
				self.cursor.execute(Tablastatusorder)
				Tabla="DROP TABLE IF EXISTS review;"
				self.cursor.execute(Tabla)
				TablaReview="CREATE TABLE IF NOT EXISTS review (IdReview INT, IdOrder VARCHAR(50), Puntaje INT, TComentario VARCHAR(150), Mensaje VARCHAR(300), FechaCreación DATE, FechaRespuesta DATE) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish_ci;"
				self.cursor.execute(TablaReview)
				Tabla="DROP TABLE IF EXISTS producto;"
				self.cursor.execute(Tabla)
				TablaProducto="CREATE TABLE IF NOT EXISTS producto (IdProduct VARCHAR(50), IdCategoria INT, LongNombProd DOUBLE, LongDescProducto DOUBLE, CantFotos INT, PesoG DOUBLE, LongCent DOUBLE, AltoC DOUBLE, AnchoC Double ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish_ci;"
				self.cursor.execute(TablaProducto)
				Tabla="DROP TABLE IF EXISTS vendedor;"
				self.cursor.execute(Tabla)
				TablaVendedor="CREATE TABLE IF NOT EXISTS vendedor (IdVendedor VARCHAR(50), ZipCode INT) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish_ci;"
				self.cursor.execute(TablaVendedor)
				Tabla="DROP TABLE IF EXISTS categoria;"
				self.cursor.execute(Tabla)
				TablaCategoria="CREATE TABLE IF NOT EXISTS categoria (IdCategoria INT, Categoria VARCHAR(50), CategIngles VARCHAR(100)) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish_ci;"
				self.cursor.execute(TablaCategoria)
				Tabla="DROP TABLE IF EXISTS  tratocerrado ;"
				self.cursor.execute(Tabla)
				TablaTratoC="CREATE TABLE IF NOT EXISTS tratocerrado (IdClientePot VARCHAR(50), IdVendedor VARCHAR(50), IdRepDesarr VARCHAR(50), IdRepVentas VARCHAR(50),FechaCierre DATE, SegmentoLider VARCHAR(40), TipoCliePot VARCHAR(40), PerfilComp VARCHAR(40), TieneEmpresa BOOL, TieneCodBarras BOOL, PromInventario DOUBLE, TipoNegocio VARCHAR(40),TamañoProduct DOUBLE, EvalMensual DOUBLE ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish_ci;"
				self.cursor.execute(TablaTratoC)
				Tabla="DROP TABLE IF EXISTS  marketing ;"
				self.cursor.execute(Tabla)
				TablaMarketing="CREATE TABLE IF NOT EXISTS marketing (IdClientePot VARCHAR(50), FechaPrcontacto DATE, IdPagina VARCHAR(50), Origen VARCHAR (40)) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish_ci;"
				self.cursor.execute(TablaMarketing)
				
			self.conexion.commit()
		finally:
			self.conexion.close()
		
Database= Creacion_ambiente()
Database.Coneccion()
Database.Creacion_base()
Database.Creacion_Tablas()




