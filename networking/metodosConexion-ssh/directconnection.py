
#  Direct Connection

from ssh2 import SSH, SSHConfigData, SSHConnectionError

HOSTNAME = 'google.com'
USERNAME = 'root'
PASSWORD = ''

def ssh_ex1():
	try:
		ssh = SSH()
		configs = SSHConfigData(hostname=HOSTNAME)
		ssh.connect(configs)
		return ssh.execute('ls -l')
	except SSHConnectionError as e:
		print(f'SSH error : {e} ')

def ssh_ex2():
	try:
		ssh = SSH()
		configs = SSHConfigData(
			hostname = hostname,
			username = USERNAME,
			password = PASSWORD,
			use_ssh_config = False)
		ssh.connect(configs)
		return ssh.execute('ls -l')
	except SSHConnectionError as e:
		print(f'SSH error : {e}')


if __name__ == '__main__' :
	ssh_ex1()
	ssh_ex2()