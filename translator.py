import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from langdetect import detect
from deep_translator import GoogleTranslator

# Enable logging for debugging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Hello! I will help you translate messages to English.')

# Translate function using deep-translator
async def translate_text(text, target_language="en"):
    try:
        translation = GoogleTranslator(source='auto', target=target_language).translate(text)
        return translation
    except Exception as e:
        logger.error(f"Translation error: {e}")
        return "Translation failed."

# Message handler for translations
async def translate_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    try:
        detected_lang = detect(text)
        # If detected language is not English, translate it
        if detected_lang != 'en':
            translation = await translate_text(text)
            await update.message.reply_text(f"Detected language: {detected_lang}\nTranslation: {translation}")
    except Exception as e:
        logger.error(f"Error detecting or translating message: {e}")
        await update.message.reply_text("Sorry, I couldn't process the message.")

def main():
    # Create the application and pass the bot token.
    application = Application.builder().token("7235845590:AAGEMqrFvoZyLfGqIVX8xSE_AyuXw9OaBVE").build()

    # Handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, translate_message))

    # Run the bot
    application.run_polling()

if __name__ == "__main__":
    main()
