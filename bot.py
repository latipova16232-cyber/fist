import os
import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# Настройка логирования
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# Ваша ссылка (замените на нужную)
LINK = "https://t.me/bh6hg45345t234"

# Функция для команды /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Отправляет ссылку при команде /start"""
    await update.message.reply_text(LINK)

# Основная функция
def main():
    # Получаем токен из переменной окружения
    token = "8528886056:AAG8QLcSud9-_jEqV4KU_4ePJi_xdWehQzM"
    
    if not token:
        print("Ошибка: BOT_TOKEN не установлен!")
        print("Добавьте переменную окружения BOT_TOKEN в настройках Render")
        return
    
    # Создаем приложение
    app = Application.builder().token(token).build()
    
    # Добавляем обработчик команды /start
    app.add_handler(CommandHandler("start", start))
    
    print("Бот запущен...")
    
    # Запускаем бота
    app.run_polling()

if __name__ == '__main__':
    main()
