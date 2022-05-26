# Escreva um programa que leia o arquivo "exemplo2.csv", e converta
# os registros desse CSV para o formato JSON. Escreva um arquivo de saída
# que contenha o conteúdo em JSON.
import json, csv

with open('exemplo2.csv', 'r') as arquivo:
    leitor_csv = csv.DictReader(arquivo)
    alunos = []
    for registro in leitor_csv:
        alunos.append(registro)

with open('exemplo2.json', 'w') as arquivo:
    json.dump(alunos, arquivo)