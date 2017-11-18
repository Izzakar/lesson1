from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )


def main():
    updater = Updater("508192645:AAHpRrgje5XPMUs-Qlyz9H_bDeF4YYsMjc4")
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    updater.start_polling()
    updater.idle()


def greet_user(bot, update):
    text = 'Вызван /start'
    print(text)
    update.message.reply_text(text)
    #print (update)
    #print('Вызван /start')


def talk_to_me(bot, update):
    user_text = update.message.text
    logging.info(user_text)
    update.message.reply_text(user_text)

main()
