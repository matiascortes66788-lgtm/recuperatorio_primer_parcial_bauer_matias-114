def total(ventas):
    suma = 0
    indice = 0
    while indice < len(ventas):
        suma = suma + ventas[indice]
        indice += 1
    return suma

def filtrar(nombres,ventas, titulo, tipo, limite):
    if titulo != " ":
        print(titulo)
    totalventas =total(ventas)
    promedio = total / len(ventas)
    suma = 0
    cantidad = 0
    acumulado = 0
    indice = 0
    while indice < len(nombres):
        porcentaje= 0
        if totalventas != 0:
            porcentaje = ventas[indice] * 100 / totalventas
            cumple = False
            if tipo == "todo":
                cumple = True
            if tipo == "porcentaje" and porcentaje < limite:
                cumple = True
            if tipo == "cantidad" and ventas[indice] < limite:
                cumple == True
            if cumple:
                print(nombres[indice], ventas[indice], porcentaje, "%")
                suma = suma + ventas[indice]
                cantidad = cantidad + 1
                acumulado = acumulado + porcentaje
            indice += 1
        if cantidad == 0:
            print("ERROR: no hay.")
        elif tipo == "porcentaje":
            print("Acumulado:" , acumulado, "%")
        elif tipo == "cantidad":
            print("Suma:" , suma, "Cantidad:" , cantidad , "Promedio:" , suma / cantidad)
        elif tipo == "Promedio":
            print("Promedio generañ:" , promedio, "Acumulado:" , acumulado, "%")

def mostrar(nombres, ventas ,titulo):
    print(titulo)
    print("Total:" , total(ventas))
    filtrar(nombres, ventas , " ", "todo", 0)

def mayor(nombres, ventas):
    mayorventa = ventas[0]
    indice = 1
    while indice < len(ventas):
        if ventas[indice] > mayorventa:
            mayorventa = ventas[indice]
        indice += 1
    print("MAYOR")
    indice = 0
    while indice < len(nombres):
        if ventas[indice] == mayorventa:
            print(nombres[indice], mayorventa, mayorventa * 100 / total(ventas), "%")
        indice += 1

def ordenar():
    lista = ["NOA" , "NEA" , "pampeana" , "Cuyo" , "Patagonica" , "GBA"]
    indice = 0
    while indice < len(lista):
        posicion = 0
        while posicion + 1 < len(lista):
            if lista[posicion] > lista[posicion + 1]:
                lista[posicion], lista[posicion + 1] = lista[posicion + 1], lista[posicion]
            posicion += 1
        indice += 1
    print("Ordenado:" , lista)
                                        





