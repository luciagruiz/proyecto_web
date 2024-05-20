import requests

CAT_API_BASE_URL = "https://api.thecatapi.com/v1"
API_KEY = "live_fArqX0s06QIhjlwfkD6mOu7a0r4W2Tm38Ply8sAXnR402wYhBTjyJ0JLW5HG4oS3"

def obtener_imagen_aleatoria_gato():
    url = f"{CAT_API_BASE_URL}/images/search"
    headers = {"x-api-key": API_KEY}
    response = requests.get(url, headers=headers)
    imagen = response.json()[0]["url"]
    return imagen

if __name__ == "__main__":
    imagen_gato = obtener_imagen_aleatoria_gato()
    print("Imagen aleatoria de un gato:")
    print(imagen_gato)