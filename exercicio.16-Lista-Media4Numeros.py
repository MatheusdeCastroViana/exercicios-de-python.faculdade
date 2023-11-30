import os
os.system("cls")
print("Algoritmo Que Lê 4 Números e Mostra a Média!")
print(("-")*40)

cont = 0
lista = []

for i in range(4):
    lista.append(float(input(f"Digite o {i+1}º número: ")))
    cont = cont + 1

x = sum(lista)
media = x / cont

print(f"O número digitados foram: {lista} e a média deles é: {media}!")