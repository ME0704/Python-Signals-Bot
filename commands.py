from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import CallbackContext

from definitions import OWNER_CONTACT, SUBSCRIPTION_PRODUCTS

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Welcome to our bot! Use /help for contact info and /subscribe for premium content.')

def help(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(f'Contact us: {OWNER_CONTACT}')

def subscribe(update: Update, context: CallbackContext) -> None:
    keyboard = []
    # Create clickable buttons for each product
    for product, price in SUBSCRIPTION_PRODUCTS.items():
        keyboard.append([InlineKeyboardButton(product + ' ' + price, callback_data=product)])
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text('Choose a subscription:', reply_markup=reply_markup)

def payment_method_click(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    data = query.data.split('_')
    method = data[0]
    product = data[1]
    # Replace with your payment URL generation logic
    payment_url = f'(link unavailable)'
    query.message.edit_text(f'Pay here: {payment_url}')