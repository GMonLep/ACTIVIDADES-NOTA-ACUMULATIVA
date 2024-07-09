#EJERCICIO I: Analiza el siguiente código que se encuentra en desorden sintáctico
nombre= input ("Ingrese nombre empleado: ")
rut = input ("Ingrese rut empleado: ")
horasTrabajadas = int(input ("Ingrese las horas trabajadas: "))
valorPorHora = int(input("Ingrese el valor hora del empleado: "))
colacion = 5500
locomocion = 3000
resultado = (valorPorHora * horasTrabajadas)+colacion+locomocion
print(f"-----LIQUIDACIÓN EMPLEADO----")
print(f"NOMBRE EMPLEADO: {nombre}")
print(f"RUT EMPLEADO: {rut}")
print(f"MOVILIZACIÓN: {locomocion}")
print(f"ALIMENTACIÓN: {colacion}")
print(f"PAGO A EMPLEADO: {resultado}")

#EJERCICIO II: La empresa de seguridad “Seguronet” está desarrollando un sistema para facilitar la creación de contraseñas de sus usuarios. La idea central es pedir una cierta cantidad de letras o dígitos de información que maneja una persona y luego mezclarlas para generar opciones de contraseña.

nombre=input("Ingrese las 2 primeras letras de su primer nombre: ")
apellido=input("Ingrese las 2 primeras letras de su segundo apellido: ")
rut=input("Ingrese los 2 primeros números de su RUT: ")
mes=input("Ingrese las 3 letras iniciales del mes que nació: ")
ciudad=input("Las 2 últimas letras de la ciudad donde vive: ")
op1=nombre+apellido+rut+mes+ciudad
op2=nombre+rut+apellido+mes+ciudad+mes
op3=rut+nombre+mes+ciudad+apellido
op4=apellido+rut+nombre+mes+ciudad+rut
op5=ciudad+apellido+nombre+rut+mes+ciudad
print("")
print(f"Opción 1 de contraseña: {op1}")
print(f"Opción 2 de contraseña: {op2}")
print(f"Opción 3 de contraseña: {op3}")
print(f"Opción 4 de contraseña: {op4}")
print(f"Opción 5 de contraseña: {op5}")

#EJERCICIO III: La empresa de videojuegos “Retro game” está implementando el conocido juego “El gato”. Se está realizando la implementación en Python vía terminal como se presenta en la siguiente imagen. Se le solicita establecer cuál es el algoritmo correcto para generar el resultado de la imagen.

posicionA="X"
posicionB=""
posicionC=""
posicionD=""
posicionE="X"
posicionF=""
posicionG=""
posicionH=""
posicionI="X"
print("")
print("\t\t|\t\t |\t")
print(f"\t{posicionA}\t|\t{posicionB}\t |\t{posicionC}")
print("\t\t|\t\t |\t")
print("----------------------------------------------------")
print("\t\t|\t\t |\t")
print(f"\t{posicionD}\t|\t{posicionE}\t |\t{posicionF}")
print("\t\t|\t\t |\t")
print("----------------------------------------------------")
print("\t\t|\t\t |\t")
print(f"\t{posicionG}\t|\t{posicionH}\t |\t{posicionI}")
print("\t\t|\t\t |\t")
print("")

#EJERCICIO IV: El almacén, “Diego’s” en su afán de incorporar nuevas tecnologías ensus procesos de negocio, le solicita un prototipo de sistema que le permita ingresar los datos de 3 ventas del almacén. Antes de usted, el almacén le había pedido a un informático comenzar a hacer el sistema, pero este lo dejó botado. Ahora los dueños desean que usted siga con el desarrollo. ¿Cuál sería el algoritmo que permite obtener el siguiente resultado (de la imagen)?

print("Ingresar los datos de la venta")
cliente = input("Nombre del cliente: ")
precio1 = int(input("Precio del primer producto: "))
cantidad1 = int(input("Ingrese la cantidad del primer producto: "))
precio2 = int(input("Precio del segundo producto: "))
cantidad2 = int(input("Ingrese la cantidad del segundo producto: "))
precio3 = int(input("Precio del tercer producto: "))
cantidad3 = int(input("Ingrese la cantidad del tercer producto: "))
descuento = int(input("¿Cuál es el descuento?: "))
total_bruto = (precio1 * cantidad1) + (precio2 * cantidad2) + (precio2 *
cantidad2)
precio_con_descuento = round(total_bruto - (total_bruto *
descuento/100))
IVA = round(precio_con_descuento * 0.19)
print("")
print(f"Nombre del cliente: \t{cliente}")
print(f"Total bruto: \t${total_bruto}")
print(f"Total desc.: \t${precio_con_descuento}")
print(f"IVA: \t\t${IVA}")
print(f"Total: \t\t${precio_con_descuento + iva}")

#EJERCICIO V: El Art ASCII, es un medio artístico que utiliza recursos computarizados fundamentados en los caracteres de impresión del Código Estándar Estadounidense de Intercambio de Información. (Wikipedia) Debe elegir la alternativa que contiene la secuencia correcta de variables para formar la figura de Luke sobre el dromedario.

print("")
linea1 = ("   ___         |\________/)")
linea18 = ("  [_,_])       \ /        \|")
linea11 = ("/|=T=|]        /     __  __ \ ")
linea13 =("| \ ' //       |_      9   p ]\ ")
linea15 =(" | |'-'/--.    / /\ =  |   \|\ \ ")
linea16 =(" /|| <\/> |   \ | '._,   @ @)<_)")
linea21 =("| |\      |    |   \.__/(_;_)")
linea31 =("| . H     |    |       : '='|")
linea6 =(" |  | _H__/   _|       :    |")
linea7 =("  \ '.__     \   /     ; '   ;")
linea19 =("     __  '-._(_}  == .' :    ;")
linea71 =("   (___|        /   -' | :. :")
linea371 =("         [.-'      \ | \ \ ; :")
linea2 =(" .-' | |               | | ':")
linea22 =(" / |==|          \ \ / \_")
linea661 =(" / [ | '       ._\_ -._ \\")
linea517 =(" / \__) __.   - \ \ )\\")
linea81 =("/ | /.'           >>)")
linea61 =("| \ |    \ |")
linea414 =("| .'     '-. | \ /")
linea651 =("|      / / / / /")
linea51 =(" |     /")
linea41 =("")
print(linea1)
print(linea18)
print(linea11)
print(linea13)
print(linea15)
print(linea16)
print(linea21)
print(linea31)
print(linea6)
print(linea7)
print(linea19)
print(linea71)
print(linea371)
print(linea2)
print(linea22)
print(linea661)
print(linea517)
print(linea81)
print(linea61)
print(linea414)
print(linea651)
print(linea51)
print(linea41)