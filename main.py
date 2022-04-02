import requests
from bs4 import BeautifulSoup

URL = 'https://www.ceneo.pl/68112285#tab=reviews'


def main():
    page = requests.get(URL)

    bs = BeautifulSoup(page.content, 'html.parser')

    COUNTER = 1

    for opinion in bs.find_all('div',class_="user-post"):
        content = opinion.find('div',class_="user-post__text").get_text().strip()
        print(f'{COUNTER}.{content}')
        COUNTER+=1 
        if COUNTER > 10:break

if __name__ == "__main__":
    main()