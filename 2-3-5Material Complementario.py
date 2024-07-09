#EJERCICIO I: El centro de psicología del estudiante ubicado en la ciudad de Santiago, con más de 20 años de experiencia en el área, desea generar una serie de encuestas que permitan describir el nivel de desarrollo de los alumnos, para que de esta forma puedan tomar medidas especiales según los resultados obtenidos.
"""El test consta de 12 preguntas, cada una de las cuales posee un punto.
2
Se desea crear 4 categorías:
 Usted es un alumno de buen desempeño (0 a 3 ptos)
 Usted es un alumno que puede mejorar (4 a 6 ptos)
 Usted es un alumno con algunos desafíos (7 a 9 ptos)
 Usted alumno con muchos desafíos (sobre 10 ptos"""

print("\tTest del buen estudiante")
print("Responda con una 's' si es sí o con una 'n' si es no.")
p1 = input("¿Deja para después lo que puede hacer ahora? ")
p2 = input("¿Presta atención en clases? ")
p3 = input("¿Resuelve sus dudas con el profesor? ")
p4 = input("¿Prueba sus hipótesis antes de preguntar? ")
p5 = input("¿Utiliza su tiempo libre para aprender cosas nuevas?")
p6 = input("¿Utiliza otra fuente de información para resolver dudas?")
p7 = input("¿Estudia solo un día antes de la prueba? ")
p8 = input("¿A sus amigos solo les gusta pasar el rato? ")
p9 = input("¿A menudo realiza acciones que no son importantes?")
p10 = input("¿Le gustaría no tener que trabajar? ")
p11 = input("¿Le gusta leer? ")
p12 = input("¿Le gustan las redes sociales? ")

puntosSi = 0
puntosNo = 0

if p1 == "s":
    puntosSi+= 1
if p2 == "n":
    puntosNo+= 1
if p3 == "n":
    puntosNo += 1
if p4 == "n":
    puntosNo += 1
if p5 == "n":
    puntosNo += 1
if p6 == "n":
    puntosNo += 1
if p7 == "s":
    puntosSi += 1
if p8 == "s":
    puntosSi += 1
if p9 == "s":
    puntosSi+= 1
if p10 == "s":
    puntosSi+= 1
if p11 == "n" :
    puntosNo += 1
if p12 == "s":
    puntosSi+= 1

total=puntosNo+puntosSi
if total < 4 :
    print("Usted es un alumno de buen desempeño");
if total >= 4 and total < 7 :
    print("Usted es un alumno que puede mejorar");
if total >= 7 and total < 10 :
    print("Usted es un alumno con algunos desafíos");
if total >= 10 :
    print("Usted alumno con muchos desafíos");

#EJERCICIO II: La empresa de ventas de productos tecnológicos “Chispa Divertida”, ha detectado que en su página web de ventas se han generado reclamos por parte de los clientes puesto que, al comprar productos, el sitio web no valida la información, por tanto, los clientes pagan, pero la orden de compra no se procesa por falta de datos. Por lo tanto, la empresa le solicita a usted que antes de que se procese el pago, todos los campos sean validados


print("Ingrese los siguientes datos para realizar su compra")
nombre = input("Nombre: ")
celular = input("Celular ")
print("Producto y cantidad")
producto = input("Nombre producto: ")
cantidad = input("Cantidad: ")
print("¿Está seguro que desea pagar? ")
opcion = input("('s' para si o 'n' para no): ")
if opcion == "s" :
    print()
    if nombre == "" or celular == "" or producto == "" or cantidad =="":
        print("Faltan datos por ingresar. Por favor chequee la información ingresada.")
        print(f"Nombre: {nombre}")
        print(f"Celular: {celular}")
        print(f"Producto: {producto}")
        print(f"Cantidad: {cantidad}")
        print("Vuelva a comenzar")
    else:
        print("La compra se realizó. Gracias.")
else:
    print("La compra no se realizó.")

#EJERCICIO III: a empresa eléctrica luz de la mañana, desea crear un interruptor de escalera digital, tal de que sea programable en un circuito rduino. La idea es que existan 2 interruptores del tipo On - OFF a cada extremo de una escalera o pasillo permitiendo que se pueda prender o apagar de cualquiera de los dos extremos. La lógica involucrada en esto es de un NOT XOR, es decir, la luz se prenderá sólo si ambos interruptores están en ON, o si ambos interruptores están en OFF.

interruptor1 = 1
interruptor2 = 0
if not (interruptor1 ^ interruptor2) :
    print("Prende la luz")
else:
    print("Apaga la luz")

#EJERCICIO IV: La empresa desarrolladora de juegos “El banquete”, te ha solicitado un prototipo de juego de aventuras. Tu muy emocionado comienzas a programar, puesto que tienes una gran idea que te ha seguido durante años. Dentro del juego puedes moverte a la derecha si presionas ‘d’, a la izquierda si presionas ‘a’ o hacia adelante si presionas ‘w’ Una preview del juego se aprecia en la imagen: Debes revisar si el algoritmo es correcto con respecto a las indicaciones del mismo juego

print("\tJuego: La gran aventura")
print("Puedes moverte a la derecha 'd', a la izquierda 'a' o hacia adelante 'w'")
print("\nInicia la aventura")
opcion=input("Corres hacia la montaña nevada. Un ruido te detiene. Muévete hacia algún lado): ")
if opcion == "a":
    print("Ves un gran oso que comienza a avanzar a ti")
    opcion = input("Te quedan muy quieto. Después de un momento te comienzas a deslizar hacia un lado. ")
    if opcion == "w":
        print("Te mueves un poco hacia adelante y el oso te mata")
    elif opcion == "a":
        print("Te mueves hacia la izquierda y una planta carnívora te come.")
    else: 
        print("Te mueves un poco hacia la derecha y ves un túnel que te lleva al siguiente nivel.")

elif opcion == "d": 
    print("Ves una serpiente que está a 30 centímetros de tu pie.")
    opcion = input("Te quedan muy quieto. Después de un momento te comienzas a deslizar hacia un lado. ")
    if opcion == "w":
        print("Te mueves un poco hacia adelante y la serpiente te muerde y mueres con dolor.")
    elif opcion == "a": 
        print("Te mueves hacia la izquierda y una planta carnívora de come.")
    else: 
            print("Te mueves un poco hacia la derecha y ves un túnel que te lleva al siguiente nivel.")
else : 
    print("Ves una luz que se acerca a ti")
    opcion = input("Te quedan muy quieto. Después de un momento te comienzas a deslizar hacia un lado. ")
    if opcion == "w": 
        print("Te mueves un poco hacia adelante y el túnel te lleva al siguiente nivel")
    elif opcion == "a": 
        print("Te mueves hacia la izquierda y una planta carnívora de come.")
    else:
        print("Te mueves un poco hacia la derecha y un león se abalanza contra ti y te come el cuello.")

print("Fin de la partida. Muchas gracias por jugar.")

#EJERCICIO V: La pizzeria Cesar’s Pizza, contiene una variada gama de pizzas para escoger. La pizzeria se caracteriza por tener una atención rápida y mantener sus precios más bajos que la competencia. La gerencia le solicita realizar un programa que permita calcular los costos del pedido con sus respectivos valores del neto, impuesto y total.

print("\tBienvenido a Cesar's Pizza")
print("Menu:")
print("1.- PEPPERONI")
print("2.- QUESO")
print("3.- JAMÓN")
print("4.- 4N1")
print("5.- HULA HAWAIIAN")
print("6.- ULTIMATE SUPREME")
print("7.- VEGGIE")
print("8.- 3 MEAT TREAT")
print("9.- SUPER CHEESE 4N1")
print("10.- CHICKEN BBQ")
opcion = input("Elija su pizza. Ingrese el número de la pizza deseada:")
cantidad = int(input("¿Cuantas pizzas desea?: "))
if opcion == "1":
    precio = 6000
elif opcion == "2":
    precio = 7000
elif opcion == "3":
    precio = 8000
elif opcion == "4" or opcion == "5":
    precio = 10000
elif opcion == "6":
    precio = 11000
elif opcion >= "7":
    precio = 12000

neto = precio * cantidad
iva = neto * 0.19
total = neto + iva
print(f"El neto de su pedido es {neto}")
print(f"El impuesto de su pedido es {iva}")
print(f"El total as pagar es {total}")