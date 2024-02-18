import random

# Opciones del juego
opciones = {
    1: "piedra",
    2: "papel",
    3: "tijeras",
}

# Entrada del usuario
userInput = input("Selecciona una: \n piedra: 1 \n papel: 2 \n tijeras: 3 \n ")

# Entrada aleatoria del equipo
pcInput = random.randrange(1, 3, 1)

# Comparación de las elecciones
if pcInput == userInput:
    print("Empate")
elif pcInput == 3 and userInput == 2:
    print("Sacaste: papel, el equipo sacó: tijeras, perdiste ;(")
elif pcInput == 2 and userInput == 3:
    print("Sacaste: tijeras, el equipo sacó: papel, ganaste :D")
elif pcInput == 1 and userInput == 2:
    print("Sacaste: papel, el equipo sacó: piedra, ganaste :D")
elif pcInput == 2 and userInput == 1:
    print("Sacaste: piedra, el equipo sacó: papel, perdiste ;(")

# Mostrar la elección del equipo
print(f"El equipo sacó: {opciones[pcInput]}")
