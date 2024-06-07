import os
import sys

escolha = []
preco = []
prato = 0
pagamento = str
contador = 0
while True:
    os.system("clear")
    print("     ======== RESTAURANTE DO MOURA ========")
    print("Seja muito bem vindo, por favor escolha seu prato!")
    print("1 ------- Lasanha ------- 30,00 R$")
    print("2 ------- Pizza ------- 50,00 R$")
    print("3 ------- Milanesa ------- 20,00 R$")
    print("4 ------- Parmegiana ------- 25,00 R$")
    print("5 ------- Macarrão ------- 20,00 R$")
    print("6 ------- X-Burguer ------- 15,00 R$")
    print("7 ------- Escondidinho ------- 30,00 R$")
    print("0 ------- Exibir preço -------")
    opcao = int(input("Escolha a opção desejada usando o código no inicio de cada prato:"))
    
    match(opcao):
        case 1:
            escolha.append("Lasanha, 30 R$")
            prato += 30
            contador += 1
            print("Prato escolhido: Lasanha")
        case 2:    
            escolha.append("Pizza, 50 R$")
            prato += 50
            contador += 1
            print("Prato escolhido: Pizza")
        case 3:    
            escolha.append("Milanesa, 20 R$")
            prato += 20
            contador += 1
            print("Prato escolhido: Milanesa")
        case 4:    
            escolha.append("Parmegiana, 25 R$")
            prato += 25
            contador += 1
            print("Prato escolhido: Parmegiana")
        case 5:    
            escolha.append("Macarrão, 20 R$")
            contador += 1
            prato += 20
            print("Prato escolhido: Macarrão")
        case 6:    
            escolha.append("X-Burguer, 15 R$")
            contador += 1
            prato += 15
            print("Prato escolhido: X-Burguer")
        case 7:    
            escolha.append("Escondidinho, 30 R$")
            prato += 30
            contador += 1
            print("Prato escolhido: Escondidinho")
        case 0:
            
            break    
        case _:
            input("Número incorreto,Pressione ENTER para voltar ao menu!")
    if opcao >= 0 and opcao < 8:
        alternativa = input("Deseja pedir outro prato?")
        if alternativa == "não" or alternativa == "nao":
            break
while True:
    pagamento = input("Digite a forma de pagamento (avista ou crédito):")
    if pagamento != "avista" and pagamento != "credito":
        print("opção incorreta, tente novamente!")
    else:
        break
if pagamento == "avista":
        desconto = prato * 0.1
        precoFinal = prato - desconto
        os.system("clear")
        for i in range (contador):
            print(f"Pratos escolhidos: {escolha[i]}")
        print("Forma de pagamento: à vista")
        print(f"Desconto: {desconto}")
        print(f"Subtotal: {prato}")
        print(f"Total a pagar: {precoFinal}")
            
else:
        desconto = prato * 0.1
        precoFinal = prato + desconto
        os.system("clear")
        for i in range (contador):
            print(f"Pratos escolhidos: {escolha[i]}")
        print("Forma de pagamento: crédito")
        print(f"Acréscimo: {desconto}")
        print(f"Subtotal: {prato}")
        print(f"Total a pagar: {precoFinal}")
        

