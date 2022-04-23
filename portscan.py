# portscan desenvolvido nas aulas da solyd, uso didatico
# este scan só tentara se conectar com algumas portas

import socket

ports = [21,22,80,443,445,3306,25]
print('\033[32m'+'------ SCAN SIMPLES - AULAS SOLYD ------'+'\033[0;0m')
alvo = input('[+] Digite um IP/Dominio: ')

print('\033[1;31m'+'\n------ PORTAS ENCONTRADAS ------'+'\033[0;0m')
print('PORT    SERVICE   STATE')
for port in ports:
	client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	client.settimeout(0.1)
	code = client.connect_ex((alvo, port))
	if code == 0:
		print(f'{port}       {socket.getservbyport(port)}      OPEN')
print('\033[1;31m'+'--------------------------------'+'\033[0;0m')
