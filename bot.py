import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

BOT_TOKEN = os.getenv("8307358430:AAHWMWZEaY2EWC8_44aMyQX4rlz8uR47ntw")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👋 Welcome to Aiveno AI")

async def chat(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Aiveno AI is online 24×7 🚀")

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, chat))
    app.run_polling()

if __name__ == "__main__":
    main()
