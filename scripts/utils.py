# scripts/utils.py
import os
import requests

def save_image(url, save_path):
    response = requests.get(url)
    if response.status_code == 200:
        with open(save_path, 'wb') as f:
            f.write(response.content)
    else:
        print(f"Failed to download image: {url}")

def ensure_dir(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)
