import telebot
import os

TOKEN = "8753696320:AAHG_c4jU3tLDhz-9T72KQ_CrjKQLlnusk8"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "✅ Бот работает!")

print("Бот запущен...")
bot.polling()
