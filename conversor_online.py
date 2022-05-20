import os
os.system('pip install requests')

import requests
import json

os.system('cls' if os.name == 'nt' else 'clear')

requisicao = requests.get("https://economia.awesomeapi.com.br/all/USD-BRL")

cotacao = requisicao.json()


print('*** COTAÇÃO DO DÓLAR *** ')
print('Moeda:' + cotacao['USD']['name'])
print('Moeda:' + cotacao['USD']['create_date'])
print('Valor atual: R$' + cotacao['USD']['bid'])

op = input('\nDeseja fazer cálculo de conversão agora?[S/N]: ').lower()

if op == 's':
	print('''\n***Conversor Real/Dólar***''')
	real = float(input('Digite Valor em Real: '))
	dolar = real / float(cotacao['USD']['bid'])
	print(f'Você possui USD {dolar:.2f}')
else:
	pass
