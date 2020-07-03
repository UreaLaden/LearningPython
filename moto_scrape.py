from bs4 import BeautifulSoup   
import requests
from time import sleep
from random import choice
from rotating_users import rotating_ua
from proxy_test import main
from urllib.request import urlopen, Request as urlrequest
import requests 


def motivate_me():
    base_url = "https://motivationping.com/"
    total_articles = []
    pages = []


    headers = rotating_ua(base_url)
    page = requests.get(base_url,headers=headers)

    while True:
        for i in range(1,24):
            url = f"{base_url}page{i}/"
            pages.append(url)
            
        for item in pages:
            page = requests.get(item)
            soup = BeautifulSoup(page.text,"html.parser")
            contents = soup.find_all("article")
        
            for content in contents:
                summary = content.find("p")
                article_url = summary.find("a")["href"]
                title = content.find(class_="entry-title")

                total_articles.append({
                    "article_title" : title.get_text(),
                    "article_summary" : summary.get_text(),
                    "article_link" : article_url,
                })
            
        container = choice(total_articles)
        topic = container['article_title']
        desc = container['article_summary']
        url = container['article_link']
        print(f"You might like this one, it's called: {topic.title()}.")
        print(f"\nSummary: \n\t{desc}")
        print(f"\n\nIf you're interested heres the link: {url}")
        break

motivate_me()
