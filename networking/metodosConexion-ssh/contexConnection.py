
# Contex Connection

from ssh2 import SSH, SSHContext

HOSTNAME = 'host1.example.com'
USERNAME = 'jsmith'
KEY_FILENAME = ['~/.ssh.id_rsa.user']
CONFIGS = {
	'hostname' : HOSTNAME,
	'username' : USERNAME,
	'key_filename' : KEY_FILENAME,
	'use_ssh_config' : False
}


def sshContext_ex1():
	with SSHContext(**CONFIGS) as shh:
		return ssh.execute('ls -l')

def sshContext_ex2():
	with SSHContext(**CONFIGS) as ssh:
		return ssh.execute('ls -l')

if __name__ == '__main__':
	sshContext_ex1()
	sshContext_ex2()