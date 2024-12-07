from bs4 import BeautifulSoup
import pandas as pd
import requests, time

def scraping():
    start_time=time.time()
    df=pd.read_csv('AbenandCole_products.csv')
    for url in df['URL'].tolist():
        try:
            response = requests.get(url)
            soup = BeautifulSoup(response.content, 'html.parser')
            price = soup.find('span', {'itemprop': 'price'}).get_text().strip()
        except Exception as e:
            price=None
        print(f'URL: {url}  Price:  {price} ')

    end_time=time.time()

    total_time=end_time-start_time

    return total_time

time_taken=scraping()
print(f'Time taken in Single Processing : {time_taken / 60:.2f} minutes')