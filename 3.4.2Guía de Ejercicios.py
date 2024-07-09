
informacion = ("Juan", 30, "Ciudad de México")
print("Nombre:", informacion[0])
print("Edad:", informacion[1])
print("Ciudad de residencia:", informacion[2])
nombre, edad, ciudad = informacion
print("\nDesempaquetado de tupla:")
print("Nombre:", nombre)
print("Edad:", edad)
print("Ciudad de residencia:", ciudad)

numeros = tuple(range(1, 11))
suma_numeros = sum(numeros)
print("\nSuma de los números:", suma_numeros)

maximo = max(numeros)
minimo = min(numeros)
print("Valor máximo:", maximo)
print("Valor mínimo:", minimo)

veces_numero_5 = numeros.count(5)
print("Número de veces que aparece el 5:", veces_numero_5)
letras = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j')

primeras_cinco = letras[:5]
print("\nPrimeras 5 letras:", primeras_cinco)

ultimas_tres = letras[-3:]
print("Últimas 3 letras:", ultimas_tres)

cada_segunda_letra = letras[::2]
print("Cada segunda letra:", cada_segunda_letra)
