# 7- Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla todos los números impares desde 1 hasta ese número separados por comas.

num = int(input("Digite un número entero positivo: "))

for i in range(0, num):
    if i % 2 != 0:
        print(i)
    else:
        continue