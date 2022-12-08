
# Decorated Connection

from ssh2 import SSH, SSHConnect

HOSTNAME = 'example.com'
USERNAME = 'user'
PASSWORD = ''
CONFIGS = {
	"hostname" : HOSTNAME,
	"username" : USERNAME,
	"password" : PASSWORD,
	"use_ssh_config": False
}

@SSHConnect(hostname = HOSTNAME)
def sshconnect_ex1(ssh : SSH):
	return ssh.execute('ls -l')


@SSHConnect(**CONFIGS)
def sshconnect_ex2(ssh : SSH):
	return ssh.execute('ls -l')

if __name__ == '__main__':
	sshconnect_ex1()
	sshconnect_ex2()