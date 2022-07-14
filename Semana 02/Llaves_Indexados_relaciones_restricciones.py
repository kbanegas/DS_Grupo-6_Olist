from grpc import Status
import mysql.connector
import time
import datetime
import mysql
import pymysql



def clientes():
	try:
		conexion = pymysql.connect(host='localhost',
								user='root',
								password='',
								db='EcomerceBrazil')
		try:
			with conexion.cursor() as cursor:
				#inicialmente verificamos si las llaves estan generados o no
				Tabla5="Show index from `cliente`;"
				cursor.execute(Tabla5)
				resultados= cursor.fetchall()
				lresultados= list(resultados)
				llave= lresultados[0]
				llave=list(llave)
				Index_exists=False
				name='IdCliente'
				for r in llave:
					if r==name:
						Index_exists=True
				if Index_exists ==True:
					print(" llaves, indexados,relacines y restricciones ya existen")
				else:
				#Creamos  llaves, indexados,relaciones y restricciones para la tabla clientes
					TablaCustomer0="ALTER TABLE `cliente` ADD PRIMARY KEY(`IdCliente`);"
					cursor.execute(TablaCustomer0)
					TablaCustomer1="ALTER TABLE `cliente` ADD INDEX (`Unique_IdCliente`);"
					cursor.execute(TablaCustomer1)
					TablaCustomer2="ALTER TABLE `cliente` ADD INDEX (`ZipCode`);"
					cursor.execute(TablaCustomer2)
					TablaCustomer3="ALTER TABLE statusorder ADD CONSTRAINT `statusorder_fk_cliente` FOREIGN KEY (IdCliente) REFERENCES cliente (IdCliente) ON DELETE RESTRICT ON UPDATE RESTRICT;"
					cursor.execute(TablaCustomer3)					
			conexion.commit()
		finally:
			conexion.close()
	except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
		print("Ocurrió un error al conectar: ", e)
	

def Geolocalizacion():

	try:
		conexion = pymysql.connect(host='localhost',
								user='root',
								password='',
								db='EcomerceBrazil')
		try:
			with conexion.cursor() as cursor:
				#inicialmente verificamos si las llaves estan generados o no
				Tabla5="Show index from `geolocalizacion`;"
				cursor.execute(Tabla5)
				resultados= cursor.fetchall()
				lresultados= list(resultados)
				llave= lresultados[0]
				llave=list(llave)
				Index_exists=False
				name='ZipCode'
				for r in llave:
					if r==name:
						Index_exists=True
				if Index_exists ==True:
					print("Las  llaves, indexados,relacines y restricciones ya existen")
				else:
					#Creamos llaves, indexados,relaciones y restricciones para la tabla Geolocalizacion
					TablaGeolocation0="ALTER TABLE `geolocalizacion` ADD PRIMARY KEY(`ZipCode`);"
					cursor.execute(TablaGeolocation0)
					TablaGeolocation1="ALTER TABLE vendedor ADD CONSTRAINT `vendedor_fk_geolocalizacion` FOREIGN KEY (ZipCode) REFERENCES geolocalizacion (ZipCode) ON DELETE RESTRICT ON UPDATE RESTRICT;"
					cursor.execute(TablaGeolocation1)
			conexion.commit()
		finally:
			conexion.close()
	except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
		print("Ocurrió un error al conectar: ", e)

def Pedido():
	try:
				conexion = pymysql.connect(host='localhost',
										user='root',
										password='',
										db='EcomerceBrazil')
				try:
					with conexion.cursor() as cursor:
						#inicialmente verificamos si las llaves estan generados o no
						Tabla5="Show index from `pedido`;"
						cursor.execute(Tabla5)
						resultados= cursor.fetchall()
						lresultados= list(resultados)
						llave= lresultados[0]
						llave=list(llave)
						Index_exists=False
						name='IdOrder'
						for r in llave:
							if r==name:
								Index_exists=True
						if Index_exists ==True:
							print("Las  llaves, indexados,relaci0nes y restricciones ya existen")
						else:
							#Creamos llaves, indexados,relaciones y restricciones para la tabla Pedido
							TablaOrder0="ALTER TABLE `pedido` ADD PRIMARY KEY(`IdOrder`);"
							cursor.execute(TablaOrder0)
							TablaOrder1="ALTER TABLE `pedido` ADD INDEX(`IdProduct`);"
							cursor.execute(TablaOrder1)
							TablaOrder2="ALTER TABLE `pedido` ADD INDEX(`IdVendedor`);"
							cursor.execute(TablaOrder2)
							TablaOrder3="ALTER TABLE `pedido` ADD INDEX(`FechalEmbar`);"
							cursor.execute(TablaOrder3)
							TablaOrder3="ALTER TABLE `pedido` ADD INDEX(`FechalEmbar`);"
							cursor.execute(TablaOrder3)
							TablaOrder4="ALTER TABLE statusorder ADD CONSTRAINT `statusorder_fk_pedido` FOREIGN KEY (IdOrder) REFERENCES pedido (IdOrder) ON DELETE RESTRICT ON UPDATE RESTRICT;"
							cursor.execute(TablaOrder4)
						conexion.commit()
				finally:
					conexion.close()
	except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
			print("Ocurrió un error al conectar: ", e)


def Pago():
	try:
				conexion = pymysql.connect(host='localhost',
										user='root',
										password='',
										db='EcomerceBrazil')
				try:
					with conexion.cursor() as cursor:
						#inicialmente verificamos si las llaves estan generados o no
						Tabla5="Show index from `Pago`;"
						cursor.execute(Tabla5)
						resultados= cursor.fetchall()
						lresultados= list(resultados)
						llave= lresultados[0]
						llave=list(llave)
						Index_exists=False
						name='IdOrder'
						for r in llave:
							if r==name:
								Index_exists=True
						if Index_exists ==True:
							print("Las  llaves, indexados,relaciones y restricciones ya existen")
						else:
							#Creamos llaves, indexados,relaciones y restricciones para la tabla Pago
							TablaPago0="ALTER TABLE `pago` ADD PRIMARY KEY(`IdPago`);"
							cursor.execute(TablaPago0)
							TablaPago1="ALTER TABLE `pago` ADD INDEX(`IdOrder`);"
							cursor.execute(TablaPago1)
							TablaPago2="ALTER TABLE pago ADD CONSTRAINT `pago_fk_statusorder` FOREIGN KEY (IdOrder) REFERENCES statusorder (IdOrder) ON DELETE RESTRICT ON UPDATE RESTRICT;"
							cursor.execute(TablaPago2)
							conexion.commit()
				finally:
					conexion.close()
	except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
			print("Ocurrió un error al conectar: ", e)


def statusorder():
	try:
				conexion = pymysql.connect(host='localhost',
										user='root',
										password='',
										db='EcomerceBrazil')
				try:
					with conexion.cursor() as cursor:
						#inicialmente verificamos si las llaves estan generados o no
						Tabla5="Show index from `statusorder`;"
						cursor.execute(Tabla5)
						resultados= cursor.fetchall()
						lresultados= list(resultados)
						llave= lresultados[0]
						llave=list(llave)
						Index_exists=False
						name='IdOrder'
						for r in llave:
							if r==name:
								Index_exists=True
						if Index_exists ==True:
							print("Las  llaves, indexados,relaciones y restricciones ya existen")
						else:			
							#Creamos llaves e indexados para la tabla statusorder
							Tablastatusorder0="ALTER TABLE `statusorder`ADD PRIMARY KEY(`IdStatusOrder`);"
							cursor.execute(Tablastatusorder0)
							Tablastatusorder1="ALTER TABLE `statusorder` ADD INDEX(`IdOrder`);"
							cursor.execute(Tablastatusorder1)
							Tablastatusorder2="ALTER TABLE `statusorder` ADD INDEX(`IdCliente`);"
							cursor.execute(Tablastatusorder2)
							Tablastatusorder3="ALTER TABLE `statusorder` ADD INDEX(`FechaCompra`);"
							cursor.execute(Tablastatusorder3)
							Tablastatusorder4="ALTER TABLE `statusorder` ADD INDEX(`FechaAprob`);"
							cursor.execute(Tablastatusorder4)
							Tablastatusorder5="ALTER TABLE `statusorder` ADD INDEX(`FechaEntreTr`);"
							cursor.execute(Tablastatusorder5)
							Tablastatusorder6="ALTER TABLE `statusorder` ADD INDEX(`FechaEntreCli`);"
							cursor.execute(Tablastatusorder6)
							Tablastatusorder7="ALTER TABLE `statusorder` ADD INDEX(`FechaEstiEntreg`);"
							cursor.execute(Tablastatusorder7)
							Tablastatusorder8="ALTER TABLE review ADD CONSTRAINT `review_fk_statusorder` FOREIGN KEY (IdOrder) REFERENCES statusorder (IdOrder) ON DELETE RESTRICT ON UPDATE RESTRICT;"
							cursor.execute(Tablastatusorder8)
			
				finally:
					conexion.close()
	except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
			print("Ocurrió un error al conectar: ", e)


def revieW():
	try:
				conexion = pymysql.connect(host='localhost',
										user='root',
										password='',
										db='EcomerceBrazil')
				try:
					with conexion.cursor() as cursor:
						#inicialmente verificamos si las llaves estan generados o no
						Tabla5="Show index from `revieW`;"
						cursor.execute(Tabla5)
						resultados= cursor.fetchall()
						lresultados= list(resultados)
						llave= lresultados[0]
						llave=list(llave)
						Index_exists=False
						name='IdReview'
						for r in llave:
							if r==name:
								Index_exists=True
						if Index_exists ==True:
							print("Las  llaves, indexados,relaciones y restricciones ya existen")
						else:
							#Creamos llaves e indexados para la tabla revieW
							TablaReview0="ALTER TABLE `review`ADD PRIMARY KEY(`IdReview`);"
							cursor.execute(TablaReview0)
							TablaReview1="ALTER TABLE `review` ADD INDEX(`IdOrder`);"
							cursor.execute(TablaReview1)
							TablaReview2="ALTER TABLE `review` ADD INDEX(`FechaCreación`);"
							cursor.execute(TablaReview2)
							TablaReview3="ALTER TABLE `review` ADD INDEX(`FechaRespuesta`);"
							cursor.execute(TablaReview3)	
				finally:
					conexion.close()
	except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
			print("Ocurrió un error al conectar: ", e)

def Producto():
		try:
					conexion = pymysql.connect(host='localhost',
											user='root',
											password='',
											db='EcomerceBrazil')
					try:
						with conexion.cursor() as cursor:
							#inicialmente verificamos si las llaves estan generados o no
							Tabla5="Show index from `producto`;"
							cursor.execute(Tabla5)
							resultados= cursor.fetchall()
							lresultados= list(resultados)
							llave= lresultados[0]
							llave=list(llave)
							Index_exists=False
							name='IdProduct'
							for r in llave:
								if r==name:
									Index_exists=True
							if Index_exists ==True:
								print("Las  llaves, indexados,relaciones y restricciones ya existen")
							else:
								#Creamos llaves e indexados para la tabla producto
								TablaProducto0="ALTER TABLE `producto`ADD PRIMARY KEY(`IdProduct`);"
								cursor.execute(TablaProducto0)
								TablaProducto1="ALTER TABLE `producto` ADD INDEX(`IdCategoria`);"
								cursor.execute(TablaProducto1)	
								TablaProducto2="ALTER TABLE producto ADD CONSTRAINT `producto_fk_pedido` FOREIGN KEY (IdProduct) REFERENCES pedido (IdProduct) ON DELETE RESTRICT ON UPDATE RESTRICT;"
								cursor.execute(TablaProducto2)
								TablaProducto3="ALTER TABLE producto ADD CONSTRAINT `producto_fk_categoria` FOREIGN KEY (IdCategoria) REFERENCES categoria (IdCategoria) ON DELETE RESTRICT ON UPDATE RESTRICT;"
								cursor.execute(TablaProducto3)
					finally:
						conexion.close()
		except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
				print("Ocurrió un error al conectar: ", e)

def Vendedor():
		try:
					conexion = pymysql.connect(host='localhost',
											user='root',
											password='',
											db='EcomerceBrazil')
					try:
						with conexion.cursor() as cursor:
							#inicialmente verificamos si las llaves estan generados o no
							Tabla5="Show index from `vendedor`;"
							cursor.execute(Tabla5)
							resultados= cursor.fetchall()
							lresultados= list(resultados)
							llave= lresultados[0]
							llave=list(llave)
							Index_exists=False
							name='IdVendedor'
							for r in llave:
								if r==name:
									Index_exists=True
							if Index_exists ==True:
								print("Las  llaves, indexados,relaciones y restricciones ya existen")
							else:
								#Creamos llaves e indexados para la tabla vendedor
								TablaVendedor0="ALTER TABLE `vendedor`ADD PRIMARY KEY(`IdVendedor`);"
								cursor.execute(TablaVendedor0)
								TablaVendedor1="ALTER TABLE `vendedor` ADD INDEX(`ZipCode`);"
								cursor.execute(TablaVendedor1)
								TablaVendedor3="ALTER TABLE tratocerrado ADD CONSTRAINT `tratocerrado_fk_vendedor` FOREIGN KEY (IdVendedor) REFERENCES vendedor (IdVendedor) ON DELETE RESTRICT ON UPDATE RESTRICT;"
								cursor.execute(TablaVendedor3)
								TablaVendedor4="ALTER TABLE pedido ADD CONSTRAINT `pedido_fk_tratocerrado` FOREIGN KEY (IdVendedor) REFERENCES tratocerrado (IdVendedor) ON DELETE RESTRICT ON UPDATE RESTRICT;"
								cursor.execute(TablaVendedor4)
					finally:
						conexion.close()
		except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
				print("Ocurrió un error al conectar: ", e)

def Categoria():
		try:
					conexion = pymysql.connect(host='localhost',
											user='root',
											password='',
											db='EcomerceBrazil')
					try:
						with conexion.cursor() as cursor:
							#inicialmente verificamos si las llaves estan generados o no
							Tabla5="Show index from `categoria`;"
							cursor.execute(Tabla5)
							resultados= cursor.fetchall()
							lresultados= list(resultados)
							llave= lresultados[0]
							llave=list(llave)
							Index_exists=False
							name='IdCategoria'
							for r in llave:
								if r==name:
									Index_exists=True
							if Index_exists ==True:
								print("Las  llaves, indexados,relaciones y restricciones ya existen")
							else:
								#Creamos llaves e indexados para la tabla categoria
								TablaCategoria="CREATE TABLE IF NOT EXISTS categoria (IdCategoria INT, Categoria VARCHAR(50), CategIngles VARCHAR(100)) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish_ci;"
								cursor.execute(TablaCategoria)
								TablaCategoria="ALTER TABLE `categoria` ADD PRIMARY KEY(`IdCatergoria`);"
								cursor.execute(TablaCategoria)
					finally:
						conexion.close()
		except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
				print("Ocurrió un error al conectar: ", e)

def tratocerrado():
		try:
					conexion = pymysql.connect(host='localhost',
											user='root',
											password='',
											db='EcomerceBrazil')
					try:
						with conexion.cursor() as cursor:
							#inicialmente verificamos si las llaves estan generados o no
							Tabla5="Show index from `tratocerrado`;"
							cursor.execute(Tabla5)
							resultados= cursor.fetchall()
							lresultados= list(resultados)
							llave= lresultados[0]
							llave=list(llave)
							Index_exists=False
							name='IdCategoria'
							for r in llave:
								if r==name:
									Index_exists=True
							if Index_exists ==True:
								print("Las  llaves, indexados,relaciones y restricciones ya existen")
							else:
								#Creamos llaves e indexados para la tabla tratocerrado
								Tablatratocerrado="ALTER TABLE `tratocerrado` ADD PRIMARY KEY(`IdClientePot`);"
								cursor.execute(Tablatratocerrado)
								Tablatratocerrado0="ALTER TABLE `tratocerrado` ADD INDEX(`IdVendedor`);"
								cursor.execute(Tablatratocerrado0)
								Tablatratocerrado1="ALTER TABLE `tratocerrado` ADD INDEX(`IdRepDesarr`);"
								cursor.execute(Tablatratocerrado1)
								Tablatratocerrado2="ALTER TABLE `tratocerrado` ADD INDEX(`IdRepVentas`);"
								cursor.execute(Tablatratocerrado2)
								Tablatratocerrado2="ALTER TABLE `tratocerrado` ADD INDEX(`FechaCierre`);"
								cursor.execute(Tablatratocerrado2)
								TablaVendedor3="ALTER TABLE tratocerrado ADD CONSTRAINT `tratocerrado_fk_marketing` FOREIGN KEY (IdClientePot) REFERENCES marketing (IdClientePot) ON DELETE RESTRICT ON UPDATE RESTRICT;"
								cursor.execute(TablaVendedor3)
					finally:
						conexion.close()
		except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
				print("Ocurrió un error al conectar: ", e)

def Marketing():
		try:
					conexion = pymysql.connect(host='localhost',
											user='root',
											password='',
											db='EcomerceBrazil')
					try:
						with conexion.cursor() as cursor:
							#inicialmente verificamos si las llaves estan generados o no
							Tabla5="Show index from `marketing`;"
							cursor.execute(Tabla5)
							resultados= cursor.fetchall()
							lresultados= list(resultados)
							llave= lresultados[0]
							llave=list(llave)
							Index_exists=False
							name='IdClientePot'
							for r in llave:
								if r==name:
									Index_exists=True
							if Index_exists ==True:
								print("Las  llaves, indexados,relaciones y restricciones ya existen")
							else:
								#Creamos llaves e indexados para la tabla Marketing
								TablaMarketing1="ALTER TABLE `marketing` ADD PRIMARY KEY(`IdClientePot`);"
								cursor.execute(TablaMarketing1)
								TablaMarketing2="ALTER TABLE `marketing` ADD INDEX(`FechaPrcontacto`);"
								cursor.execute(TablaMarketing2)
								TablaMarketing3="ALTER TABLE `marketing` ADD INDEX(`IdPagina`);"
								cursor.execute(TablaMarketing3)
								TablaMarketing4="ALTER TABLE `marketing` ADD INDEX(`Origen`);"
								cursor.execute(TablaMarketing4)
	
					finally:
						conexion.close()
		except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
				print("Ocurrió un error al conectar: ", e)

