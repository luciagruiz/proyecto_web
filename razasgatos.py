import requests

CAT_API_BASE_URL = "https://api.thecatapi.com/v1"
API_KEY = "live_fArqX0s06QIhjlwfkD6mOu7a0r4W2Tm38Ply8sAXnR402wYhBTjyJ0JLW5HG4oS3"

def obtener_razas_gatos(api_key):
    url = f"{CAT_API_BASE_URL}/breeds"
    headers = {"x-api-key": api_key}
    response = requests.get(url, headers=headers)
    razas = response.json()
    return razas

if __name__ == "__main__":
    api_key = "live_fArqX0s06QIhjlwfkD6mOu7a0r4W2Tm38Ply8sAXnR402wYhBTjyJ0JLW5HG4oS3"
    razas_gatos = obtener_razas_gatos(api_key)
    print("Razas de gatos disponibles:")
    for raza in razas_gatos:
        print(raza["name"])
