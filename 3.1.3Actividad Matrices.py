
def crear_y_mostrar_matriz():
    matriz = []
    for i in range(3):
        fila = []
        for j in range(4):
            elemento = int(input(f"Ingrese el elemento para la posición [{i}][{j}]: "))
            fila.append(elemento)
        matriz.append(fila)
    
    print("Matriz:")
    for fila in matriz:
        for elemento in fila:
            print(elemento, end=" ")
        print()
crear_y_mostrar_matriz()

def contar_elementos_color():
    arreglo = [
        [["amarillo", "rojo", "Naranja"], ["Verde", "Blanco", "rojo"], ["amarillo", "Verde", "Blanco"]],
        [["Blanco", "rojo", "Naranja"], ["amarillo", "Verde", "Blanco"], ["Naranja", "rojo", "amarillo"]],
        [["Verde", "Naranja", "rojo"], ["amarillo", "Blanco", "Verde"], ["Naranja", "Blanco", "rojo"]]
    ]
    
    conteo = {"amarillo": 0, "rojo": 0, "Naranja": 0, "Verde": 0, "Blanco": 0}
    for i in range(3):
        for j in range(3):
            for k in range(3):
                color = arreglo[i][j][k]
                if color in conteo:
                    conteo[color] += 1
    
    for color, cantidad in conteo.items():
        print(f"Número de elementos {color}: {cantidad}")

contar_elementos_color()
def simular_bus():
    asientos = []
    numero_asiento = 1
    for i in range(10):
        fila = []
        for j in range(4):
            fila.append(numero_asiento)
            numero_asiento += 1
        asientos.append(fila)
    print("Asientos del bus:")
    for fila in asientos:
        for asiento in fila:
            print(asiento, end=" ")
        print()

simular_bus()
