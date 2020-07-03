from pyfiglet import figlet_format
from colorama import init
from termcolor import colored
init()
import requests
from random import choice


def dad_joke4000(*args):
    url = "https://icanhazdadjoke.com/search"
    header = figlet_format("Dad Joke 4000")
    header = colored(header, color = "green")
    print(header)
    user_request = input("Let me tell you a joke! Give me a topic: ")
    res = requests.get(
    url,
     headers={"Accept" : "Application/json"},
     params= {"term" : user_request}
     ).json()

    num_jokes = (res["total_jokes"])
    results = res["results"]
    if num_jokes > 1:
        print(f"We have {num_jokes} jokes about {user_request}'s!")
        print(f"Here's one of them: \n")
        print(choice(results)['joke'])
    elif num_jokes == 1:
        result = (res["results"][0]['joke'])
        print(f"\nLucky you we have {num_jokes} joke about {user_request}'s \n")
        print(f"Here it is: \n\t{result} \n")
    
    else:
        print(f"\nSorry couldn't find any jokes about {user_request} ")
        

dad_joke4000()

    




