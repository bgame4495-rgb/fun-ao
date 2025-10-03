import os
os.system("cls")

pares= 0
impares = 0

def par_ou_impar(numero):

    if numero % 2 == 0: 
        print("par")
    else:
            print ("impar")

print("solicitando dados.")
numero = int(input("digite um numero: "))

#chamando a funçao
par_ou_impar(numero)
