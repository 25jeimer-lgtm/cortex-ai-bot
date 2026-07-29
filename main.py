import os
import json
from flask import Flask, request
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = os.environ.get('BOT_TOKEN')
app = Flask(__name__)

# Создаём приложение (без запуска поллинга)
application = Application.builder().token(TOKEN).build()

# Обработчик команды /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("✅ Бот работает!")

# Регистрируем команду
application.add_handler(CommandHandler("start", start))

# Вебхук для Flask
@app.route('/' + TOKEN, methods=['POST'])
def webhook():
    try:
        data = request.get_json(force=True)
        update = Update.de_json(data, application.bot)
        application.process_update(update)
        return 'ok', 200
    except Exception as e:
        print(f"Error: {e}")
        return 'error', 403

@app.route('/', methods=['GET'])
def index():
    return 'Cortex AI Bot is running!', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 10000)))
