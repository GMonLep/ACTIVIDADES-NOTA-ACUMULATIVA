def validar_lista_numeros():
    while True:
        numeros_str = input("Ingrese una lista de números enteros separados por espacios: ")
        numeros = numeros_str.split() 
        
        try:
            numeros = [int(num) for num in numeros]
            return numeros
        except ValueError:
            print("Error: Por favor, ingrese solo números enteros.")

def identificar_pares_impares(lista_numeros):
    pares = []
    impares = []
    
    for num in lista_numeros:
        if num % 2 == 0:
            pares.append(num)
        else:
            impares.append(num)
    
    return pares, impares

def mostrar_resultados(pares, impares):
    print("\nNúmeros pares:")
    if pares:
        print(", ".join(map(str, pares)))
    else:
        print("No hay números pares en la lista.")
    
    print("\nNúmeros impares:")
    if impares:
        print(", ".join(map(str, impares)))
    else:
        print("No hay números impares en la lista.")

def main():
    print("Identificación de números pares e impares en una lista")
    print("------------------------------------------------------")
    lista_numeros = validar_lista_numeros()
    pares, impares = identificar_pares_impares(lista_numeros)
    mostrar_resultados(pares, impares)

if __name__ == "__main__":
    main()
