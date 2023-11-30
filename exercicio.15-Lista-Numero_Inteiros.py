import os
os.system("cls")
print("Algoritmo que Lê Números Inteiros e Exibe Ele com Sua Posição na Lista!")
print(("-")*80)

lista = []

for i in range(6):
    lista.append(int(input(f"Digite o {i+1}º número: ")))

for i, e in enumerate(lista):
    print(f"Índice {i} possui o valor {e}")