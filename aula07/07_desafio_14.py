from msilib.schema import Error
import sys
import requests
import json

# Crie uma aplicação que permita ao usuário obter informações sobre um determinado feitiço.
# O usuário deve digitar o nome de um feitiço como entrada para a nossa aplicação através da
# linha de comando. Por exemplo:
# python 07_desafio_14.py Vanishing Spell
# Você deverá obeter os dados sobre o feitiço diretamente do JSON disponível em
# https://construdelas.blob.core.windows.net/intro-ao-python/feiticos.json
# Utilize a biblioteca requests para ler o JSON.
# Ao final do programa, imprima os dados sobre o feitiço que ele solicitou.
# Se o feitiço não foi encontrado, lance uma exceção.
requisito = requests.get('https://construdelas.blob.core.windows.net/intro-ao-python/feiticos.json')
arquivo = requisito.json()
arq_lower = {k.lower(): v for k, v in arquivo.items()}

procura = sys.argv

if len(procura) > 2:
    feitico = procura[1] + " " + procura[2]
else:
    feitico = procura[1]

feitico = feitico.lower()

try: 
    print(f"""
Encantamento: {arq_lower[feitico]['encantamento']}
Tipo: {arq_lower[feitico]['tipo']}
Descrição: {arq_lower[feitico]['descricao']}
Cor da Luz: {arq_lower[feitico]['cor_da_luz']}""")
except KeyError:
    print("Verifique o feitiço digitado e tente novamente.")