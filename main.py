import requests
from bs4 import BeautifulSoup

URL = 'https://www.ceneo.pl/68112285#tab=reviews'
OPINIONS = []

def Read_page(URL):
    
    COUNTER = 1
    page = requests.get(URL)
    bs = BeautifulSoup(page.content, 'html.parser')

    #Reading form the first page
    for opinion in bs.find_all('div',class_='user-post'):
        content = opinion.find('div',class_='user-post__text').get_text().strip()
        OPINIONS.append(content)
        if COUNTER > 9:break 
        COUNTER+=1
    pagination = bs.find( 'div', class_='pagination')
    right_arrow = pagination.find('a', class_="pagination__next")
    if(right_arrow!=None):
        return right_arrow['href']
    else:
        return 0

def Display_Opinions():
    opinion_counter = 1

    for opinion in OPINIONS:
        print(f'{opinion_counter}.{opinion}')
        opinion_counter+=1

def main():

    href = Read_page(URL)

    while True:
        
        if href != 0:
            link = 'https://www.ceneo.pl/'+href
            href = Read_page(link)       
        else:
            break

    Display_Opinions()


if __name__ == "__main__":
    main()