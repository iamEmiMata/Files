
import mysql.connector
import logging

class conexion():

	dbName = input('Enter DbName to consult >>> ')
	def __init__(self):
		logging.basicConfig(filename = 'logMain.log', level = 'DEBUG')
		try:
			self.conexion = mysql.connector.connect(
				host = '127.0.0.1',
				port = 3306,
				user = 'root',
				password = '',
				db = self.dbName) # self.dbName

			# validamos
			if self.conexion.is_connected():
				dbInfo = self.conexion.get_server_info()
				logging.info(f'Connection is working... {dbInfo}')
				# print('Connection is working... ', dbInfo)
		except Exception as e:
			print('Connection has failed... ', e)
			logging.error(f'Connection has failed... {e}')
		# finally:
		# 	# Cerramos conexion
		# 	if self.conexion.is_connected():
		# 		self.conexion.close()
		# 		print('Connection is closed')

	def commandLine(self):
		try:
			if self.conexion.is_connected():
				cursor = self.conexion.cursor()
				# Sql commands
				sqlCommands = input('>>> ')
				commandIndex = sqlCommands.split() # ['show','tables'] 
				cursor.execute(sqlCommands)

				# If fetch : Lista resultados else commit()
				if commandIndex[0] == 'show' or commandIndex[0] == 'select' or commandIndex[0] == 'describe' :
					fetch = cursor.fetchall()
					if fetch == []:
						print(cursor.rowcount, ' rows found ')

					for results in fetch:
						print(results)
					logging.debug(' >> fetch done ')
				else: 
					try:
						self.conexion.commit()
						print('>>> ', cursor.rowcount, ' affected ')
						logging.debug(' >> commit done ')
					except Exception as e:
						print(e)
						logging.error(f' >> commit {e}')


		except:
			self.conexion.rollback()
			logging.debug(' >> rollback done')
		finally:
			cursor.close()
			logging.debug(' >> cursor close')


run = conexion()

continuar = True
while continuar :
	run.commandLine()

	exit = input('\nEnter to continue. . . To exit 0  >>>  ')
	if exit == '0':
		continuar = False
	else:
		continuar = True

# print('Connection is closed')
logging.info(' >> Connection is closed')