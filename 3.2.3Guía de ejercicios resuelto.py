import csv
import json

def clasificar_edad(edad):
    if edad >= 25:
        return "Mayor de edad"
    else:
        return "Menor de edad"

archivo_csv = "datos.csv"
archivo_json = "mayores.json"

mayores = []
with open(archivo_csv, mode='r', newline='', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        nombre = row['Nombre']
        edad = int(row['Edad'])
        comuna = row['Comuna']
        estado_edad = clasificar_edad(edad)
        print(f"Nombre: {nombre}, Edad: {edad}, Estado: {estado_edad}, Comuna: {comuna}")
        if edad >= 25:
            mayores.append({
                'Nombre': nombre,
                'Edad': edad,
                'Comuna': comuna,
                'Estado': estado_edad
            })
with open(archivo_json, mode='w', encoding='utf-8') as json_file:
    json.dump(mayores, json_file, indent=4, ensure_ascii=False)

print(f"\nSe han guardado los datos de las personas mayores o iguales a 25 años en '{archivo_json}'.")
def es_ganador(run):
    digitos_finales = run[-3:-1] + run[-1]
    return digitos_finales in ['92', '95', '84']
archivo_csv = "listadoRun.csv"
archivo_json = "ganadores.json"
ganadores = []

with open(archivo_csv, mode='r', newline='', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        run = row['run']
        nombre = row['nombre']
        if es_ganador(run):
            ganadores.append({
                'run': run,
                'nombre': nombre
            })
with open(archivo_json, mode='w', encoding='utf-8') as json_file:
    json.dump(ganadores, json_file, indent=4, ensure_ascii=False)

print(f"Se han guardado los datos de los ganadores en '{archivo_json}'.")

