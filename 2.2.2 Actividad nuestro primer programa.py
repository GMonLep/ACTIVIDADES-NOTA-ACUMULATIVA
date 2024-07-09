#2.2.2 Actividad Nuestro Primer Programa
print ("Bienvenida/o al mundo de la programación.")
nom=input("Para comenzar, ingresa tu nombre: ") #input() --> para variables de carácter
print ("Bienvenida/o", nom)
x=int(input("Escriba un número para reemplazar la X en la ecuación: (x^2+3x+1)/4)--->"))
resultado=((x**2+3*x+1)/4)#Para hacer un número elevado a otro es n**potencia, mientras que multiplicación es sólo un *
print("El resultado es ",resultado)
print("Ahora procederemos a preguntarle sus datos personales, ",nom)

nomcomp=input("Escriba su nombre y apellido por favor: ")
rut=input("Escriba su RUT con punto y dígito verificador: ")
correo=input("Escriba su correo: ")
celular=int(input("Escriba su número de teléfono: "))
oracion= (f"NOMBRE: {nomcomp}",f"RUT: {rut}",f"CORREO: {correo}",f"FONO: {celular}") #f"cadena texto {aqui_la_variable}"
espacio='\n'
JUANCHO = espacio.join(oracion)
print(JUANCHO)
"""
Si no se pone la coma entre las variables, te sale asi:
N
O
M
B
R
E
:
B
e
t
o

"""
