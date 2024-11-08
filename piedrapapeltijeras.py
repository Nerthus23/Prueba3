import random


opciones = ["piedra" , "papel" , "tijera" , "lagarto" , "Spock"]

eleccion_usuario = input("Elige piedra, papel, tijera, lagarto o Spock").lower ()

eleccion_computadora = random.choice(opciones)
print("Computadora eligió:" , eleccion_computadora)

gana_usuario = (eleccion_usuario == "tijera" and eleccion_computadora in ["papel" "lagarto"]) or (eleccion_usuario == "piedra" and eleccion_computadora in ["lagarto" "tijera"]) or (eleccion_usuario == "papel" and eleccion_computadora in ["Spock" "piedra"]) or (eleccion_usuario == "lagarto" and eleccion_computadora in ["Spock" "papel"]) or (eleccion_usuario == "Spcok" and eleccion_computadora in ["tijera" "piedra"]
                                                                                                                                                                                                                                                                                                                                                      )

if eleccion_usuario == eleccion_computadora : 
    print("Es un empate.")
elif gana_usuario:
    print("¡GANASTE!")
else:
    print("PERDISTE:(")
     