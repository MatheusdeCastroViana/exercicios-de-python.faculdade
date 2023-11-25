import os
os.system("cls")
print("Algoritmo que recebe 20 números e imprime a metade de cada número!")
print(("-")*40)

i = 0

while i <= 20:
    num = float(input(f"Digite o {i+1}º número: "))
    r = num / 2
    print(f"A metade desse número é: {r}\n")
    input("Pressione enter para ver o próximo número: ")
    i += 1
    os.system("cls")