import requests
from bs4 import BeautifulSoup

def obtener_letra_genius(artist_name, song_title):
    # Formatear el nombre del artista y el título de la canción para la URL
    artist_name = artist_name.replace(' ', '-').lower()
    song_title = song_title.replace(' ', '-').lower()
    url = f"https://genius.com/{artist_name}-{song_title}-lyrics"

    # Realizar la solicitud GET a la página web
    response = requests.get(url)

    # Verificar si la solicitud fue exitosa
    if response.status_code == 200:
        # Analizar el contenido HTML de la página
        soup = BeautifulSoup(response.content, 'html.parser')
        # Buscar el elemento que contiene la letra de la canción
        lyrics_container = soup.find('div', {'data-lyrics-container': True})
        # Extraer y devolver la letra de la canción
        if lyrics_container:
            return lyrics_container.get_text(separator='\n').strip()
        else:
            return "No se pudo obtener la letra de la canción."
    else:
        return "No se pudo obtener la letra de la canción."

if __name__ == "__main__":
    artist = input("Ingresa el nombre del artista: ")
    song = input("Ingresa el título de la canción: ")
    letra = obtener_letra_genius(artist, song)
    print(f"\nLetra de '{song}' de {artist}:\n")
    print(letra)
    input("\n\nPresiona Enter para salir...") # Añadido para poder correr sin abrir el IDLE
