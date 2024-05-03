import telebot

TOKEN = ""
bot - telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message)
...bot

@bot.message_handler(commands=['help'])
def help(message):
...

#Handle the /courses commands
bot.message_handler(commands=['courses'])
def courses(message):
...



