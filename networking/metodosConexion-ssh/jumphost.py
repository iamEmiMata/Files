
# Context Connection using Jumphost

from ssh2 import SSHTunnelContext, SSHConfigData

HOSTNAME = 'host1.example.com'
USERNAME = 'jsmith'
KEY_FILENAME = ['~/.ssh/id_rsa.host1']
CONFIGS = {
	'hostname' : HOSTNAME,
	'username' : USERNAME,
	'key_filename' : KEY_FILENAME,
	'use_ssh_config' : False
}

JUMP_HOSTNAME = 'jump1.example.com'
JUMP_USERNAME = 'jsmith'
JUMP_PASSWORD = 'password!'
JUMP_CONFIGS =  {
	'hostname' : JUMP_HOSTNAME,
	'username' : JUMP_USERNAME,
	'password' : JUMP_PASSWORD,
	'user_ssh_config' : False
}

def sshtunnelcontext_ex1():
	with SSHTunnelContext(
		SSHConfigData(hostname = JUMP_HOSTNAME),
		SSHConfigData(hostname = HOSTNAME) ) as ssh:
		return ssh.execute('ls -l')


def sshtunnelcontext_ex2():
	with SSHTunnelContext(
		SSHConfigData(**JUMP_HOSTNAME),
		SSHConfigData(CONFIGS)) as ssh:
		return ssh.execute('ls -l')


if __name__ == '__main__':
	sshtunnelcontext_ex1()
	sshtunnelcontext_ex2()