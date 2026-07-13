import requests
import random
import os

BASE_URL = "https://images-api.nasa.gov"

search_url = f"{BASE_URL}/search"
search_params = {
    "q": "Curiosity rover Mars",  # пошуковий запит
    "media_type": "image",  # тільки зображення
    "page_size": 20  # щоб було з чого вибрати
}

def get_first_nasa_id(url, params):
    response = requests.get(url, params=params)
    first_nasa_item_id = response.json()['collection']['items'][0]['data'][0]['nasa_id']
    return first_nasa_item_id

def get_last_nasa_id(url, params):
    response = requests.get(url, params=params)
    last_nasa_item_id = response.json()['collection']['items'][-1]['data'][0]['nasa_id']
    return last_nasa_item_id

def download_random_photo_of_first_item():
    asset_endpoint = f"{BASE_URL}/asset/{get_first_nasa_id(search_url, search_params)}"
    response = requests.get(asset_endpoint)
    photo_list = response.json()['collection']['items']
    random_photo = random.choice(photo_list)['href']
    photo_response = requests.get(random_photo)
    filename = random_photo.split("/")[-1]

    os.makedirs("downloads", exist_ok=True)
    filepath = os.path.join("downloads", filename)

    with open(filepath, "wb") as f:
        f.write(photo_response.content)

    return filepath

def download_random_photo_of_second_item():
    asset_endpoint = f"{BASE_URL}/asset/{get_last_nasa_id(search_url, search_params)}"
    response = requests.get(asset_endpoint)
    photo_list = response.json()['collection']['items']
    random_photo = random.choice(photo_list)['href']
    photo_response = requests.get(random_photo)
    filename = random_photo.split("/")[-1]

    os.makedirs("downloads", exist_ok=True)
    filepath = os.path.join("downloads", filename)

    with open(filepath, "wb") as f:
        f.write(photo_response.content)

    return filepath

download_random_photo_of_first_item()
download_random_photo_of_second_item()