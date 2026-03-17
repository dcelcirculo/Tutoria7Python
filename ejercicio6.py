#6- Escribir un programa que pregunte al usuario su edad y muestre  por pantalla todos los años que ha cumplido (desde 1 hasta su edad).

age = int(input("Digite su edad: "))
anio_actual = 2026

for y in range(0, age+1):
    print(anio_actual)
    anio_actual -= 1