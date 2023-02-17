import os

""" Se crea una constate de el abecedartio """
abecedario=("abcdefghijklmnñopqrstuvwxyz")



""" Vigenere """
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

        if (opt1==3):
            print ("|--------------|")
            print ("|  1 Cifrar    |")
            print ("|  2 Descifrar |")
            print ("|--------------|")
            opt2=int(input("Ingrese la opción: "))

            if (opt2==1):
                c = str(input("Introduce el texto a cifrar: ")).lower()    
                clave = str(input("Introduce la clave: ")).lower() 
                print (vicifrar(c, clave))
                print ()
            
            if (opt2==2):
                c = str(input("Introduce el texto a descifrar: ")).lower() 
                clave = str(input("Introduce la clave: ")).lower()
                print (videcifrar(c, clave))
                print ()
        
        if (opt1==4):
            break

if __name__ == "__main__":
    main()