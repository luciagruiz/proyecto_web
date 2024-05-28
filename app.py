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
        breed = breeds[0]['name'] if breeds else None
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

def get_random_cat_image_for_game(max_attempts=30):
    headers = {'x-api-key': CAT_API_KEY}
    for _ in range(max_attempts):
        try:
            response = requests.get('https://api.thecatapi.com/v1/images/search', headers=headers)
            response.raise_for_status()
            data = response.json()
            
            if not data:
                print("No data returned from the API.")
                continue
            
            image_data = data[0]
            image_url = image_data['url']
            breeds = image_data.get('breeds', [])
            
            if not breeds:
                print("No breed information available. Retrying...")
                continue
            
            breed = breeds[0]['name']
            return image_url, breed
        except requests.RequestException as e:
            print(f"Error fetching random cat image: {e}")
    
    print("Failed to fetch an image with breed information after several attempts.")
    return None, None


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
    image_url, _ = get_random_cat_image_and_breed()
    return render_template('gatos.html', breeds=breeds, cat_image_url=image_url)

@app.route('/random_cat_image', methods=['POST'])
def random_cat_image():
    cat_image_url = get_random_cat_image_and_breed()
    return redirect(url_for('gatos'))

def get_breed_image(breed_id):
    try:
        headers = {'x-api-key': CAT_API_KEY}
        response = requests.get(f'https://api.thecatapi.com/v1/images/search?breed_ids={breed_id}', headers=headers)
        response.raise_for_status()
        data = response.json()
        return data[0]['url']
    except requests.RequestException as e:
        print(f"Error fetching breed image: {e}")
        return ''
    
def get_breed_info(breed_id):
    try:
        headers = {'x-api-key': CAT_API_KEY}
        response = requests.get(f'https://api.thecatapi.com/v1/breeds/{breed_id}', headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Error fetching cat breed info: {e}")
        return {}

@app.route('/gatos/<breed_id>', methods=['GET', 'POST'])
def raza(breed_id):
    breed_info = get_breed_info(breed_id)
    breed_image = get_breed_image(breed_id)
    return render_template('razagato.html', breed_info=breed_info, breed_image=breed_image)

@app.route('/generate_breed_image/<breed_id>', methods=['POST'])
def generate_breed_image(breed_id):
    breed_info = get_breed_info(breed_id)
    breed_image = get_breed_image(breed_id)
    return render_template('razagato.html', breed_info=breed_info, breed_image=breed_image)

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

@app.route('/juegogato', methods=['GET', 'POST'])
def juegogato():
    if request.method == 'POST':
        selected_breed = request.form.get('breed')
        correct_breed = request.form.get('correct_breed')
        if selected_breed == correct_breed:
            result = f"¡Correcto! La raza es {correct_breed}."
            result_class = "text-success"
        else:
            result = f"Incorrecto. La raza correcta es {correct_breed}."
            result_class = "text-danger"
    else:
        result = None
        result_class = None

    image_url, correct_breed = get_random_cat_image_for_game()
    if not image_url:
        return "Error fetching cat image", 500
    
    all_breeds = get_all_cat_breeds()
    breed_names = [breed['name'] for breed in all_breeds]
    
    if correct_breed in breed_names:
        breed_names.remove(correct_breed)
    
    options = random.sample(breed_names, 2)
    options.append(correct_breed)
    random.shuffle(options)
    
    return render_template('juegogato.html', image_url=image_url, options=options, correct_breed=correct_breed, result=result, result_class=result_class)

if __name__ == '__main__':
    app.run(debug=True)