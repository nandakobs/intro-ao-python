import time

# Crie um decorator que calcule o tempo de execução de uma determinada função

def tempo_de_exec(funcao):
    def contagem(c, i):
        começa = time.perf_counter()
        funcao(c, i)
        acaba = time.perf_counter()
        print(f'Busca executada em {acaba-começa:.2f}s')
    return contagem

# Aplique seu decorator na função abaixo e veja quanto tempo a busca de um mesmo valor em um set e uma lista demoram para serem executadas
@tempo_de_exec
def encontrar_item(container, item):
    return item in container

def main():
    tamanho = 1000000
    set_grande = set(range(tamanho))
    lista_grande = list(range(tamanho))
    item = 500399
    encontrar_item(set_grande, item)
    encontrar_item(lista_grande, item)

if __name__ == '__main__':
    main()