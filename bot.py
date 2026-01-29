import os
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# Токен вашего бота. Мы получим его из переменной окружения (безопаснее)
TOKEN = "8528886056:AAG8QLcSud9-_jEqV4KU_4ePJi_xdWehQzM"

# Ваше заготовленное сообщение
PREPARED_MESSAGE = "https://t.me/bh6hg45345t234"

# Функция-обработчик для команды /start
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(PREPARED_MESSAGE, parse_mode='Markdown')

# Функция-обработчик для ЛЮБОГО текстового сообщения
async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Отправляем наше заготовленное сообщение в ответ на любой текст
    await update.message.reply_text(PREPARED_MESSAGE, parse_mode='Markdown')

# Основная функция
def main():
    # 1. Создаем приложение и передаем токен
    app = Application.builder().token(TOKEN).build()

    # 2. Регистрируем обработчики команд
    app.add_handler(CommandHandler("start", start_command))
    
    # 3. Регистрируем обработчик для всех текстовых сообщений
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    # 4. Запускаем бота в режиме "вебхука" (для Render) или "лонг поллинга"
    # Для Render используем вебхук
    port = int(os.environ.get('PORT', 8443))
    webhook_url = os.getenv('RENDER_EXTERNAL_URL')  # Будет задан на Render
    
    if webhook_url:
        # На Render: настраиваем вебхук
        app.run_webhook(
            listen="0.0.0.0",
            port=port,
            url_path=TOKEN,
            webhook_url=f"{webhook_url}/{TOKEN}"
        )
    else:
        # Для локального тестирования (если нужно)
        print("Бот запущен в режиме опроса...")
        app.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == '__main__':

    main()


