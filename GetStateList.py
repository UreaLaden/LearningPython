"""This function extracts the 50 States along with their abbreviations and exports
to a csv file. Filename is user dependent"""

from bs4 import BeautifulSoup
from GetUserAgent import *
import csv
import random
import requests ,time, urllib3

def extractStates(filename):    
    
    url = f'https://abbreviations.yourdictionary.com/articles/state-abbrev.html'

    headers = {"User-agent": random.choice(HEADERS)}
    print(headers)

    proxy = random.choice(PROXIES)
    print(proxy)
    delay = random.randint(1,30)
    time.sleep(delay)

    req = requests.get(url,proxies={"https:": proxy}, headers=headers,timeout = 15)
    doc = BeautifulSoup(req.content,'html.parser')
    contents = doc.find_all('li')

    #Search HTML for everything tagged with 'p' then collect the text and add too a temporary list
    temp_states = [content.find('p').get_text() for content in contents if content.find('p') != None ]
    
    #Loop through the first 50 states of the temporary list, and split based on the '-' then 
    # add to another  temporary list    
    splitStates = [s.split('-') for s in temp_states[:50]]

    keys = [key[0] for key in splitStates]
    values = [value[1] for value in splitStates]
    
    compiledStates = {} 
    #Add the states and their abbreviations to a dictionary       
    for key in range(len(keys)):
        compiledStates.update({keys[key]:values[key]})
    
    #Loop through the dictionary and write the states and their abbreviations to a csv
    with open(filename, 'w', newline = '') as file:
        headers = ('State Name', 'Abbreviated State')
        csv_writer = csv.DictWriter(file, fieldnames=headers)
        csv_writer.writeheader()
        for k,v in compiledStates.items():
            csv_writer.writerow(
                {
                    'State Name':k,
                    'Abbreviated State': v
                }
            )
        
#extractStates('stateList.csv')
   
    

