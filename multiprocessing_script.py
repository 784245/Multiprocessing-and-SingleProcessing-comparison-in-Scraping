import pandas as pd
import requests
import time
from bs4 import BeautifulSoup
import multiprocessing


def scrape_url(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        price = soup.find('span', {'itemprop': 'price'}).get_text().strip()
        return (url, price)
    except Exception as e:
        return (url, str(e))
def scraping():
    start_time = time.time()
    df = pd.read_csv('AbenandCole_products.csv')
    urls = df['URL'].tolist()
    with multiprocessing.Pool(processes=8) as pool:
        results = pool.map(scrape_url, urls)
    for url, price in results:
        print(f'URL: {url}  Price:  {price}')

    end_time = time.time()
    total_time = end_time - start_time
    return total_time

if __name__ == "__main__":
    time_taken = scraping()
    print(f'Time taken in Multiprocessing: {time_taken / 60:.2f} minutes')
