import requests
from bs4 import BeautifulSoup

URL = 'https://www.ceneo.pl/68112285#tab=reviews'

REVIEWS = []

def Read_Page(URL):

    
    #Constans
    counter = 1
    page = requests.get(URL)
    pageDom = BeautifulSoup(page.content, 'html.parser')

    for review in pageDom.find_all('div',class_='user-post'):

        opinion_id = review['data-entry-id']
        author = review.find('span', class_='user-post__author-name').get_text().strip()
        try:
            recomendation = review.find('span',class_="user_post__author-recomendation").get_text().strip()
            if recomendation == "Polecam": recomendation = True
            else: recomendation = False
        except:
            recomendation = None
        content = review.find('div',class_='user-post__text').get_text().strip()
        stars = review.find('span', class_='user-post__score-count').get_text().strip()
        stars = float(stars.split("/").pop(0).replace(',','.'))
        publish_date = review.select("span.user-post__published > time:nth-child(1)").pop(0)['datetime']
        publish_date = publish_date.split(" ").pop(0)
        try:
            purchase_date = review.select("span.user-post__published > time:nth-child(2)").pop(0)["datetime"]
            purchase_date = purchase_date.split(" ").pop(0)
        except IndexError: 
                purchase_date = None
        useful = review.select("span[id^=votes-yes]").pop(0).text
        useful = int(useful)
        useless = review.select("span[id^=votes-no]").pop(0).text
        useless = int(useless)

        pros = review.select("div.review-feature__title--positives ~ div.review-feature__item")
        pros = [item.text.strip() for item in pros]
        pros = ", ".join(pros)

        cons = review.select("div.review-feature__title--negatives ~ div.review-feature__item")
        cons = [item.text.strip() for item in cons]
        cons = ", ".join(cons)

        singleReview ={
            'opinion_id':opinion_id,
            'author':author,
            'content':content,
            'stars':stars,
            'publish_date':publish_date,
            'purchase_date':purchase_date,
            'useful':useful,
            'useless':useless, 
            'pros':pros,
            'cons':cons
        }

        REVIEWS.append(singleReview)
        if counter > 9:break 
        counter+=1

    pagination = pageDom.find( 'div', class_='pagination')
    right_arrow = pagination.find('a', class_="pagination__next")
    if(right_arrow!=None):
        return right_arrow['href']
    else:
        return 0


def Display_Reviews():

    for review in REVIEWS:
        print(f'{review}')
        print('')


def main():

    href = Read_Page(URL)

    while True:
        
        if href != 0:
            link = 'https://www.ceneo.pl/'+href
            href = Read_Page(link)       
        else:
            break

    Display_Reviews()



if __name__ == "__main__":
    main()
