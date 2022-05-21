## O programa abaixo deve calcular a média dos valores digitados pelo usuário.
## No entanto, ele não está funcionando bem. Você pode consertá-lo?

def calcular_media(valores):
    tamanho = 0
    soma = 0.0
    for i, valor in enumerate(valores):
        soma += valor
        tamanho = i + 1
    media = soma / tamanho
    return media

continuar = True
valores = []
while continuar:
    valor = input('Digite um número para entrar na sua média ou "ok" para calcular o valor:')
    if valor.lower() == 'ok':
        continuar = False
    elif valor.isdigit():
        valores.append(int(valor))
    elif '.' or ',' in valor and valor.isalnum:
        valores.append(float(valor.replace(',', '.')))
    else:
        raise ValueError('Entrada inválida. Por favor, tente novamente.')

media = calcular_media(valores)
print(f'A média calculada para os valores {valores} foi de {media:.1f}')
