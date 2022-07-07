import os.path
import json
# from datetime import datetime
import matplotlib.pyplot as plt

class Analyst:

    def __init__(self):
        pass


    def open_file(self,path):
        with open( path, 'r') as f:
            data = json.loads(f.read())

        return data
        
    def analyze(self, path):

        #Scrapping data
        
        opinionsCounter = 0 
        recommendations = 0  
        STARS = []  
        data = self.open_file(path)
        for item in data:
            if item['recommendation'] == True: recommendations+=1
            STARS.append(item['stars'])
            opinionsCounter+=1

        notRecommending = opinionsCounter - recommendations

        #Drawing chart

        pie_chart = plt.figure()
        pie_chart.canvas.set_window_title('Chart of recommendations')
        ax = pie_chart.add_axes([0,0,1,1])
        ax.axis('equal')


        pie_chartData = [recommendations,notRecommending]
        pie_chartHeaders = ['Recommending','Not recommending']
            
        ax.pie(pie_chartData, labels = pie_chartHeaders, autopct = '%1.2f%%',shadow = True, startangle=45)
            
        
        plt.title("How many buyers recommend this item")
        plt.show()

        #Seems to be optional for me but worth having it there in case 
        #purchaseDate = datetime.strptime(item['purchaseDate'].split()[0], '%Y-%m-%d')
        #publishDate = datetime.strptime(item['publishDate'].split()[0], '%Y-%m-%d')
        #experience = (publishDate-purchaseDate).days
 
    def show_data(self,path):

        data = self.open_file(path)

        opinions = 0
        recommendations = 0 
        stars =0
        for item in data:
            if item['recommendation'] == True: recommendations +=1
            stars+= item['stars']
            opinions+=1

        print(f'''
{round((recommendations/opinions)*100,2)} percents of buyers recommend this item
{round(stars/opinions,2)} average stars amount for this item   
        ''')