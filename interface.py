import os 
import json
from reader import Reader
from analyst import Analyst

def display_message(message):
    print(message)
    input("Press [Enter] key to continue")

class Interface():
    
    def __init__(self,title):
        self.title = title

    def run(self):
        self.display_menu()

    def display_menu(self):

        while True:

            os.system("clear")

            print(f'''
{self.title} [Menu]
[0].Quit
[1].Check an item 
[2].Show subscribed items  
            ''')
            
            choice = input("Your choice:")
            
            try:
                if choice == '0':
                    break
                elif choice == '1':
                    reader = Reader()
                    item_url = input("Item url:")
                    data = reader.Read_Reviews(item_url,True)
                elif choice == '2':
                    
                    id = 0
                    subscribed_items = {}
                    
                    for name in os.listdir("./Data"):
                        subscribed_items[str(id)] = name
                        print(f'{id}:{name}')
                        id+=1
                        
                    
                    choice = input("Your choice:")
                    try:
                        path = "./Data/" + subscribed_items[str(choice)] + "/" + subscribed_items[str(choice)] +"_raw_data.json"
                    except KeyError:
                        display_message(f'U can choose only [1-{id-1}] items')
                        self.display_menu()
                    os.system("clear")

                    print(f'''
Your item is {subscribed_items[str(choice)]}
What do you want to do with it
1.Show average data 
2.Render chart about it recommendations
                    ''')

                    choice = input("Your choice:")

                    if choice == '1': 
                        analyst = Analyst()
                        analyst.show_data(path)
                    elif choice == '2':
                        analyst = Analyst()
                        analyst.analyze(path)
                    else:
                        display_message("There is just 2 options")
                    display_message('')
                else: 
                    display_message("Choose another option")
            except ValueError:
                    self.display_menu("Choose another option")
        




