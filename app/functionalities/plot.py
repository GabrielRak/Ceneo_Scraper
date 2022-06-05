import os.path 
import matplotlib.pyplot as plt 
import json 

def make_plot(path,save_as):
    
    with open(path, 'r') as json_file:
        data = json.loads(json_file.read())

    opinion_Counter = 0
    recomendation_Counter = 0 

    for item in data:
        if item['recommendation'] == True: recomendation_Counter+=1
        opinion_Counter+=1

    colors = ['#fca103','#292f37']

    chart = plt.figure()
    chart.canvas.set_window_title('Chart of reccomendations')
    ax = chart.add_axes([0,0,1,1])
    ax.axis('equal')

    chartData = [recomendation_Counter, opinion_Counter-recomendation_Counter]
    charHeaders = ['Reccomending', 'Not Reccomending']

    ax.pie(chartData, labels = charHeaders,autopct = '%1.2f%%',shadow = True,colors = colors)

    plt.savefig(save_as)

