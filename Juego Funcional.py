from random import randint
intentos= 0
estimado= 0
numero_secreto= randint(1,100)
nombre=input("Inserte su nombre: ")

print(f"bueno {nombre}, he pensado un numero entre 1 y 100\n tienes 8 intentos para adivinar")

while intentos < 8:
    estimado = int(input("¿cual es el numero?"))
    intentos += 1
    if estimado not in range(1,101):
        print("Tu numero no se encuentra entre el rango 1-100")
    if estimado < numero_secreto:
        print("mi numero es mas alto")
    elif estimado > numero_secreto:
        print("mi numero es mas bajo")
    else:
        print(f"felicitaciones {nombre}! Has acertado en {intentos} intentos!")
        break




if estimado != numero_secreto:
    print(f"Lo siento {nombre}, se han agotado los intentos.\n El numero secreto era {numero_secreto}")


