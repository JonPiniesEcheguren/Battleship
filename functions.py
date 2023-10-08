import numpy as np
import random
import variables as va
import time

def Bienvenida():
    usuario = input("Introduzca su nombre: ")
    print(f"Bienvenid@ al juego \"Hundir la flota\" {usuario}")

def Inicializar_tablero(fill = " "):
    tablero = np.full((10, 10), fill)
    return tablero

def Generar_b_usuario(tablero, eslora):
    while True:
        try:
            x = int(input(f"Introduzca las coordenadas \"x\" e \"y\" donde colocar el barco de eslora {eslora}. Coordenada \"x\": "))
            y = int(input("Coordenada \"y\": "))
            while True:
                orientacion = input("Introduzca la orientación \"N\", \"S\", \"E\" u \"O\" en la que colocar el barco: ")
                if orientacion == "N":
                    limitexn = x - eslora
                    j = x
                    break
                elif orientacion == "S":
                    limitexs = x + eslora
                    j = x
                    break
                elif orientacion == "E":
                    limiteye = y + eslora
                    j = y
                    break
                elif orientacion == "O":
                    limiteyo = y - eslora
                    j = y
                    break
                else:
                    print("Orientación errónea.")
                    pass
            if x >= (eslora-1) and orientacion == "N":
                while j > limitexn:
                    if tablero[j][y] == "O":
                        print("No es posible colocar el barco. Ya existe un barco ocupando estas posiciones")
                        break
                    else: 
                        pass
                    j -= 1
                if j == limitexn:
                    cont = 0
                    while cont < eslora:
                        tablero[x-cont][y] = "O"
                        cont += 1
                    break
            elif x <= (9-(eslora-1)) and orientacion == "S":
                while j < limitexs:
                    if tablero[j][y] == "O":
                        print("No es posible colocar el barco. Ya existe un barco ocupando estas posiciones")
                        break
                    else: 
                        pass
                    j += 1
                if j == limitexs:
                    cont = 0
                    while cont < eslora:
                        tablero[x+cont][y] = "O"
                        cont += 1
                    break
            elif y <= (9-(eslora-1)) and orientacion == "E":
                while j < limiteye:
                    if tablero[x][j] == "O":
                        print("No es posible colocar el barco. Ya existe un barco ocupando estas posiciones")
                        break
                    else: 
                        pass
                    j += 1
                if j == limiteye:
                    cont = 0
                    while cont < eslora:
                        tablero[x][y+cont] = "O"
                        cont+=1
                    break
            elif y >= (eslora-1) and orientacion == "O":
                while j > limiteyo:
                    if tablero[x][j] == "O":
                        print("No es posible colocar el barco. Ya existe un barco ocupando estas posiciones")
                        break
                    else: 
                        pass
                    j -= 1
                if j == limiteyo:
                    cont = 0
                    while cont < eslora:
                        tablero[x][y-cont] = "O"
                        cont += 1
                    break
            else:
                print(f"Las coordenadas {x},{y} y la orientación {orientacion} no son correctas para la colocación de un barco de {eslora} de eslora")
                pass
        except:
            pass
    return tablero

def Disparar_usuario(tablero_mostrado, tablero_oculto):
    while True:
        try:
            x = int(input("Es tu turno. Introduzca las coordenadas \"x\" e \"y\" donde disparar. Coordenada \"x\": "))
            y = int(input("Coordenada \"y\": "))
            if tablero_mostrado[x,y] != "-" and tablero_mostrado[x,y] != "X":
                break
        except:
            pass
    if tablero_oculto[x,y] == "O":
        print("Acertaste")
        tablero_oculto[x,y] = "X"
        tablero_mostrado[x,y] = "X"
        acierto = True
    else:
        print("Fallaste")
        tablero_oculto[x,y] = "-"
        tablero_mostrado[x,y] = "-"
        acierto = False
    return tablero_mostrado, tablero_oculto, acierto

def Disparar_aleatorio(tablero_usuario):
    while True:
        x = random.randint(0,9)
        y = random.randint(0,9)
        if tablero_usuario[x,y] != "-" and tablero_usuario[x,y] != "X":
            break
    print("Es turno de la máquina")
    time.sleep(2)
    if tablero_usuario[x,y] == "O":
        print("La máquina ha acertado su disparo")
        tablero_usuario[x,y] = "X"
        acierto = True
    else:
        print("La máquina ha fallado su disparo")
        tablero_usuario[x,y] = "-"
        acierto = False
    return tablero_usuario, acierto

def Generar_b_aleatorio(tablero, eslora):
    while True:
        x = random.randint(0,9)
        y = random.randint(0,9)
        orientacion = random.choice("NSEO")
        if orientacion == "N":
            limitexn = x - eslora
            j = x
        elif orientacion == "S":
            limitexs = x + eslora
            j = x
        elif orientacion == "E":
            limiteye = y + eslora
            j = y
        elif orientacion == "O":
            limiteyo = y - eslora
            j = y
        if x >= (eslora-1) and orientacion == "N":
            while j > limitexn:
                if tablero[j][y] == "O":
                    break
                else: 
                    pass
                j -= 1
            if j == limitexn:
                cont = 0
                while cont < eslora:
                    tablero[x-cont][y] = "O"
                    cont += 1
                break
        if x <= (9-(eslora-1)) and orientacion == "S":
            while j < limitexs:
                if tablero[j][y] == "O":
                    break
                else: 
                    pass
                j += 1
            if j == limitexs:
                cont = 0
                while cont < eslora:
                    tablero[x+cont][y] = "O"
                    cont += 1
                break
        if y <= (9-(eslora-1)) and orientacion == "E":
            while j < limiteye:
                if tablero[x][j] == "O":
                    break
                else: 
                    pass
                j += 1
            if j == limiteye:
                cont = 0
                while cont < eslora:
                    tablero[x][y+cont] = "O"
                    cont+=1
                break
        if y >= (eslora-1) and orientacion == "O":
            while j > limiteyo:
                if tablero[x][j] == "O":
                    break
                else: 
                    pass
                j -= 1
            if j == limiteyo:
                cont = 0
                while cont < eslora:
                    tablero[x][y-cont] = "O"
                    cont += 1
                break
    return tablero

def Generar_barcos_aleatorios(tablero_oculto):
    while va.contBarcosEslora1 < 4:
        tablero = Generar_b_aleatorio(tablero_oculto, 1)
        va.contBarcosEslora1 += 1
    while va.contBarcosEslora2 < 3:
        tablero = Generar_b_aleatorio(tablero_oculto, 2)
        va.contBarcosEslora2 += 1
    while va.contBarcosEslora3 < 2:
        tablero = Generar_b_aleatorio(tablero_oculto, 3)
        va.contBarcosEslora3 += 1
    while va.contBarcosEslora4 < 1:
        tablero = Generar_b_aleatorio(tablero_oculto, 4)
        va.contBarcosEslora4 += 1
    return tablero

def Generar_barcos_usuario(tablero_usuario):
    for i in range(4):
        eslora = 1
        tablero_usuario = Generar_b_usuario(tablero_usuario, eslora)
        va.contadorBarcoUsuario += 1
        print(f"\nBarco número {va.contadorBarcoUsuario} de 10 colocado\n")
        print(tablero_usuario)
        print("\n")
    for i in range(3):
        eslora = 2
        tablero_usuario = Generar_b_usuario(tablero_usuario, eslora)
        va.contadorBarcoUsuario += 1
        print(f"\nBarco número {va.contadorBarcoUsuario} de 10 colocado\n")
        print(tablero_usuario)
        print("\n")
    for i in range(2):
        eslora = 3
        tablero_usuario = Generar_b_usuario(tablero_usuario, eslora)
        va.contadorBarcoUsuario += 1
        print(f"\nBarco número {va.contadorBarcoUsuario} de 10 colocado\n")
        print(tablero_usuario)
        print("\n")
    for i in range(1):
        eslora = 4
        tablero_usuario = Generar_b_usuario(tablero_usuario, eslora)
        va.contadorBarcoUsuario += 1
        print(f"\nBarco número {va.contadorBarcoUsuario} de 10 colocado\n")
        print(tablero_usuario)
        print("\n")
    return tablero_usuario

def Disparos(tablero_mostrado, tablero_oculto, tablero_usuario):
    while "O" in tablero_usuario and "O" in tablero_oculto:
        acierto = True
        while acierto:
            if "O" not in tablero_oculto:
                break
            print(f"Tablero de tu oponente\n{tablero_mostrado}")
            tablero_mostrado, tablero_oculto, acierto = Disparar_usuario(tablero_mostrado, tablero_oculto)
            print(f"Tablero de tu oponente\n{tablero_mostrado}")
        acierto = True
        if "O" not in tablero_oculto:
            acierto = False
        while acierto:
            if "O" not in tablero_usuario:
                break
            tablero_usuario, acierto = Disparar_aleatorio(tablero_usuario)
            print(f"Tablero propio\n{tablero_usuario}")
    if "O" not in tablero_usuario:
        print("La máquina ha hundido tu flota. Has pérdido")
        print(tablero_usuario)
    if "O" not in tablero_oculto:
        print("¡Has hundido la flota de la máquina!. ¡Has ganado!")
        print(tablero_oculto)