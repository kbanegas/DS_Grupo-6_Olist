import mysql.connector
import time
import datetime
#import mysql
import pymysql

class Relaciones:
	def clientes(self):
		try:
			self.conexion = pymysql.connect(host='localhost',
									user='root',
									password='',
									db='EcomerceBrazil')
			try:
				with self.conexion.cursor() as self.cursor:
					#inicialmente verificamos si las llaves estan generados o no
					self.cursor.execute("USE EcomerceBrazil;")
					Tabla5="Show index from `cliente`;"
					self.cursor.execute(Tabla5)
					resultados= self.cursor.fetchall()
					lresultados= list(resultados)
					if not lresultados:
						TablaCustomer0="ALTER TABLE `cliente` ADD PRIMARY KEY(`IdCliente`);"
						self.cursor.execute(TablaCustomer0)
						TablaCustomer1="ALTER TABLE `cliente` ADD INDEX (`Unique_IdCliente`);"
						self.cursor.execute(TablaCustomer1)
						TablaCustomer2="ALTER TABLE `cliente` ADD INDEX (`ZipCode`);"
						self.cursor.execute(TablaCustomer2)
						TablaCustomer3="ALTER TABLE statusorder ADD CONSTRAINT `statusorder_fk_cliente` FOREIGN KEY (IdCliente) REFERENCES cliente (IdCliente) ON DELETE RESTRICT ON UPDATE RESTRICT;"
						self.cursor.execute(TablaCustomer3)
					else:
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
							self.cursor.execute(TablaCustomer0)
							TablaCustomer1="ALTER TABLE `cliente` ADD INDEX (`Unique_IdCliente`);"
							self.cursor.execute(TablaCustomer1)
							TablaCustomer2="ALTER TABLE `cliente` ADD INDEX (`ZipCode`);"
							self.cursor.execute(TablaCustomer2)
							TablaCustomer3="ALTER TABLE statusorder ADD CONSTRAINT `statusorder_fk_cliente` FOREIGN KEY (IdCliente) REFERENCES cliente (IdCliente) ON DELETE RESTRICT ON UPDATE RESTRICT;"
							self.cursor.execute(TablaCustomer3)		
				self.conexion.commit()
			finally:
				
				self.conexion.close()
		except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
					print("Ocurrió un error al conectar: ", e)
		
		

	def Geolocalizacion(self):

		try:
			self.conexion = pymysql.connect(host='localhost',
									user='root',
									password='',
									db='EcomerceBrazil')
			try:
				with self.conexion.cursor() as self.cursor:
					#inicialmente verificamos si las llaves estan generados o no
					self.cursor.execute("USE EcomerceBrazil;")
					Tabla5="Show index from `geolocalizacion`;"
					self.cursor.execute(Tabla5)
					resultados= self.cursor.fetchall()
					lresultados= list(resultados)
					if not lresultados:
						#Creamos llaves, indexados,relaciones y restricciones para la tabla Geolocalizacion
						TablaGeolocation0="ALTER TABLE `geolocalizacion` ADD PRIMARY KEY(`ZipCode`);"
						self.cursor.execute(TablaGeolocation0)
						TablaGeolocation1="ALTER TABLE cliente ADD CONSTRAINT `cliente_fk_geolocalizacion` FOREIGN KEY (ZipCode) REFERENCES geolocalizacion (ZipCode) ON DELETE RESTRICT ON UPDATE RESTRICT;"
						self.cursor.execute(TablaGeolocation1)
					else:
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
							self.cursor.execute(TablaGeolocation0)
							TablaGeolocation1="ALTER TABLE cliente ADD CONSTRAINT `cliente_fk_geolocalizacion` FOREIGN KEY (ZipCode) REFERENCES geolocalizacion (ZipCode) ON DELETE RESTRICT ON UPDATE RESTRICT;"
							self.cursor.execute(TablaGeolocation1)
				self.conexion.commit()
			finally:
				self.conexion.close()
		except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
			print("Ocurrió un error al conectar: ", e)

	def Pedido(self):
		try:
					self.conexion = pymysql.connect(host='localhost',
											user='root',
											password='',
											db='EcomerceBrazil')
					try:
						with self.conexion.cursor() as self.cursor:
							#inicialmente verificamos si las llaves estan generados o no
							self.cursor.execute("USE EcomerceBrazil;")
							Tabla5="Show index from `pedido`;"
							self.cursor.execute(Tabla5)
							resultados= self.cursor.fetchall()
							lresultados= list(resultados)
							if not lresultados:
								#Creamos llaves, indexados,relaciones y restricciones para la tabla Pedido
								TablaOrder0="ALTER TABLE `pedido` ADD PRIMARY KEY(`IdOrder`);"
								self.cursor.execute(TablaOrder0)
								TablaOrder1="ALTER TABLE `pedido` ADD INDEX(`IdProduct`);"
								self.cursor.execute(TablaOrder1)
								TablaOrder2="ALTER TABLE `pedido` ADD INDEX(`IdVendedor`);"
								self.cursor.execute(TablaOrder2)
								TablaOrder3="ALTER TABLE `pedido` ADD INDEX(`FechalEmbar`);"
								self.cursor.execute(TablaOrder3)
								TablaOrder3="ALTER TABLE `pedido` ADD INDEX(`FechalEmbar`);"
								self.cursor.execute(TablaOrder3)
								TablaOrder4="ALTER TABLE statusorder ADD CONSTRAINT `statusorder_fk_pedido` FOREIGN KEY (IdOrder) REFERENCES pedido (IdOrder) ON DELETE RESTRICT ON UPDATE RESTRICT;"
								self.cursor.execute(TablaOrder4)
							else:
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
									#Creamos llaves, indexados,relaciones y restricciones para la tabla Pedido
									TablaOrder0="ALTER TABLE `pedido` ADD PRIMARY KEY(`IdOrder`);"
									self.cursor.execute(TablaOrder0)
									TablaOrder1="ALTER TABLE `pedido` ADD INDEX(`IdProduct`);"
									self.cursor.execute(TablaOrder1)
									TablaOrder2="ALTER TABLE `pedido` ADD INDEX(`IdVendedor`);"
									self.cursor.execute(TablaOrder2)
									TablaOrder3="ALTER TABLE `pedido` ADD INDEX(`FechalEmbar`);"
									self.cursor.execute(TablaOrder3)
									TablaOrder3="ALTER TABLE `pedido` ADD INDEX(`FechalEmbar`);"
									self.cursor.execute(TablaOrder3)
									TablaOrder4="ALTER TABLE statusorder ADD CONSTRAINT `statusorder_fk_pedido` FOREIGN KEY (IdOrder) REFERENCES pedido (IdOrder) ON DELETE RESTRICT ON UPDATE RESTRICT;"
									self.cursor.execute(TablaOrder4)
							self.conexion.commit()
					finally:
						self.conexion.close()
		except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
				print("Ocurrió un error al conectar: ", e)


	def Pago(self):
		try:
					self.conexion = pymysql.connect(host='localhost',
											user='root',
											password='',
											db='EcomerceBrazil')
					try:
						with self.conexion.cursor() as self.cursor:
							#inicialmente verificamos si las llaves estan generados o no
							self.cursor.execute("USE EcomerceBrazil;")
							Tabla5="Show index from `Pago`;"
							self.cursor.execute(Tabla5)
							resultados= self.cursor.fetchall()
							lresultados= list(resultados)
							if not lresultados:
								#Creamos llaves, indexados,relaciones y restricciones para la tabla Pago
								TablaPago0="ALTER TABLE `pago` ADD PRIMARY KEY(`IdPago`);"
								self.cursor.execute(TablaPago0)
								TablaPago1="ALTER TABLE `pago` ADD INDEX(`IdOrder`);"
								self.cursor.execute(TablaPago1)
								self.conexion.commit()
							else:
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
									self.cursor.execute(TablaPago0)
									TablaPago1="ALTER TABLE `pago` ADD INDEX(`IdOrder`);"
									self.cursor.execute(TablaPago1)
							self.conexion.commit()
					finally:
						self.conexion.close()
		except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
				print("Ocurrió un error al conectar: ", e)


	def statusorder(self):
		try:
					self.conexion = pymysql.connect(host='localhost',
											user='root',
											password='',
											db='EcomerceBrazil')
					try:
						with self.conexion.cursor() as self.cursor:
							#inicialmente verificamos si las llaves estan generados o no
							self.cursor.execute("USE EcomerceBrazil;")
							Tabla5="Show index from `statusorder`;"
							self.cursor.execute(Tabla5)
							resultados= self.cursor.fetchall()
							lresultados= list(resultados)
							if not lresultados:
								#Creamos llaves e indexados para la tabla statusorder
								Tablastatusorder0="ALTER TABLE `statusorder`ADD PRIMARY KEY(`IdStatusOrder`);"
								self.cursor.execute(Tablastatusorder0)
								Tablastatusorder1="ALTER TABLE `statusorder` ADD INDEX(`IdOrder`);"
								self.cursor.execute(Tablastatusorder1)
								Tablastatusorder2="ALTER TABLE `statusorder` ADD INDEX(`IdCliente`);"
								self.cursor.execute(Tablastatusorder2)
								Tablastatusorder3="ALTER TABLE `statusorder` ADD INDEX(`FechaCompra`);"
								self.cursor.execute(Tablastatusorder3)
								Tablastatusorder4="ALTER TABLE `statusorder` ADD INDEX(`FechaAprob`);"
								self.cursor.execute(Tablastatusorder4)
								Tablastatusorder5="ALTER TABLE `statusorder` ADD INDEX(`FechaEntreTr`);"
								self.cursor.execute(Tablastatusorder5)
								Tablastatusorder6="ALTER TABLE `statusorder` ADD INDEX(`FechaEntreCli`);"
								self.cursor.execute(Tablastatusorder6)
								Tablastatusorder7="ALTER TABLE `statusorder` ADD INDEX(`FechaEstiEntreg`);"
								self.cursor.execute(Tablastatusorder7)
								TablaPago2="ALTER TABLE pago ADD CONSTRAINT `pago_fk_pedido` FOREIGN KEY (IdOrder) REFERENCES pedido (IdOrder) ON DELETE RESTRICT ON UPDATE RESTRICT;"
								self.cursor.execute(TablaPago2)
							else:
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
									self.cursor.execute(Tablastatusorder0)
									Tablastatusorder1="ALTER TABLE `statusorder` ADD INDEX(`IdOrder`);"
									self.cursor.execute(Tablastatusorder1)
									Tablastatusorder2="ALTER TABLE `statusorder` ADD INDEX(`IdCliente`);"
									self.cursor.execute(Tablastatusorder2)
									Tablastatusorder3="ALTER TABLE `statusorder` ADD INDEX(`FechaCompra`);"
									self.cursor.execute(Tablastatusorder3)
									Tablastatusorder4="ALTER TABLE `statusorder` ADD INDEX(`FechaAprob`);"
									self.cursor.execute(Tablastatusorder4)
									Tablastatusorder5="ALTER TABLE `statusorder` ADD INDEX(`FechaEntreTr`);"
									self.cursor.execute(Tablastatusorder5)
									Tablastatusorder6="ALTER TABLE `statusorder` ADD INDEX(`FechaEntreCli`);"
									self.cursor.execute(Tablastatusorder6)
									Tablastatusorder7="ALTER TABLE `statusorder` ADD INDEX(`FechaEstiEntreg`);"
									self.cursor.execute(Tablastatusorder7)
									TablaPago2="ALTER TABLE pago ADD CONSTRAINT `pago_fk_pedido` FOREIGN KEY (IdOrder) REFERENCES pedido (IdOrder) ON DELETE RESTRICT ON UPDATE RESTRICT;"
									self.cursor.execute(TablaPago2)
							self.conexion.commit()
					finally:
						self.conexion.close()
		except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
				print("Ocurrió un error al conectar: ", e)


	def revieW(self):
		try:
					self.conexion = pymysql.connect(host='localhost',
											user='root',
											password='',
											db='EcomerceBrazil')
					try:
						with self.conexion.cursor() as self.cursor:
							#inicialmente verificamos si las llaves estan generados o no
							self.cursor.execute("USE EcomerceBrazil;")
							Tabla5="Show index from `revieW`;"
							self.cursor.execute(Tabla5)
							resultados= self.cursor.fetchall()
							lresultados= list(resultados)
							if not lresultados:
								#Creamos llaves e indexados para la tabla revieW
								TablaReview0="ALTER TABLE `review`ADD PRIMARY KEY(`IdReview`);"
								self.cursor.execute(TablaReview0)
								TablaReview1="ALTER TABLE `review` ADD INDEX(`IdOrder`);"
								self.cursor.execute(TablaReview1)
								TablaReview2="ALTER TABLE `review` ADD INDEX(`FechaCreación`);"
								self.cursor.execute(TablaReview2)
								TablaReview3="ALTER TABLE `review` ADD INDEX(`FechaRespuesta`);"
								self.cursor.execute(TablaReview3)
								Tablastatusorder8="ALTER TABLE review ADD CONSTRAINT `review_fk_pedido` FOREIGN KEY (IdOrder) REFERENCES pedido (IdOrder) ON DELETE RESTRICT ON UPDATE RESTRICT;"
								self.cursor.execute(Tablastatusorder8)
							else:
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
									self.cursor.execute(TablaReview0)
									TablaReview1="ALTER TABLE `review` ADD INDEX(`IdOrder`);"
									self.cursor.execute(TablaReview1)
									TablaReview2="ALTER TABLE `review` ADD INDEX(`FechaCreación`);"
									self.cursor.execute(TablaReview2)
									TablaReview3="ALTER TABLE `review` ADD INDEX(`FechaRespuesta`);"
									self.cursor.execute(TablaReview3)
									Tablastatusorder8="ALTER TABLE review ADD CONSTRAINT `review_fk_pedido` FOREIGN KEY (IdOrder) REFERENCES pedido (IdOrder) ON DELETE RESTRICT ON UPDATE RESTRICT;"
									self.cursor.execute(Tablastatusorder8)
							self.conexion.commit()				
					finally:
						self.conexion.close()
		except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
				print("Ocurrió un error al conectar: ", e)

	def Producto(self):
			try:
						self.conexion = pymysql.connect(host='localhost',
												user='root',
												password='',
												db='EcomerceBrazil')
						try:
							with self.conexion.cursor() as self.cursor:
								#inicialmente verificamos si las llaves estan generados o no
								self.cursor.execute("USE EcomerceBrazil;")
								Tabla5="Show index from `producto`;"
								self.cursor.execute(Tabla5)
								resultados= self.cursor.fetchall()
								lresultados= list(resultados)
								if not lresultados:
									#Creamos llaves e indexados para la tabla producto
									TablaProducto0="ALTER TABLE `producto`ADD PRIMARY KEY(`IdProduct`);"
									self.cursor.execute(TablaProducto0)
									TablaProducto1="ALTER TABLE `producto` ADD INDEX(`IdCategoria`);"
									self.cursor.execute(TablaProducto1)	
									TablaProducto2="ALTER TABLE producto ADD CONSTRAINT `producto_fk_pedido` FOREIGN KEY (IdProduct) REFERENCES pedido (IdProduct) ON DELETE RESTRICT ON UPDATE RESTRICT;"
									self.cursor.execute(TablaProducto2)
								else:
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
										self.cursor.execute(TablaProducto0)
										TablaProducto1="ALTER TABLE `producto` ADD INDEX(`IdCategoria`);"
										self.cursor.execute(TablaProducto1)	
										TablaProducto2="ALTER TABLE producto ADD CONSTRAINT `producto_fk_pedido` FOREIGN KEY (IdProduct) REFERENCES pedido (IdProduct) ON DELETE RESTRICT ON UPDATE RESTRICT;"
										self.cursor.execute(TablaProducto2)
								self.conexion.commit()
						finally:
							self.conexion.close()
			except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
					print("Ocurrió un error al conectar: ", e)

	def Vendedor(self):
			try:
						self.conexion = pymysql.connect(host='localhost',
												user='root',
												password='',
												db='EcomerceBrazil')
						try:
							with self.conexion.cursor() as self.cursor:
								#inicialmente verificamos si las llaves estan generados o no
								self.cursor.execute("USE EcomerceBrazil;")
								Tabla5="Show index from `vendedor`;"
								self.cursor.execute(Tabla5)
								resultados= self.cursor.fetchall()
								lresultados= list(resultados)
								if not lresultados:
									#Creamos llaves e indexados para la tabla vendedor
									TablaVendedor0="ALTER TABLE `vendedor`ADD PRIMARY KEY(`IdVendedor`);"
									self.cursor.execute(TablaVendedor0)
									TablaVendedor1="ALTER TABLE `vendedor` ADD INDEX(`ZipCode`);"
									self.cursor.execute(TablaVendedor1)
									TablaVendedor3="ALTER TABLE tratocerrado ADD CONSTRAINT `tratocerrado_fk_vendedor` FOREIGN KEY (IdVendedor) REFERENCES vendedor (IdVendedor) ON DELETE RESTRICT ON UPDATE RESTRICT;"
									self.cursor.execute(TablaVendedor3)
									TablaVendedor4="ALTER TABLE pedido ADD CONSTRAINT `pedido_fk_tratocerrado` FOREIGN KEY (IdVendedor) REFERENCES tratocerrado (IdVendedor) ON DELETE RESTRICT ON UPDATE RESTRICT;"
									self.cursor.execute(TablaVendedor4)
								else:
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
										self.cursor.execute(TablaVendedor0)
										TablaVendedor1="ALTER TABLE `vendedor` ADD INDEX(`ZipCode`);"
										self.cursor.execute(TablaVendedor1)
										TablaVendedor3="ALTER TABLE tratocerrado ADD CONSTRAINT `tratocerrado_fk_vendedor` FOREIGN KEY (IdVendedor) REFERENCES vendedor (IdVendedor) ON DELETE RESTRICT ON UPDATE RESTRICT;"
										self.cursor.execute(TablaVendedor3)
										TablaVendedor4="ALTER TABLE pedido ADD CONSTRAINT `pedido_fk_tratocerrado` FOREIGN KEY (IdVendedor) REFERENCES tratocerrado (IdVendedor) ON DELETE RESTRICT ON UPDATE RESTRICT;"
										self.cursor.execute(TablaVendedor4)
							self.conexion.commit()
						finally:
							self.conexion.close()
			except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
					print("Ocurrió un error al conectar: ", e)

	def Categoria(self):
			try:
						self.conexion = pymysql.connect(host='localhost',
												user='root',
												password='',
												db='EcomerceBrazil')
						try:
							with self.conexion.cursor() as self.cursor:
								#inicialmente verificamos si las llaves estan generados o no
								self.cursor.execute("USE EcomerceBrazil;")
								Tabla5="Show index from `categoria`;"
								self.cursor.execute(Tabla5)
								resultados= self.cursor.fetchall()
								lresultados= list(resultados)
								if not lresultados:
									#Creamos llaves e indexados para la tabla categoria
									TablaCategoria="CREATE TABLE IF NOT EXISTS categoria (IdCategoria INT, Categoria VARCHAR(50), CategIngles VARCHAR(100)) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish_ci;"
									self.cursor.execute(TablaCategoria)
									TablaCategoria="ALTER TABLE `categoria` ADD PRIMARY KEY(`IdCategoria`);"
									self.cursor.execute(TablaCategoria)
									TablaProducto3="ALTER TABLE producto ADD CONSTRAINT `producto_fk_categoria` FOREIGN KEY (IdCategoria) REFERENCES categoria (IdCategoria) ON DELETE RESTRICT ON UPDATE RESTRICT;"
									self.cursor.execute(TablaProducto3)
								else:
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
										self.cursor.execute(TablaCategoria)
										TablaCategoria="ALTER TABLE `categoria` ADD PRIMARY KEY(`IdCategoria`);"
										self.cursor.execute(TablaCategoria)
										TablaProducto3="ALTER TABLE producto ADD CONSTRAINT `producto_fk_categoria` FOREIGN KEY (IdCategoria) REFERENCES categoria (IdCategoria) ON DELETE RESTRICT ON UPDATE RESTRICT;"
										self.cursor.execute(TablaProducto3)
							self.conexion.commit()
						finally:
							self.conexion.close()
			except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
					print("Ocurrió un error al conectar: ", e)

	def tratocerrado(self):
			try:
						self.conexion = pymysql.connect(host='localhost',
												user='root',
												password='',
												db='EcomerceBrazil')
						try:
							with self.conexion.cursor() as self.cursor:
								#inicialmente verificamos si las llaves estan generados o no
								self.cursor.execute("USE EcomerceBrazil;")
								Tabla5="Show index from `tratocerrado`;"
								self.cursor.execute(Tabla5)
								resultados= self.cursor.fetchall()
								lresultados= list(resultados)
								if not lresultados:
									#Creamos llaves e indexados para la tabla tratocerrado
									Tablatratocerrado="ALTER TABLE `tratocerrado` ADD PRIMARY KEY(`IdClientePot`);"
									self.cursor.execute(Tablatratocerrado)
									Tablatratocerrado0="ALTER TABLE `tratocerrado` ADD INDEX(`IdVendedor`);"
									self.cursor.execute(Tablatratocerrado0)
									Tablatratocerrado1="ALTER TABLE `tratocerrado` ADD INDEX(`IdRepDesarr`);"
									self.cursor.execute(Tablatratocerrado1)
									Tablatratocerrado2="ALTER TABLE `tratocerrado` ADD INDEX(`IdRepVentas`);"
									self.cursor.execute(Tablatratocerrado2)
									Tablatratocerrado2="ALTER TABLE `tratocerrado` ADD INDEX(`FechaCierre`);"
									self.cursor.execute(Tablatratocerrado2)
									
								else:
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
										self.cursor.execute(Tablatratocerrado)
										Tablatratocerrado0="ALTER TABLE `tratocerrado` ADD INDEX(`IdVendedor`);"
										self.cursor.execute(Tablatratocerrado0)
										Tablatratocerrado1="ALTER TABLE `tratocerrado` ADD INDEX(`IdRepDesarr`);"
										self.cursor.execute(Tablatratocerrado1)
										Tablatratocerrado2="ALTER TABLE `tratocerrado` ADD INDEX(`IdRepVentas`);"
										self.cursor.execute(Tablatratocerrado2)
										Tablatratocerrado2="ALTER TABLE `tratocerrado` ADD INDEX(`FechaCierre`);"
										self.cursor.execute(Tablatratocerrado2)
										
							self.conexion.commit()
						finally:
							self.conexion.close()
			except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
					print("Ocurrió un error al conectar: ", e)

	def Marketing(self):
			try:
						self.conexion = pymysql.connect(host='localhost',
												user='root',
												password='',
												db='EcomerceBrazil')
						try:
							with self.conexion.cursor() as self.cursor:
								#inicialmente verificamos si las llaves estan generados o no
								self.cursor.execute("USE EcomerceBrazil;")
								Tabla5="Show index from `marketing`;"
								self.cursor.execute(Tabla5)
								resultados= self.cursor.fetchall()
								lresultados= list(resultados)
								if not lresultados:
									#Creamos llaves e indexados para la tabla Marketing
									TablaMarketing1="ALTER TABLE `marketing` ADD PRIMARY KEY(`IdClientePot`);"
									self.cursor.execute(TablaMarketing1)
									TablaMarketing2="ALTER TABLE `marketing` ADD INDEX(`FechaPrcontacto`);"
									self.cursor.execute(TablaMarketing2)
									TablaMarketing3="ALTER TABLE `marketing` ADD INDEX(`IdPagina`);"
									self.cursor.execute(TablaMarketing3)
									TablaMarketing4="ALTER TABLE `marketing` ADD INDEX(`Origen`);"
									self.cursor.execute(TablaMarketing4)
									TablaVendedor3="ALTER TABLE tratocerrado ADD CONSTRAINT `tratocerrado_fk_marketing` FOREIGN KEY (IdClientePot) REFERENCES marketing (IdClientePot) ON DELETE RESTRICT ON UPDATE RESTRICT;"
									self.cursor.execute(TablaVendedor3)
								else:
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
										self.cursor.execute(TablaMarketing1)
										TablaMarketing2="ALTER TABLE `marketing` ADD INDEX(`FechaPrcontacto`);"
										self.cursor.execute(TablaMarketing2)
										TablaMarketing3="ALTER TABLE `marketing` ADD INDEX(`IdPagina`);"
										self.cursor.execute(TablaMarketing3)
										TablaMarketing4="ALTER TABLE `marketing` ADD INDEX(`Origen`);"
										self.cursor.execute(TablaMarketing4)
										TablaVendedor3="ALTER TABLE tratocerrado ADD CONSTRAINT `tratocerrado_fk_marketing` FOREIGN KEY (IdClientePot) REFERENCES marketing (IdClientePot) ON DELETE RESTRICT ON UPDATE RESTRICT;"
										self.cursor.execute(TablaVendedor3)
							self.conexion.commit()
						finally:
							#pass
							self.conexion.close()
			except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
					print("Ocurrió un error al conectar: ", e)
	def cerrar(self):
		self.conexion.close()


Drela=Relaciones()
Drela.clientes()
Drela.Geolocalizacion()
Drela.Pedido()
Drela.Pago()
Drela.statusorder()
Drela.revieW()
Drela.Producto()
Drela.Vendedor()
Drela.Categoria()
Drela.tratocerrado()
Drela.Marketing()

