import telebot
from flask import Flask, request, abort
import os

# Ваш токен
TOKEN = "8753696320:AAGKdqh1eaUbSgE39IP1FYwOuEuMuhhcX9w"
bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)

# Обработчик команды /start
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Привет! Я Cortex AI. Бот работает!")

# Это главный маршрут, который будет принимать запросы от Telegram
@app.route('/' + TOKEN, methods=['POST'])
def webhook():
    # Проверяем, что это точно запрос от Telegram
    if request.headers.get('content-type') == 'application/json':
        # Получаем данные и передаём их боту
        json_string = request.get_data().decode('utf-8')
        update = telebot.types.Update.de_json(json_string)
        bot.process_new_updates([update])
        return 'ok', 200
    else:
        abort(403)

# Домашняя страница для проверки, что бот жив
@app.route('/', methods=['GET'])
def index():
    return 'Cortex AI Bot is running!', 200

if __name__ == '__main__':
    # Удаляем старый вебхук и устанавливаем новый
    bot.remove_webhook()
    bot.set_webhook(url='https://cortex-ai-bot.onrender.com/' + TOKEN)
    # Запускаем сервер
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 10000)))
