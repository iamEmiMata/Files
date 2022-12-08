
# SFTP Connection

from ssh2 import SSH, SSHConfigData, SSHConnect, SSHContext 

HOSTNAME = 'example.com'

def sftp_ex1():
	ssh = SSH()
	configs = SSHConfigData(hostname = HOSTNAME)
	ssh.connect(configs)
	sftp = ssh.open_sftp()
	return sftp.listdir()


@SSHConnect(hostname = HOSTNAME)
def sftp_ex2(ssh : SSH):
	sftp = ssh.open_sftp()
	return sftp.listdir()


def sftp_ex3():
	with SSHContext(hostname = HOSTNAME) as ssh:
		sftp = ssh.open_sftp()
		return sftp.listdir()


if __name__ == '__main__':
	sftp_ex1()
	sftp_ex2()
	sftp_ex3()
