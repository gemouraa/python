import os
import math
from dataclasses import dataclass
def logoSenai():
    os.system("cls || clear")
    print("=== SENAI === ")

def calcular_imc(peso, altura):
    return peso / math.pow(altura, 2)

def resultado_imc(imc):
    if imc < 18.5:
        resultado = "Muito magro"
    elif imc < 25:
        resultado = "Peso normal"
    elif imc < 30:
        resultado = "Sobrepeso"
    elif imc < 35:
        resultado = "Obesidade grau I"
    elif imc < 40:
        resultado = "Obesidade grau II"
    else:
        resultado = "Obesidade grau III (mórbida)"

    return resultado
class Dados:
    def __init__(self,n1:str,n2:str,n3,n4,n5,n6,n7):
        self.nomes = n1 
        self.sobrenomes =  n2
        self.nomeCompletos = n1 + n2
        self.idades = n3
        self.alturas = n4
        self.pesos = n5
        self.imcs = n6
        self.situacaoImc = n7
pesquisa = []

while True:
    logoSenai()
    nome = input("Digite o nome do usuário (ou digite 'sair' para encerrar): ")
    
    if nome.lower() == 'sair':
        break
    
    sobrenome = input("Digite o sobrenome do usuário: ")
    idade = int(input("Digite a idade do usuário: "))
    altura = float(input("Digite a altura do usuário (em metros): "))
    peso = float(input("Digite o peso do usuário (em quilogramas): "))
    imc = calcular_imc(peso, altura)
    situacao = resultado_imc(imc)
    pesquisa.append(Dados(nome,sobrenome,idade,altura,peso,imc,situacao))

    
    
logoSenai()
print("\nDados dos usuários: \n")
for i,j in enumerate(pesquisa):
    print(f"=====Usuário {i+1}:=====")
    print("Nome:", j.nomes)
    print("Sobrenome:", j.sobrenomes)
    print("Nome completo:", j.nomeCompletos)
    print("Idade:", j.idades)
    print("Altura:", j.alturas, "metros")
    print(f"Peso:{j.pesos:.1f} quilogramas")
    print(f"IMC: {j.imcs:.1f}")
    print("Resultado:", j.situacaoImc)
    print("")
    

