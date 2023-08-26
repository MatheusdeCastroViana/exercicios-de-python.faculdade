import os
os.system("cls")
print("Cotação de carros")
print(("-")*40)
c1 = float(input("Digite o valor do primeiro carro: "))
c2 = float(input("Digite o valor do segundo carro: "))
c3 = float(input("Digite o valor do terceiro carro: "))
c4 = float(input("Digite o valor do quarto carro: "))
m = (c1+c2+c3+c4)/4
os.system("cls")
print(f"A média do orçamento dos quatro carros ficou em: {m}")