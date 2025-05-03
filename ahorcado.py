import random
import string

from palabras import lista_palabras
from vidas_restantes import vidas_diccionario_visual


def obtener(lista_palabras):
    palabra = random.choice(lista_palabras)

    while("-" in palabra or " " in palabra):
        palabra = random.choice(lista_palabras)

    return palabra.upper()    


def ahorcado():
    print("======================")
    print(" ¡Bienvenid@ al juego ")
    print("======================")

    palabra = obtener(lista_palabras)

    letras_por_adivinar = set(palabra) 
    letras_adivinadas = set()
    abecedario = set(string.ascii_uppercase)

    vidas = 7


    while(len(letras_por_adivinar) > 0 and vidas > 0):
        print(f"Te quedan {vidas} vidas y usaste estas letras: {' '.join(letras_adivinadas)}")

        lista = [letra if letra in letras_adivinadas else "-" for letra in palabra]
        print(vidas_diccionario_visual[vidas])
        print(f"Palabra: {' '.join(lista)}")

        letra_usuario = input("Elegi una letra: ").upper()

        if letra_usuario in abecedario - letras_adivinadas:
            letras_adivinadas.add(letra_usuario)

            if letra_usuario in letras_por_adivinar:
                letras_por_adivinar.remove(letra_usuario)
            else:
                vidas = vidas - 1
                print(f"\nTu letra, {letra_usuario} no esta en la palabra.")
        elif letra_usuario in letras_adivinadas:
            print("\nYa elegiste esa letra, elegi otra nueva >:C")
        else:
            print("\nLetra invalida :(")

    if vidas == 0:
        print(vidas_diccionario_visual[vidas])
        print(f"Ahorcado >:).  La palabra era: {palabra}")           
    else:
        print(f"GANASTEEEEE!!. La palabra era: {palabra}")
ahorcado()        

