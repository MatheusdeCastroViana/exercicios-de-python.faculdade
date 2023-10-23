import os
os.system("cls")
print("Algoritmo Calculadora")
print(("-")*40)
n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))
operacao = float(input("""\nEscolha agora a operação
--------------------------------
Soma = Digite 1
Subtração = Digite 2
Divisão = Digite 3
Multiplicação = Digite 4\n"""))

match operacao:
    case 1:
        resultado = n1 + n2
        print(f"O resultado é: {resultado}")
    case 2:
        resultado = n1 - n2
        print(f"O resultado é: {resultado}")
    case 3:
        if n2 < 1:
            print("Não se pode dividir nenhum número por 0!")
        else:
            resultado = n1 / n2
            print(f"O resultado é: {resultado}")
    case 4:
        resultado = n1 * n2
        print(f"O resultado é: {resultado}")
    case _:
        print("Opção Inválida")