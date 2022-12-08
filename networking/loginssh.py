
# ssh me@localhost 'uname'

from paramiko.client import SSHClient
with SSHClient() as ssh:
	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	ssh.connect('localhost', 2222, username = 'root', password = '')
	stdin, stdout, stderr, = ssh.exec_command('uname')
	print(stdout.read())