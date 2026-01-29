import os
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters

# Функция для команды /start
async def start(update: Update, context):
    await update.message.reply_text('Привет! Бот работает.')

# Основная функция
def main():
    # Получаем токен из переменных окружения
    token = os.getenv('TELEGRAM_BOT_TOKEN')
    
    if not token:
        print("ОШИБКА: Не найден TELEGRAM_BOT_TOKEN")
        return
    
    # Создаем приложение
    app = Application.builder().token(token).build()
    
    # Регистрируем обработчики команд
    app.add_handler(CommandHandler("start", start))
    
    # Запускаем бота
    print("Бот запускается...")
    app.run_polling()

if __name__ == '__main__':
    main()
