from dotenv import load_dotenv
import os
import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
load_dotenv()
TOKEN = os.getenv("TOKEN")
bot = telebot.TeleBot(TOKEN)
@bot.message_handler(commands=["start"])
def handle_start(message):
  print(message)
  bot.send_message(message.chat.id, "Привет!", reply_markup=keyboard())
@bot.message_handler(commands=["help"])
def handle_help(message):
  print(message)
  bot.send_message(message.chat.id, "Прив!")

def keyboard():
  markup = InlineKeyboardMarkup()
  markup.add(InlineKeyboardButton(text="Старт", callback_data="start"))
  markup.add(InlineKeyboardButton(text="Помощь", callback_data="help"))
  return markup

@bot.callback_query_handler(func=lambda call: call.data == "start")
def handle_start_button(call):
    bot.answer_callback_query(call.id)
    print("Пользователь нажал на кнопку старт")
    print(call)



bot.polling(none_stop=True, interval=0)