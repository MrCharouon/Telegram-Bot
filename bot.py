from telegram.ext import Updater, MessageHandler, Filters

# Telegram API
updater = Updater(token='XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
dispatcher = updater.dispatcher


def gpt(bot, update):
    bot.sendMessage(
        chat_id=update.message.chat_id,
        text='Hi, I am on the Fandogh.cloud'
    )


def main():
    # handle dispatcher
    dispatcher.add_handler(MessageHandler(Filters.text, gpt))

    # run
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
