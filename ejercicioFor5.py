# Escribir un programa en el que se pregunte al usuario por una frase y una letra, y muestre por pantalla el número de veces que aparece la letra en la frase.

phrase = input("Digite una frase: ")
letter = input("Digite una letra: ")
count = 0

for x in phrase:
    if x == letter:
        count += 1
print(f"The letter '{letter}' comes out {count} times in the phrase '{phrase}'")

# Upgrade: Solo cuente las mayúsculas

print(" ")
contador = 0

for x in phrase:
    if x.isupper():
        contador += 1
print(f"Hay {contador} letras máyusculas en la frase '{phrase}'")

#Upgrade: Preguntando la letra en mayúscula
print(" ")

upper = input("Digite la letra mayúscula: ")
count2 = 0

for x in phrase:
    if x.isupper() == upper:
        count2 += 1
print(f"Hay {count2} letras máyusculas en la frase '{phrase}'")
