from command import commands
from dotenv import load_dotenv
import os
import telebot

load_dotenv()


API_KEY = os.getenv('TOKEN')


wallpaperBot = telebot.TeleBot(API_KEY)


@wallpaperBot.message_handler(commands=['start'])
def start(message):

    wallpaperBot.reply_to(
        message, "Hi, I'am a wallpapers bot. Type /help to see all my commands and get satisfactory experience")
# def start(message):

#     print(message.text)
#     wallpaperBot.send_message(message.chat.id,"Hi, I'am a wallpapers bot")


@wallpaperBot.message_handler(commands=["help"])
def showCommands(message):
    wallpaperBot.reply_to(
        message, "/wallpaper - A general wallpaper(mobile,pc) \n/mobile - A mobile wallpaper \n/fantasy - fantasy wallpaper \n/future - future wallpaper \n/anime - anime wallpaper")


@wallpaperBot.message_handler(commands=["fantasy", "anime", "mobile", "wallpaper",  "future"])
def sendWallpaper(message):

    try:
        command = message.text.replace("/", "")
        wallpaperBot.send_photo(message.chat.id, commands[command]())
    except:
        wallpaperBot.reply_to(
            message, "An error has occurred. Please try again")


wallpaperBot.infinity_polling()
