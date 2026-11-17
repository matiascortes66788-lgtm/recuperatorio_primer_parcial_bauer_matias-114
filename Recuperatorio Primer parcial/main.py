from validaciones import pedir
from ventas import mostrar , filtrar , mayor , ordenar
nombre = ["NOA" , "NEA" , "Pampeana", "Cuyo" , "Patagonica" , "GBA"]
ventas = [0,0,0,0,0,0]
cargado = False
while True:
    print("1.Cargar 2.Mostrar 3.<5% 4. <25% 5.>500 6.>3000 7.Promedio 8.Mayor 9.Basicos 10.Hard 11.Ord 0.Salir")
    opcion = pedir("Opcion: ")
    if opcion == 0:
        break
    elif opcion == 1:
        indice = 0
        while indice < len(nombre):
            ventas[indice] = pedir("Ventas " + nombre[indice] + " : ")
            indice += 1 
            cargado = True
    elif opcion == 10:
         nombre = ["PBA" , "CABA" , "La Pampa", "Tucuman" , "Mendoza" , "Chubut" , " Corrientes" , "Neuquen" , "La Rioja" , "Jujuy"]
         ventas = [1800 , 555 , 2333 , 1850 , 3999 , 777 , 1410 , 7180 , 2500 , 60]
         cargado = True
    elif opcion == 11:
        ordenar()
    elif not cargado:
        print("ERROR: primero 1 o 10. ")
    elif opcion == 2:
        mostrar(nombre , ventas , "MOSTRAR")
    elif opcion == 3:
        filtrar(nombre , ventas , "MENOS DEL 5% , "porcentaje" , 5)
                                



