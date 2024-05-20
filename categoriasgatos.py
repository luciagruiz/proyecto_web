import requests

CAT_API_BASE_URL = "https://api.thecatapi.com/v1"
API_KEY = "live_fArqX0s06QIhjlwfkD6mOu7a0r4W2Tm38Ply8sAXnR402wYhBTjyJ0JLW5HG4oS3"

def obtener_categorias_gatos(api_key):
    url = f"{CAT_API_BASE_URL}/categories"
    headers = {"x-api-key": api_key}
    response = requests.get(url, headers=headers)
    categorias = response.json()
    return categorias

if __name__ == "__main__":
    api_key = "live_fArqX0s06QIhjlwfkD6mOu7a0r4W2Tm38Ply8sAXnR402wYhBTjyJ0JLW5HG4oS3"
    categorias_gatos = obtener_categorias_gatos(api_key)
    print("Categorías de imágenes de gatos disponibles:")
    for categoria in categorias_gatos:
        print(categoria["name"])
