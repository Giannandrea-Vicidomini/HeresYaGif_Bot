import requests
import dotenv
import os
from random import seed
from random import randint
import json

seed(1)

def get_gif_tenor(parameter: str):
    q = parameter.replace(" ","+").lower()
    print(q)
    key = os.environ.get("API_KEY")
    #url = f"https://api.giphy.com/v1/gifs/search?q={q}&api_key={key}"
    url = f"https://g.tenor.com/v1/search?q={q}&key={key}&limit={15}"

    res = requests.get(url)
    return res

def extract_gif_url(results):
    size = len(results)
    index = randint(0,size-1)
    gif_url = results[index]["media"][0]["gif"]["url"]
    return gif_url