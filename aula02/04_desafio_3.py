# Peça para o usuário digitar a data de seu próximo aniversário no formato brasileiro

# Imprima uma mensagem dizendo quantos dias faltam para o aniversário dele

# Pergunte ao usuário se ele(a) gosta de aniversário e salve a resposta

# Pergunte ao usuário se ele(a) vai fazer festa e salve a resposta

# Imprima uma mensagem dizendo se o usuário vai ganhar presente ou não
# A regra é: o usuário só pode ganhar presente se gostar de aniversário e for fazer festa.
from datetime import datetime

user_birth = input("Quando é o seu aniversario? [DD/MM/AAAA]\n")
user_birth = datetime.strptime(user_birth, '%d/%m/%Y')
user_niver = user_birth.replace(year=datetime.now().year) - datetime.now()
print(f'\nO seu aniversário é em {user_niver.days} dias.\n')

like_niver = input("Você gosta do seu aniversario? [S/N]  ").upper().strip()
festa = input("Vai ter/teve festa esse ano? [S/N]  ").upper().strip()

if like_niver == "S" and festa == "S":
    print("\nVou te dar um presente!!")
elif like_niver == "N" and festa == "S":
    print("\nOushi, e tu faz festa mesmo sem gostar?")
else:
    print("\nPoxa, queria bolo :(")
