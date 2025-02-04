import tkinter as tk
import requests 
from io import BytesIO 
from PIL import Image, ImageTk 
import random

def buscarPokemon():
    nombrePokemon = entry_pokemon.get().lower()
    if not nombrePokemon:
        label_resultado.config(text="Ingresa un nombre de un pokemon antes")
        label_imagen.config(image="")
    else:
        url = f"https://pokeapi.co/api/v2/pokemon/{nombrePokemon}"

        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()

            nombre = data["name"]
            numero = data["id"]
            tipos = [tipo["type"]["name"] for tipo in data["types"]]
            estadisticas = {estad["stat"]["name"]: estad["base_stat"] for estad in data["stats"]}
            ataque = estadisticas.get("attack", "No disponible")
            velocidad = estadisticas.get("speed")
            defensa = estadisticas.get("defense")
            hp = estadisticas.get("hp")

            resultado = f"Nombre: {nombre.capitalize()}\nNúmero: {numero} \nTipo: {', '.join(tipos)} \nHP: {hp} | Ataque: {ataque} | Defensa: {defensa} | Velocidad: {velocidad}"
            
            imagen_url = data["sprites"]["front_default"]
            response_imagen = requests.get(imagen_url)
            imagen = Image.open(BytesIO(response_imagen.content))
            imagen = imagen.resize((300,300), Image.Resampling.LANCZOS)
            foto = ImageTk.PhotoImage(imagen)
            label_imagen.config(image=foto)
            label_imagen.image = foto
            button_borrar.pack() 
        else:
            resultado = "No se encontró el Pokemon, sigue cazando pokemones"
            label_imagen.config(image=None)

        label_resultado.config(text=resultado)
def buscarPokemonAzar():
    idPokemon = random.randint(1,807) 
    url = f"https://pokeapi.co/api/v2/pokemon/{idPokemon}"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        nombre = data["name"]
        numero = data["id"]
        tipos = [tipo["type"]["name"] for tipo in data["types"]]
        estadisticas = {estad["stat"]["name"]: estad["base_stat"] for estad in data["stats"]}
        ataque = estadisticas.get("attack", "No disponible")
        velocidad = estadisticas.get("speed")
        defensa = estadisticas.get("defense")
        hp = estadisticas.get("hp")

        resultado = f"Nombre: {nombre.capitalize()}\nNúmero: {numero} \nTipo: {', '.join(tipos)} \nHP: {hp} | Ataque: {ataque} | Defensa: {defensa} | Velocidad: {velocidad}"
        
        imagen_url = data["sprites"]["front_default"]
        response_imagen = requests.get(imagen_url) 
        imagen = Image.open(BytesIO(response_imagen.content))
        imagen = imagen.resize((300,300), Image.Resampling.LANCZOS)
        foto = ImageTk.PhotoImage(imagen)
        label_imagen.config(image=foto) 
        label_imagen.image = foto 
        button_borrar.pack() 
    
    else:
        resultado = "No se encontró el Pokemon, sigue cazando pokemones"
        label_imagen.config(image=None)

    label_resultado.config(text=resultado)
def botonBorrar():
    label_resultado.config(text="Borrado")
    label_imagen.config(image='')
    label_imagen.image = None
    button_borrar.pack_forget()

window = tk.Tk()
window.title("Encuentra tu Pokemon favorito")

label_pokemon = tk.Label(window)
label_pokemon.pack() 

label_titulo = tk.Label(window, text="Escribe el nombre o ID de un pokemon o busca uno al azar")
label_titulo.pack()

entry_pokemon = tk.Entry(window)
entry_pokemon.pack()

button_buscar = tk.Button(window, text="Buscar", command=buscarPokemon)
button_buscar.pack()

button_aleatorio = tk.Button(window, text="Aleatorio", command=buscarPokemonAzar)
button_aleatorio.pack()

label_resultado = tk.Label(window, text="")
label_resultado.pack()

label_imagen = tk.Label(window)
label_imagen.pack()

button_borrar = tk.Button(window, text="Borrar" ,command=botonBorrar)
window.mainloop()
