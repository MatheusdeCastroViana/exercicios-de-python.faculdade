import os
os.system("cls")
print("Calculadora")
print(("-")*40)
n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))
operacao = float(input("""\nEscolha agora a operação
--------------------------------
Soma = Digite 1
Subtração = Digite 2
Divisão = Digite 3
Multiplicação = Digite 4\n"""))
if operacao < 0 or operacao > 5:
    print("""Opção inválida :( 
Escolha uma das opções existentes.""")
elif operacao == 1:
    resultado = n1 + n2
    print(f"O resultado é: {resultado}")
elif operacao == 2:
    resultado = n1 - n2
    print(f"O resultado é: {resultado}")    
elif operacao == 3:
    if n2 < 1:
        print("Não se pode dividir nenhum número por zero!")
    else:
        resultado = n1 / n2
        print(f"O resultado é: {resultado}")
else:
    resultado = n1 * n2
    print(f"O resultado é: {resultado}")