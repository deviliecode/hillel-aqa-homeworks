import requests

BASE_URL = "http://127.0.0.1:8080"
FILENAME = "Homeworks/Homework17/downloads/PIA14256~orig.jpg"

def upload_image():
    with open(FILENAME, 'rb') as f:
        files = {"image": (FILENAME.split("/")[-1], f)}
        response = requests.post(f"{BASE_URL}/upload", files=files)
    return response.status_code, response.json()

def get_uploaded_image():
    headers = {'Content-Type': 'text'}
    response = requests.get(f'{BASE_URL}/image/{FILENAME.split("/")[-1]}', headers=headers)
    return response.status_code, response.json()

def delete_uploaded_image():
    response = requests.delete(f'{BASE_URL}/delete/{FILENAME.split("/")[-1]}')
    return response.status_code, response.json()

print(upload_image())
print(get_uploaded_image())
print(delete_uploaded_image())