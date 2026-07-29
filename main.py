import telebot
from flask import Flask, request, abort
import os

TOKEN = "8753696320:AAGKdqh1eaUbSgE39IP1FYwOuEuMuhhcX9w"
bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    return 'Cortex AI Bot is running!', 200

@app.route('/' + TOKEN, methods=['POST'])
def webhook():
    if request.headers.get('content-type') == 'application/json':
        json_string = request.get_data().decode('utf-8')
        update = telebot.types.Update.de_json(json_string)
        bot.process_new_updates([update])
        return 'ok', 200
    else:
        abort(403)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Привет! Я Cortex AI. Бот работает!")

if __name__ == '__main__':
    bot.remove_webhook()
    bot.set_webhook(url='https://cortex-ai-bot.onrender.com/' + TOKEN)
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 10000)))
