import requests
from bs4 import BeautifulSoup

URL = 'https://www.ceneo.pl/68112285#tab=reviews'


def main():
    page = requests.get(URL)

    bs = BeautifulSoup(page.content, 'html.parser')

    opinion = bs.find( 'div', class_="user-post")
    content = opinion.find( 'div', class_="user-post__text").get_text().strip()
    print(content)



if __name__ == "__main__":
    main()