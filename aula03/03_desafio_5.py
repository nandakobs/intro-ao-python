# Crie uma lista com 60 números começando com o valor 1 e indo até o número 60 (ou seja, o número 60 deve estar na lista).


# Imprima todos os itens da sua lista de índice par. Imprima o índice e o item.
lista = list(range(1, 61))
for i in lista:
    if i % 2 == 0:
        print(f"Índice: {i-1}  Item: {i}")
