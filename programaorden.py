alturas = [198,159,180,170,175]
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
def saludo():
    print("-"*10+ "OPCIONES DE ORDENAMIENTO EN PYTHON" +"-"*10)
def mainmenu():
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
            pass
        case 4:
            pass
        case 5:
            print("Saliendo del programa....")
        case _:
            print("Ingrese una opcion valida.")
mainmenu()
