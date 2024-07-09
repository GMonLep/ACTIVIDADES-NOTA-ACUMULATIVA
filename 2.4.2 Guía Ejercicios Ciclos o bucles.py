"""
EJERCICIO 1
Realiza construcción de un programa que deba realizar lo siguiente:
Comienza con la inicialización de variables y solicita al usuario la cantidad de bultos. Luego, utiliza un bucle FOR para procesar cada bulto, solicitando el peso al usuario y manejando posibles errores (agregar excepciones). Dependiendo del peso ingresado, acumula valores y contadores correspondientes para bultos livianos y normales. Finalmente, imprime el total a pagar por bultos livianos y normales, así como la cantidad de bultos en cada categoría.

Una empresa de transporte requiere automatizar sus procesos de cálculo para poder cobrar por la cantidad de paquetes que trae un cliente.
Para calcular el valor total a cobrar y catalogarlo para envío, requiere preguntar elpeso de cada bulto y determinar el valor según lo siguiente:

Kilos     Categoría    Valor
1 - 5      Liviana    $1,000
6 - 10     Normal     $2,000

Ejemplo:
Si un cliente ingresa 3 bultos y según sus pesos estos clasifican en 1 liviano y 2 normales, el cliente debe paga $5,000
El sistema debe mostrar lo siguiente:
1 bulto liviano $1,000
2 bultos normales $4,000
Valor total a pagar: $5,000

EJERCICIO 2
Ahora, realiza la siguiente modificación al programa anterior:
• El bucle For, debe ser reemplazado por una sentencia While, que permita
ejecutarse mientras la variable “nroBulto” sea menor o igual a la cantidad de
bultos ingresados por el usuario.
• Recuerda incluir sentencias de validación.
"""

try:
    total_bultos = int(input("Ingrese la cantidad de bultos: "))
    bultos_livianos = 0
    bultos_normales = 0
    total_pagar = 0

    for i in range(total_bultos):
        while True:
            try:
                peso = float(input(f"ingrese el peso del bulto {i+1} en kg "))
                if peso <= 0:
                    raise ValueError("el peso invalido")
                break
            except ValueError:
                print("error")
        
        if peso >= 1 and peso <= 5:
            bultos_livianos += 1
            total_pagar += 1000
            print(f"bulto {i+1} es liviano $1.000")
        elif peso > 5 and peso <= 10:
            bultos_normales += 1
            total_pagar += 2000
            print(f"bulto {i+1} es normal $2.000")
    
    print(f"{bultos_livianos} bultos livianos por un total de ${bultos_livianos * 1000}")
    print(f"{bultos_normales} bultos normals por un total de ${bultos_normales * 2000}")
    print(f"total: ${total_pagar}")
    
except ValueError:
    print("error")
except Exception:
    print("error")

"""EJERCICIO 3
Construye un programa que tenga como objetivo el solo ser referente para la utili-
zación de captura de errores por medio excepciones, el programa debe capturar
error de valores, y división por cero."""

try:
    n1 = int(input("primer numero: "))
    n2 = int(input("segundo numero: "))
    resultado = n1 / n2 
    print(f"El resultado de {n1} dividido por {n2} es: {resultado}")

except ValueError:
    print("valor invalido")
    
except ZeroDivisionError:
    print("no se divide en cero, pelmaso")
    
except Exception as e:
    print(f"error¿")