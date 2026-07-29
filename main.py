import telebot
from flask import Flask, request
import os

TOKEN = "8753696320:AAGKdqh1eaUbSgE39IP1FYwOuEuMuhhcX9w"
bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "✅ Бот работает! Ты написал /start")

@app.route('/' + TOKEN, methods=['POST'])
def webhook():
    update = telebot.types.Update.de_json(request.stream.read().decode('utf-8'))
    bot.process_new_updates([update])
    return "ok", 200

if __name__ == '__main__':
    bot.remove_webhook()
    bot.set_webhook(url='https://cortex-ai-bot.onrender.com/' + TOKEN)
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 10000)))
