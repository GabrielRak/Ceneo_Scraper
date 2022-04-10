import requests
from bs4 import BeautifulSoup
import json 
import os.path
from functionalities import display_message

class Reader:

    def __init__(self,):
        pass

    def Read_Reviews(self,link,saveToFile):

        REVIEWS = []        

        while True:
            
            try:
                url = 'https://www.ceneo.pl/' + link + '#tab=reviews'
                response = requests.get(url)
                DOM = BeautifulSoup(response.text,'html.parser')
            except requests.exceptions.RequestException:
                display_message("Invalid URL")
                saveToFile = False
                break

            reviews  = DOM.select("div.js_product-review")
            
            for review in reviews:

                id = review['data-entry-id']
                author = review.select_one("span.user-post__author-name").text.strip()
                try:
                    recommendation = review.select_one("span.user-post__author-recomendation > em").text.strip()
                    recommendation = True if recommendation == "Polecam" else False 
                except AttributeError: 
                    recommendation = None
                stars = review.select_one("span.user-post__score-count").text.strip()
                stars = float(stars.split("/").pop(0).replace(",", "."))
                content = review.select_one("div.user-post__text").text.strip()
                publishDate = review.select_one("span.user-post__published > time:nth-child(1)")["datetime"]
                try:
                    purchaseDate = review.select_one("span.user-post__published > time:nth-child(2)")["datetime"]
                except TypeError: 
                    purchaseDate = None
                useful = review.select_one("button.vote-yes > span").text.strip()
                useful = int(useful)
                useless = review.select_one("button.vote-no > span").text.strip()
                useless = int(useless)
                adv = review.select("div.review-feature__title--positives ~ div.review-feature__item")
                adv = [item.text.strip() for item in adv]
                dis = review.select("div.review-feature__title--negatives ~ div.review-feature__item")
                dis = [item.text.strip() for item in dis]

                singleReview = {
                    "id":id,
                    "author":author,
                    "recommendation":recommendation,
                    "content":content,
                    "stars":stars,
                    "publishDate":publishDate,
                    "purchaseDate":purchaseDate,
                    "useful":useful,
                    "useless":useless,
                    "adv":adv,
                    "dis":dis,
                }

                REVIEWS.append(singleReview)

            try:
                next_page = DOM.select_one("a.pagination__next")
                link =  'https://www.ceneo.pl'+next_page["href"]
            except TypeError:
                break

        if saveToFile == True:
            filename = input("What is the nanme of the file:")
            path = "Data/"+filename+"/"+filename+"_raw_data.json"
            os.makedirs(os.path.dirname(path), exist_ok=True)
            with open(path, 'w', encoding='utf-8') as f:
                json.dump(REVIEWS,f,ensure_ascii=False,indent=4)
            display_message("Successfully downloaded data about item")
        
        return REVIEWS







