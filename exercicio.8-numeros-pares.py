import os
os.system("Cls")
print("Algoritmo que lê números pares")
print(("-")*40)
num = int(input("Não digite um número par: "))

while num % 2 != 0:
    print("Muito bem, obediência é sinônimo de sabedoria!")
    print("\nPressione enter para digitar outro número: ")
    input()
    num = int(input("Não digite um número par: "))
        
print("Error...Número par digitado, desligando o sistem..")