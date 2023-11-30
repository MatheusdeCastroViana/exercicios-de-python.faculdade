import os
os.system("cls")
print("Algoritmo de Listas Derivadas de Outras Listas!")
print(("-")*50)

lista = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

print(lista[1:10])
print(lista[8:14])
print(lista[0:15:2])
print(lista[1:16:2])
lista.sort(reverse=True)
print(lista)
lista.append(16)
lista.sort()
print(lista)
lista[6] = "alterado"
print(lista)