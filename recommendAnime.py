import csv
import random
import requests
from PIL import Image
from io import BytesIO

def load_anime_data(csv_file):
    anime_data = []
    with open(csv_file, 'r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            anime_data.append(row)
    return anime_data

def recommend_random_anime(anime_data):
    return random.choice(anime_data)

def display_image_from_url(url):
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
    img.show()

def main():
    anime_data = load_anime_data('myanimelist_top100.csv')
    random_anime = recommend_random_anime(anime_data)
    print("Randomly Recommended Anime:")
    print(f"Title: {random_anime['Title']}")
    print(f"Rank: {random_anime['Rank']}")
    print(f"Score: {random_anime['Score']}")
    print(f"Picture: {random_anime['Picture']}")
    display_image_from_url(random_anime['Picture'])

if __name__ == "__main__":
    main()
