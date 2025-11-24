from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, CommandHandler, ContextTypes, filters

# This function handles any text message
async def reply_hello(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Nak Nak srolanh Sokleap")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Henlo! Ask me anything.")

def main():
    # Replace with your bot token
    app = ApplicationBuilder().token("8519394721:AAHsYHxHG5itQZfUgEPleOwzBHOR-Xp_C5s").build()

    # /start command
    app.add_handler(CommandHandler("start", start))

    # Any text message
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, reply_hello))

    print("Bot running...")
    app.run_polling()

if __name__ == "__main__":
    main()
