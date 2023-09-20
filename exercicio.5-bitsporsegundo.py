import os
os.system("cls")
print("Algoritmo bits por segundo")
print(("-")*40)

b = int(input("Digite o tamanho do arquivo: "))
v = float(input("Digite a velocidade da conexão: "))
t = b/v

print(f"\n\nA quantidade de tempo que o download irá durar é: {t:.2f} por segundo")