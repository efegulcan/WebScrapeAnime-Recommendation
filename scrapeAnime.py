import requests
from bs4 import BeautifulSoup
import csv

def scrape_anime_data(url):
    
    response = requests.get(url)

    soup = BeautifulSoup(response.content, 'html.parser')

    table = soup.find('table', class_='top-ranking-table')

    anime_data = []

    for row in table.find_all('tr')[1:]:
     
        rank_element = row.find('td', class_='rank')
        if rank_element:
            rank = rank_element.text.strip()
        else:
            rank = 'N/A'

        title_element = row.find('div', class_='detail')
        if title_element:
            title = title_element.find('a').text.strip()
        else:
            title = 'N/A'
        
        img_tag = row.find('img', class_='lazyload')
        if img_tag and 'data-src' in img_tag.attrs:
            picture_link = img_tag['data-src']
        else:
            picture_link = 'N/A'
        
        score_element = row.find('td', class_='score')
        if score_element:
            score = score_element.text.strip()
        else:
            score = 'N/A'
        
        anime_data.append([rank, title, score, picture_link])

    return anime_data


url_1_to_50 = 'https://myanimelist.net/topanime.php'
url_51_to_100 = 'https://myanimelist.net/topanime.php?limit=50'

anime_data_1_to_50 = scrape_anime_data(url_1_to_50)
anime_data_51_to_100 = scrape_anime_data(url_51_to_100)

with open('myanimelist_top100.csv', 'w', newline='', encoding='utf-8') as top100csv:
   
    writerTop100 = csv.writer(top100csv)
    
    writerTop100.writerow(['Rank', 'Title', 'Score', 'Picture'])
  
    for data in anime_data_1_to_50:
        writerTop100.writerow(data)

    for data in anime_data_51_to_100:
        writerTop100.writerow(data)

print("Scraping and writing to CSV file completed.")
