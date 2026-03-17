#8- Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla la cuenta atrás desde ese número hasta cero separados por comas.

num = int(input("Digite un número entero positivo: "))

for i in range(0, num):
    print(f"{i},")
    i -= 1