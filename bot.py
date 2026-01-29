

import telegram.ext

TOKEN = '8528886056:AAG8QLcSud9-_jEqV4KU_4ePJi_xdWehQzM'
LINK = 'https://t.me/bh6hg45345t234'  # Твоя ссылка

async def start(update, context):
    """Отправляет ссылку при /start"""
    await update.message.reply_text(LINK)

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()

if __name__ == '__main__':
    main()
