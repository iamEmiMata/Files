
# loggers

# Una de las utilidades más usadas de los decoradores son los logger. Su
# uso nos permite escribir en un fichero los resultados de ciertas
# operaciones, que funciones han sido llamadas, o cualquier información
# que en un futuro resulte útil para ver que ha pasado.

# En el siguiente ejemplo tenemos un uso más completo del decorador
# log() que escribe en un fichero los resultados de las funciones que
# han sido llamadas.


# logs, bitacoras
''' 
python provee una biblioteca que nos permite trabajar con logs basicos.
Los logs son utiles cuando los programas se vuelven mas complejos
nos sirven para conocer problemas, ayudarnos en el debug y problemas
de desempeno

existen diferentes niveles de loggin dependiendo de la importancia

NOTSET = 0, DEBUG = 10, INFO = 20, WARN = 30, ERROR = 40, CRITICAL = 50

El formateador del log le coloca al mensaje del log informacion que da
contexto (archivo, linea, metodo, hilo, y proceso)

El handler es el componente que muestra o escribe el log
puede hacerlo a un archivo FileHandler, en la consola StreamHandler
o por Email SMTPHandler, son los mas comunes

http://docs.python.org/3/library/loggin.handlers.html#module-logging.handlers

El handler tiene dos campos : el formateador y el nivel
el nivel filtra a los logs inferiores

Para crear un logger tenemos que obtenerlos con getLogger()
El logger tiene tres campos
propagacion tiene tres campos
Propagacion - Decide si el log se debe de propagar al padre del logger
Nivel - Se usa para filtrar logs menos importantes
Handlers - La lista de handlers a los que sera enviado el log .
Esto permite un archivo para los DEBUG y un email para los CRITICAL

El logger se identifica en un sistema jerarquico, teniendo hasta arriba al
root logger  > logging.root

Su nivel es WARN y loggers es creado solo como un hijo del root

El nivel efectivo es el mismo que el nivel si el nivel no es NOTSET
El nivel efectivo es el mismo que el antepasado mas cercado si el nivel NOTSET
y el antepasado no es NOTSET

'''

# https://realpython.com/python-logging/
# https://python-intermedio.readthedocs.io/es/latest/args_and_kwargs.html
# https://www.rfc-editor.org/rfc/rfc5424

import logging

def main():
	
	host = '127.0.0.1'
	user = 'root'

	logging.basicConfig(filename = 'logTest.log', level = 'DEBUG')

	logging.critical('error critico al conectar con el host')
	logging.error(f'error al conectar con el host {host}')
	logging.warning(f'{user} no es un usuario seguro')
	logging.info('Info desde loggers.py')
	logging.debug('El programa alcanzo el punto de ejecucion')

if __name__ == '__main__':
	main()