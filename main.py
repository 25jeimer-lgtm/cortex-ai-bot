import os
from flask import Flask, request
from telegram import Update, Bot
from telegram.ext import Application, CommandHandler, Dispatcher

TOKEN = os.environ.get('BOT_TOKEN')
bot = Bot(token=TOKEN)
app = Flask(__name__)

# Обработчик команды /start
async def start(update, context):
    await update.message.reply_text("✅ Бот работает!")

# Создаем диспетчер и добавляем обработчик
dispatcher = Dispatcher(bot, None, use_context=True)
dispatcher.add_handler(CommandHandler("start", start))

@app.route('/' + TOKEN, methods=['POST'])
def webhook():
    if request.headers.get('content-type') == 'application/json':
        update = Update.de_json(request.get_json(force=True), bot)
        dispatcher.process_update(update)
        return 'ok', 200
    return 'error', 403

@app.route('/', methods=['GET'])
def index():
    return 'Cortex AI Bot is running!', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 10000)))
