from telegram.ext import Updater, CommandHandler
from datetime import datetime

updater = Updater(token='BotToken', use_context=True)
dispatcher = updater.dispatcher

# Set callback functions
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")

def info(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Server time: {}".format(datetime.now()))

# Set Handler
start_handler = CommandHandler('start', start)
info_handler = CommandHandler('info', info)

# Set dispatcher
dispatcher.add_handler(start_handler)
dispatcher.add_handler()

# Start bot!
updater.start_polling()