import random
numero_secreto = random.randint(1, 10)
adivinanza = int(input("Adivina un número entre 1 y 10"))
if adivinanza == numero_secreto: 
    print("¡CORRECTO!")
else: 
    print("Incorrecto, el número era:", numero_secreto)



