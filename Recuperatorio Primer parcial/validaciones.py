def esnumero(texto):
    if len(texto) == 0:
        return False
    indice = 0
    while indice < len(texto):
        if texto[indice] < "0" or texto[indice] > "9":
            return False
        indice += 1
        return True

def anumero(texto):
    digitos = "0123456789"
    numero = 0
    indice = 0
    while indice < len(texto):
        posicion = 0
        while posicion < len(digitos):
            if texto[indice] == digitos[posicion]:
                numero = numero * 10 + posicion
            posicion += 1
        indice += 1
    return numero

def pedir(mensaje):
    while True:
        texto = input(mensaje)
        if esnumero(texto):
            return anumero(texto)
        print("ERROR: solo numeros sin menos.")
                   

