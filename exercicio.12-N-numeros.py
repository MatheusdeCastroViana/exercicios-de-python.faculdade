import os
os.system("cls")
print("Algoritmo que recebe N números e imprime o quadrado de cada número.")
print(("-")*40)

N = int(input("Digite o número de vezes que você quer calcular o quadrado dos números: "))

for i in range(N):
    num = int(input(f"Digite o {i+1}º número: "))
    q = num * num
    print(f"O quadrado do número {num} é: {q}\n")