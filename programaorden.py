alturas = [198,159,180,170,175,160,161,195,185,156]
def bubble():
    for i in range(len(alturas)-1):
        for j in range(len(alturas)-1-i):
            if alturas[j] > alturas[j+1]:
                alturas[j], alturas[j+1] = alturas[j+1], alturas[j]
def selection():
    for i in range(len(alturas)):
        min_index = i
        for j in range(i + 1, len(alturas)):
            if alturas[j] < alturas[min_index]:
                min_index = j
        alturas[i], alturas[min_index] = alturas[min_index], alturas[i]
def quicksort(lista):
    if len(lista) <= 1:
        return lista
    pivote =lista[len(lista)//2]
    menores =[x for x in lista if x < pivote]
    iguales =[x for x in lista if x == pivote]
    mayores =[x for x in lista if x > pivote]
    return quicksort(menores) + iguales + quicksort(mayores)
import random
def lista_ordenada(lista):
    return all(lista[i] <= lista[i+1] for i in range(len(lista)-1))
def bogo(lista):
        intentos = 0
        while not lista_ordenada(lista):
            random.shuffle(lista)
            intentos +=1
        print(f"Ordenada despues de {intentos} intentos")
        return lista
def saludo():
    print("-"*10+ "OPCIONES DE ORDENAMIENTO EN PYTHON" +"-"*10)
def mainmenu():
    while True:
        print("1. METODO BUBBLE\n"
              "2. METODO SELECTION\n"
              "3. QUICK SORT\n"
              "4. BOGO SORT\n"
              "5. SALIR")
        option = int(input("Ingrese la opcion que desea elegir: "))
        match option:
            case 1:
                print("ALTURAS ORIGINALES: ", alturas)
                bubble()
                print("ALTURAS ORDENADAS: ", alturas)
            case 2:
                print("ALTURAS ORIGINALES: ", alturas)
                selection()
                print("ALTURAS ORDENADAS: ", alturas)
            case 3:
                print("ALTURAS ORIGINALES: ", alturas)
                print("ALTURAS ORDENADAS: ", quicksort(alturas))
            case 4:
                print("ALTURAS ORIGINALES:", alturas)
                print("ALTURAS ORDENADAS: ", bogo(alturas))
            case 5:
                print("Saliendo del programa....")
                break
            case _:
                print("Ingrese una opcion valida.")
mainmenu()
