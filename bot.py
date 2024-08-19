import logging
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler
from commands import payment_method_click, start, subscribe
from database import create_database
from definitions import TOKEN

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Initialize database
create_database()

def main() -> None:
    updater = Updater(TOKEN)

    dispatcher = updater.dispatcher

    # Register command handlers
    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(CommandHandler('help', help))
    dispatcher.add_handler(CommandHandler('subscribe', subscribe))
    dispatcher.add_handler(CallbackQueryHandler(payment_method_click))

    # Start the bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()








