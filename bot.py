import os
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Токен вашего бота
TOKEN = "8528886056:AAG8QLcSud9-_jEqV4KU_4ePJi_xdWehQzM"

# Ваше заготовленное сообщение
PREPARED_MESSAGE = "https://t.me/bh6hg45345t234"

# Функция-обработчик для команды /start
def start_command(update: Update, context: CallbackContext):
    update.message.reply_text(PREPARED_MESSAGE)

# Функция-обработчик для ЛЮБОГО текстового сообщения
def echo(update: Update, context: CallbackContext):
    update.message.reply_text(PREPARED_MESSAGE)

# Основная функция
def main():
    # 1. Создаем Updater и передаем токен
    updater = Updater(TOKEN, use_context=True)

    # 2. Получаем диспетчер для регистрации обработчиков
    dp = updater.dispatcher

    # 3. Регистрируем обработчики команд
    dp.add_handler(CommandHandler("start", start_command))
    
    # 4. Регистрируем обработчик для всех текстовых сообщений
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    # 5. Определяем режим запуска
    port = int(os.environ.get('PORT', 8443))
    webhook_url = os.getenv('RENDER_EXTERNAL_URL')
    
    if webhook_url:
        print(f"Запуск в режиме вебхука на порту {port}")
        # Запускаем вебхук
        updater.start_webhook(
            listen="0.0.0.0",
            port=port,
            url_path=TOKEN,
            webhook_url=f"{webhook_url}/{TOKEN}"
        )
        updater.idle()
    else:
        # Для локального тестирования
        print("Бот запущен в режиме опроса...")
        updater.start_polling()
        updater.idle()

if __name__ == '__main__':
    main()
