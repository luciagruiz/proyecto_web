from flask import Flask, render_template, request, redirect, url_for, jsonify
import requests
import random

app = Flask(__name__)

CAT_API_KEY = 'live_fArqX0s06QIhjlwfkD6mOu7a0r4W2Tm38Ply8sAXnR402wYhBTjyJ0JLW5HG4oS3'

def get_random_dog_image():
    response = requests.get('https://dog.ceo/api/breeds/image/random')
    return response.json()['message']

def get_random_cat_image():
    headers = {'x-api-key': CAT_API_KEY}
    response = requests.get('https://api.thecatapi.com/v1/images/search', headers=headers)
    return response.json()[0]['url']

def get_all_dog_breeds():
    response = requests.get('https://dog.ceo/api/breeds/list/all')
    return response.json()['message']

def get_all_cat_breeds():
    headers = {'x-api-key': CAT_API_KEY}
    response = requests.get('https://api.thecatapi.com/v1/breeds', headers=headers)
    return response.json()

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
    breeds = list(get_all_dog_breeds().keys())
    correct_breed = random.choice(breeds)
    image_url = get_random_dog_image()
    options = random.sample(breeds, 3)
    if correct_breed not in options:
        options[random.randint(0, 2)] = correct_breed
    return render_template('juegoperro.html', image_url=image_url, options=options, correct_breed=correct_breed)

@app.route('/juegogato')
def juegogato():
    breeds = get_all_cat_breeds()
    correct_breed = random.choice(breeds)
    image_url = get_random_cat_image()
    options = random.sample([breed['name'] for breed in breeds], 3)
    if correct_breed['name'] not in options:
        options[random.randint(0, 2)] = correct_breed['name']
    return render_template('juegogato.html', image_url=image_url, options=options, correct_breed=correct_breed['name'])

if __name__ == '__main__':
    app.run(debug=True)
