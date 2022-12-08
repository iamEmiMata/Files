import ipaddress

def check_ip(ip):
	try:
		ipaddress.ip_address(ip)
		return True
	except ValueError as e:
		return False

ip1 = '192.168.0.1'
ip2 = '1.2.3'

print(f'Checking IP...\n{ip1}, {check_ip(ip1)}\n{ip2}, {check_ip(ip2)}')