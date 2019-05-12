import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from image_handler import *

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


from pathlib import Path

cur_dir = Path("./img")
cur_dir = cur_dir.resolve()

class ImageManager(object):
    def __init__(self):
        self.updater = Updater("YOUR_TOKEN_HERE", use_context=True)
        # Get the dispatcher to register handlers
        self.dp = self.updater.dispatcher

        # on different commands - answer in Telegram
        
        # on noncommand i.e message - echo the message on Telegram
        self.dp.add_handler(MessageHandler(Filters.text, self.echo))

        # log all errors
        self.dp.add_error_handler(self.error)
    
    def _list(self, update, context):
        global cur_dir
        pass

    def echo(self, update, context):
        """Echo the user message."""
        print(update.message.chat_id)
        update.message.reply_text(update.message.text)

    def error(self, update, context):
        """Log Errors caused by Updates."""
        logger.warning('Update "%s" caused error "%s"', update, context.error)

    def start_polling(self):
        # Start the Bot
        self.updater.start_polling()

        # Run the bot until you press Ctrl-C or the process receives SIGINT,
        # SIGTERM or SIGABRT. This should be used most of the time, since
        # start_polling() is non-blocking and will stop the bot gracefully.
        self.updater.idle()

    def show_image(self, update, context):
        global cur_dir
        fpath = str(update.message.text).split()
            # fpath[0] : /select
        # fpath[1] : destination
        flist = list(cur_dir.glob('**/' + fpath[1]))
        if flist:
            context.bot.send_photo(chat_id=update.message.chat_id, photo=open(str(flist[0]), 'rb'))    
    
    def rot90(self, update, context):
        global cur_dir
        fpath = str(update.message.text).split()
        # fpath[0] : /select
        # fpath[1] : destination
        pass

def main():
    im = ImageManager()
    im.start_polling()
    
if __name__ == '__main__':
    main()