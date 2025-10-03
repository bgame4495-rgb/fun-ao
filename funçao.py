import os
os.system("cls")

#funçao com passagem de parametros.
#criando uma funçã

def saudacao(nome, idade,altura, peso):
    os.system("cls")
    print(f"ola, {nome}! bem-vindo(a)!:")
    print(f"sua idade é {idade} anos.")
    print(f"sua altura é :{altura}metros")
    print(f"seu peso é {peso}kg")

print("solicitando dados.")
nome = input("digite o seu nome:")
idade = int(input("digite sua idade: "))
altura = float(input("Digite sua altura: "))
peso = float(input("Digite seu peso:"))
#chamando a função.

saudacao(nome,idade,altura,peso)
