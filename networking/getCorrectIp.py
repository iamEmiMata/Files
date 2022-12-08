from checkIp import check_ip

def returnCorrectIp(ipListAddress):
	correct = []

	# for ip in ipListAddress:
	# 	if check_ip(ip):
	# 		correct.append(ip)
	# return correct

	return [ip for ip in ipListAddress if check_ip(ip)]


print('\nChecking List IP Addressed....')
lista = ['1.1.1.1', '8.8.8.8', '192.168.0.1', '1.3.4', '5.5', '0.0.1']
correct = returnCorrectIp(lista)
print(correct)
