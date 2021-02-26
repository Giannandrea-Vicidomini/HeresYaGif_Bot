import telebot
import dotenv
import os
from utils import gif
import re


dotenv.load_dotenv();
bot = telebot.TeleBot(os.environ.get("TOKEN"))
pattern = r":gif (.+)"
regex = re.compile(pattern,re.IGNORECASE)
counter = 50

@bot.message_handler(func = lambda message: re.search(regex,message.text))
def word_to_gif(message):
    text = message.text
    word_list = re.search(regex,text).group(1)
    res = gif.get_gif_tenor(word_list)

    if res.status_code == 200:
        res = res.json()
        res_array = res["results"]
        gif_url = gif.extract_gif_url(res_array)
        bot.send_animation(message.chat.id,gif_url)
    else:
        bot.send_message(message.chat.id,f"Error: code[{res.status_code}]")

@bot.message_handler(func = lambda message: re.search(re.compile("vince",re.IGNORECASE),message.text))
def biat_a_vicienz(message):
    global counter
    if(counter == 50):
        bot.send_message(message.chat.id,"biat a te de martì")
        counter = 0
    else:
        counter = counter +1

bot.polling(none_stop=False)