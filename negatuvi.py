import os
os.system("cls")

def  positivo_negativo(numero1):
    if numero1 < 0:
        print("negativo")
    else:
        print("positivo")
numero1 = int(input("Digite uma numero:"))

positivo_negativo(numero1)
