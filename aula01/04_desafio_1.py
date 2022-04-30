# 1. Peça ao seu usuário para inserir 3 dados: nome, idade e cidade.
# 2. Imprima no console uma única mensagem desejando boas vindas ao usuário.
print("Hey!\nVocê mesmo!")
nome = input("Qual é o seu nome?\n")
idade = int(input(f"Quantos anos você tem, {nome}?\n"))
cidade = input(f"{nome}, só mais uma coisinha... De qual cidade você é?\n")
print("="*10)
print(
    f"Seja bem vinde, {nome}!\nVocê acaba de completar o primeiro desafio! :)")
