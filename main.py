import functions as fu
import variables as va

fu.Bienvenida()

tablero_oculto = fu.Inicializar_tablero()

tablero_mostrado = fu.Inicializar_tablero("S")

tablero_usuario = fu.Inicializar_tablero("@")

print(f"\n{va.instruccionesUsuario}\n")

tablero_usuario = fu.Generar_barcos_usuario(tablero_usuario)

tablero_oculto = fu.Generar_barcos_aleatorios(tablero_oculto)

fu.Disparos(tablero_mostrado, tablero_oculto, tablero_usuario)
