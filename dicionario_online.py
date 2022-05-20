#Importando as libs necessárias

import os
os.system('pip install requests')

import requests
import json
os.system('cls' if os.name == 'nt' else 'clear')

#Requisitando a palavra na API
word = input('Palavra: ')
request = requests.get('https://significado.herokuapp.com/v2/'+word)

os.system('cls' if os.name == 'nt' else 'clear')

#Formatando Json recebido
container = request.json()
content = (container[0])
meaning = content["meanings"]
comp = meaning[0]

#formatando saída
format = word.upper()
print('=' * 5, format, "=" * 5)
print('Significado: ' + comp)


