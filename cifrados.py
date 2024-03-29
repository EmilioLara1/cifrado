import os
# -*- coding: utf-8 -*-

# Se crea una constate de el abecedario 
abecedario=("abcdefghijklmnñopqrstuvwxyz")


# Cesar funciones


# Polybios funciones
def poCifra(mensaje):
    cifrado = ""

    for char in mensaje:
        #Mapea la matriz en 5x5 iniciando por fila y luego por columna con el alfabeto
        row = int((ord(char) - ord("a")) / 5) + 1
        col = ((ord(char) - ord("a")) % 5) + 1

        #Se recorren las filas
        if char == "k":
            row = row - 1
            col = 5 - col + 1

        # Se arregla un bug y junta en el mismo campo j y i
        elif ord(char) >= ord("j"):
            if col == 1:
                col = 6
                row = row -1
            col = col -1
        
        #Se asignan los valores y se convierten en string
        r = str(row)
        c = str(col)
        cifrado = cifrado + r + c
    return cifrado

def poDecifrar(mensaje):
    #Se crea una lista que contiene el mensaje
    mensaje1 = list(mensaje)
    decifrado = ""

    #Se divide la lista en pares para poder sacar el codigo de las letras
    for i in range (0, len(mensaje), 2):
        # Se asigna el valor de la fila y de la columna
        r = int(mensaje1[i])
        c = int(mensaje1[i+1])

        # Se agrega el 96 debido a que 
        ch = chr(((r-1) * 5 + c + 96))
        if (ord(ch)-96 >= 10):
            ch = chr(((r-1) * 5 + c + 96 + 1))
        ch1 = str(ch)
        decifrado = decifrado + ch1
    return decifrado

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
        if (opt1==2):
            print ("|--------------|")
            print ("|  Polybios    |")
            print ("|  1 Cifrar    |")
            print ("|  2 Descifrar |")
            print ("|--------------|")
            opt2=int(input("Ingrese la opción: "))

            if (opt2==1):
                #Cifrado sin espacios porque le da amsieda
                c = input("Ingrese el mensaje a cifrar sin espacios:")
                c = c.lower()
                cifra = poCifra(c)
                print("El mensaje cifrado es: ",cifra)
            if (opt2==2):
                #Decifrado
                c = input("Ingrese el mensaje a decifrar: ")
                decifrado = poDecifrar(c)
                print("El mensaje decifrado es: ",decifrado)


        #Opciones de Vigenere
        if (opt1==3):
            print ("|--------------|")
            print ("|  Vigenere    |")
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