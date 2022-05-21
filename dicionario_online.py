#Importando as libs necessárias

import os
os.system('pip install requests')

import requests
import json

def clean():
	os.system('cls' if os.name == 'nt' else 'clear')


clean()
#Requisitando a palavra na API
while True:
	word = input('Palavra: ').lower()
	request = requests.get('https://significado.herokuapp.com/v2/'+word)

	clean()

#Formatando Json recebido
	container = request.json()

	try:
		content = (container[0])
	except KeyError:
		print('Desculpe, não encontramos sua palavra :/')
	else:
		meaning = content["meanings"]
		comp = meaning[0]
		format = word.upper()
		print('=' * 5, format, "=" * 5)
		print('Significado: ' + comp)
	finally:
		op = input('\nDeseja tentar outra? [S/N]: ').lower()
		if op == 's':
			clean()
			pass
		if op == 'n':
			break


