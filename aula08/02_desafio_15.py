# Crie uma classe que modele o objeto "carro".
# Um carro tem os seguintes atributos: ligado, cor, modelo, velocidade.
# Um carro tem os seguintes comportamentos: liga, desliga, acelera, desacelera.

class Carro:
    
    def __init__(self):
        self.ligado = False
        self.cor = "Cinza"
        self.modelo = "Fusca"
        self.velocidade = 0

    def ligar(self):
        self.ligado = True
    
    def desligar(self):
        if self.velocidade == 0:
            self.ligado = False
        else:
            return 'Carro em movimento! Desacelere para desligar.'
    
    def acelerar(self, num):
        if self.ligado:
            if self.velocidade < 160:
                self.velocidade += num
                if self.velocidade >= 161:
                    self.velocidade = 160
                    print('Velocidade máxima de 160km/h atingida.')
                else:
                    print(f'A velocidade atual é de {self.velocidade}Km/h')
            else:
                print('Velocidade máxima atingida.')
        else:
            return 'Carro desligado. Ligue-o para acelerar.'

    def desacelerar(self, num):
        if self.ligado:
            if self.velocidade > 0:
                self.velocidade -= num
                if self.velocidade < 0:
                    self.velocidade = 0
                    print('Velocidades negativas não são permitidas. O Carro agora está parado.')
                else:
                    print(f'A velocidade atual é de {self.velocidade}Km/h')
        else:
            return 'O carro está desligado e sua velocidade é nula.'
    
    def __str__(self) -> str:
        if self.ligado:
            if self.velocidade == 0:
                info = f"INFO: {self.modelo} da cor {self.cor} está ligado e parado."
            else:
                info = f"INFO: {self.modelo} da cor {self.cor} está ligado e a {self.velocidade} Km/h"
        else:
            info = f"INFO: {self.modelo} da cor {self.cor} está desligado."
        return info


# Crie uma instância da classe carro.

carro_em_uso = Carro()

# Faça o carro "andar" utilizando os métodos da sua classe.
print(carro_em_uso)
carro_em_uso.ligar()
print(carro_em_uso)
carro_em_uso.acelerar(50)
# Faça o carro "parar" utilizando os métodos da sua classe.
carro_em_uso.desacelerar(160)
print(carro_em_uso)