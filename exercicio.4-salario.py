import os
os.system("cls")
print("Algoritmo Salário")
print(("-")*40)
s = float(input("Digite o seu salário: "))
p = float(input("Digite o seu percentual de aumento: "))
a = s * p/100
ns = s + a
os.system("cls")
print(f"Você recebeu um aumento de: {a}")
print(f"O seu salário com aumento ficou em: R${ns}")
print(("-")*40)
