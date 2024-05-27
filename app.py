from flask import Flask, render_template, request, redirect, url_for, jsonify
import requests
import random

app = Flask(__name__)

CAT_API_KEY = 'live_fArqX0s06QIhjlwfkD6mOu7a0r4W2Tm38Ply8sAXnR402wYhBTjyJ0JLW5HG4oS3'

def get_random_dog_image_and_breed():
    try:
        response = requests.get('https://dog.ceo/api/breeds/image/random')
        response.raise_for_status()
        image_url = response.json()['message']
        breed = image_url.split('/')[4]
        return image_url, breed
    except requests.RequestException as e:
        print(f"Error fetching dog image: {e}")
        return None, None

def get_random_cat_image_and_breed():
    try:
        headers = {'x-api-key': CAT_API_KEY}
        response = requests.get('https://api.thecatapi.com/v1/images/search', headers=headers)
        response.raise_for_status()
        image_data = response.json()[0]
        image_url = image_data['url']
        breeds = image_data.get('breeds', [])
        breed = breeds[0]['name'] if breeds else 'Unknown'
        return image_url, breed
    except requests.RequestException as e:
        print(f"Error fetching cat image: {e}")
        return None, None

def get_all_dog_breeds():
    try:
        response = requests.get('https://dog.ceo/api/breeds/list/all')
        response.raise_for_status()
        return response.json()['message']
    except requests.RequestException as e:
        print(f"Error fetching dog breeds: {e}")
        return {}

def get_all_cat_breeds():
    try:
        headers = {'x-api-key': CAT_API_KEY}
        response = requests.get('https://api.thecatapi.com/v1/breeds', headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Error fetching cat breeds: {e}")
        return []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/perros')
def perros():
    breeds = get_all_dog_breeds()
    return render_template('perros.html', breeds=breeds)

@app.route('/gatos')
def gatos():
    breeds = get_all_cat_breeds()
    return render_template('gatos.html', breeds=breeds)

@app.route('/juegoperro')
def juegoperro():
    image_url, correct_breed = get_random_dog_image_and_breed()
    if not image_url or not correct_breed:
        return "Error fetching dog image", 500
    all_breeds = list(get_all_dog_breeds().keys())
    options = random.sample(all_breeds, 2)
    options.append(correct_breed)
    random.shuffle(options)
    return render_template('juegoperro.html', image_url=image_url, options=options, correct_breed=correct_breed)

@app.route('/juegogato')
def juegogato():
    image_url, correct_breed = get_random_cat_image_and_breed()
    if not image_url or not correct_breed:
        return "Error fetching cat image", 500
    all_breeds = get_all_cat_breeds()
    breed_names = [breed['name'] for breed in all_breeds if breed['name'] != correct_breed]
    if len(breed_names) < 2:
        breed_names = breed_names + ['Unknown', 'Unknown']
    options = random.sample(breed_names, 2)
    options.append(correct_breed)
    random.shuffle(options)
    return render_template('juegogato.html', image_url=image_url, options=options, correct_breed=correct_breed)

if __name__ == '__main__':
    app.run(debug=True)
