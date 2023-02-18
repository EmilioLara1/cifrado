import os
# -*- coding: utf-8 -*-

# Se crea una constate de el abecedario 
abecedario=("abcdefghijklmnñopqrstuvwxyz")

# Cesar funciones


# Polybios funciones



# Vigenere funciones
def vicifrar(mensaje, key):
    cifrado = ""
    i = 0
    for letra in mensaje: 
        suma = abecedario.find(letra) + abecedario.find(key[i % len(key)])
        modulo = int(suma) % len(abecedario)
        cifrado = cifrado + str(abecedario[modulo]) 
        i = i + 1
    return cifrado

def videcifrar(mensaje,key):
    cifrado = ""
    i = 0
    for letra in mensaje:
        suma = abecedario.find(letra) - abecedario.find(key[i % len(key)])  
        modulo = int(suma) % len(abecedario)
        cifrado = cifrado + str(abecedario[modulo])  
        i = i + 1
    return cifrado


def main():
    while True:
        print ("|---------------------------------------|")
        print ("|¿Que método de cifrado quiere utilizar?|")
        print ("|              1  Cesar                 |")
        print ("|              2 Polybios               |")
        print ("|              3 Vigenére               |")
        print ("|              4  Salir                 |")
        print ("|---------------------------------------|")
        opt1=int(input("Ingrese la opción: "))

        #Opciones de Cesar


        # Opciones de Polybios

        #Opciones de Vigenere
        if (opt1==3):
            print ("|--------------|")
            print ("|  1 Cifrar    |")
            print ("|  2 Descifrar |")
            print ("|--------------|")
            opt2=int(input("Ingrese la opción: "))

            # Cifrado 
            if (opt2==1):
                # Se le pide al usuario el texto que desea cifrar 
                c = str(input("Ingrese el mensaje a cifrar: ")).lower()

                # Se le pide la clave de cifrado #  
                clave = str(input("Introduce la clave: ")).lower() 
                print ("Mensaje cifrado: ", vicifrar(c, clave))
            
            # Decifrado 
            if (opt2==2):
                #Se le pide al usuario el texto que desea decifrar 
                c = str(input("Introduce el texto a descifrar: ")).lower()

                # Se le pide la clave de cifrado, debe de ser la misma que la de cifrado 
                clave = str(input("Introduce la clave: ")).lower()
                print ("Mensaje decifrado:", videcifrar(c, clave))
        
        if (opt1==4):
            break

if __name__ == "__main__":
    main()