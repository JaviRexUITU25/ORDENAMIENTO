alturas = [198,159,180,170,175]
def bubble():
    for i in range(len(alturas)-1):
        for j in range(len(alturas)-1-i):
            if alturas[j] > alturas[j+1]:
                alturas[j], alturas[j+1] = alturas[j+1], alturas[j]
def saludo():
    print("-"*10+ "OPCIONES DE ORDENAMIENTO EN PYTHON" +"-"*10)
    print("1. METODO BUBBLE\n"
          "2. METODO SELECTION\n"
          "3. QUICK SORT\n"
          "4. BOGO SORT")
    option = int(input("Ingrese la opcion que desea elegir: "))
    match option:
        case 1:
            bubble()
            print(alturas)
        case 2:
            pass
        case 3:
            pass
        case 4:
            pass
        case _:
            print("Ingrese una opcion valida.")
saludo()
