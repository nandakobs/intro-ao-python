# 1. Pergunte ao usuário em qual cidade e o estado em que ele(a) mora

# 2. Imprima uma mensagem diga a cidade em que o usuário mora.
#    O nome da cidade deve estar todo em letras maiúsculas.

# 3. Imprima uma mensagem diga o estado em que o usuário mora.
#    O nome do estado deve estar todo em letras maiúsculas.
#    Utilize uma forma de formatação de string diferente da que foi usada no item 2.
print("Por favor nos diga a cidade e o estado do qual você está falando")
cidade = input("Cidade: ")
estado = input("Estado: ")
print("="*10)
print("TURUUUUUUM")
print("="*10)
print(f"MENSAGEM DE VOZ DA CIDADE DE {cidade.upper()}")
estado = estado.upper()
print(f"E DO ESTADO DE {estado}")
