import os.path
import json
import matplotlib.pyplot as plt

class Analyst:

    def __init__(self):
        pass

    def return_data(self,path):

        with open(path, 'r') as json_file:
            data = json.loads(json_file.read())

        if len(data) !=0:

            opinions = 0
            recommendations = 0 
            stars =0
            for item in data:
                if item['recommendation'] == True: recommendations +=1
                stars+= item['stars']
                opinions+=1

            avg_recommendations = round((recommendations/opinions)*100,2)
            avg_stars = round(stars/opinions,2)

            data = {
                "avg_recommendations":avg_recommendations,
                "avg_stars":avg_stars,
            }

        else:
            data = {
                "avg_recommendations":0,
                "avg_stars":0,
            }


        return data 