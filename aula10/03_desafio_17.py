# O banco Banco Delas é um banco moderno e eficiente, com vantagens exclusivas para clientes mulheres.
# Modele um sistema orientado a objetos para representar contas correntes em do Banco Delas seguindo os requisitos abaixo.

# 1. Cada conta corrente pode ter um ou mais clientes como titular.
# 2. O banco controla apenas o nome, o telefone e a renda mensal de cada cliente.
# 3. A conta corrente apresenta um saldo e uma lista de operações de saques e depósitos.
#    Quando a cliente fizer um saque, diminuiremos o saldo da conta corrente. Quando ela 
#    fizer um depósito, aumentaremos o saldo.
# 4. Clientes mulheres possuem em suas contas um cheque especial de valor igual à sua renda
#    mensal, ou seja, elas podem sacar valores que deixam a sua conta com valor negativo até
#    -renda_mensal.
# 5. Clientes homens por enquanto não têm direito a cheque especial.

# Para modelar seu sistema, utilize obrigatoriamente os conceitos "classe", "herança" e "polimorfismo".
# Opcionalmente, você pode também utilizar "propriedades", "encapsulamento" e "classe abstrata".

class Cliente:
    def __init__(self, nome, telefone, sexo, renda_mensal):
        self._nome = nome
        self.telefone = telefone
        self.sexo = sexo
        self.renda_mensal = renda_mensal

    def __str__(self):
        return f'Cliente: {self._nome}, Telefone: {self.telefone}, Genero: {self.genero}, Renda Mensal: {self.renda_mensal}'


class Conta_Corrente(Cliente):

	def __init__(self, genero, renda_mensal, extrato):
        super().__init__(genero)
        super().__init__(renda_mensal)
		self.saldo = 0
        self.extrato = [0, ]
		print("Bem-vindo ao banco.")

    def saldo(self):
        if self.saldo >= 0:
            print(f"Saldo: R${self.saldo}")
        else:
            print(f"Saldo: R${self.saldo}\n Cheque Especial em uso.")

    def extrato(self):
        for t in range(len(self.extrato)):
            print(t)

	def depositar(self):
		deposito = float(input("Valor a ser depositado: R$").replace(',', '.'))
		self.saldo += deposito
		print("\n Valor depositado: R$", deposito)
        self.extrato.append(f"+{deposito}")

	def sacar(self):
		saque = float(input("Valor a ser sacado: R$").replace(',', '.'))
		if self.saldo >= saque:
			self.saldo -= saque
			print("\n Você sacou: R$", saque)
            self.extrato.append(f"-{saque}")
		else:
            if self.genero == "M" and saque <= self.renda_mensal:
                self.saldo -= saque
			    print("\n Concedido Cheque Especial de: R$", saque)
                self.extrato.append(f"-{saque}")
            else:
			    print("\n Saldo Insuficiente.")
         
        
cliente01 = Cliente('Maria da Silva', 1299999999, "M", 1500)
conta = Conta_Corrente()
conta.depositar()
conta.saldo()
conta.sacar()
conta.extrato()
