Problem03: Source Code Analysis
=============
## 3.1 Draw Class Diagram of the given program. 

* Notes
  * You may use PowerPoints or Words.

```python
class ImageManager(object):
    def __init__(self):
        self.updater = Updater("791208549:AAGZ2VT74r1nbz70UJk6I267WpSCNdJUhzU", use_context=True)
        # Get the dispatcher to register handlers
        self.dp = self.updater.dispatcher

        # on different commands - answer in Telegram
        self.dp.add_handler(CommandHandler("list", self._list))
        self.dp.add_handler(CommandHandler('show', self.show_image))
        self.dp.add_handler(CommandHandler('rot90', self.rot90))
        # on noncommand i.e message - echo the message on Telegram
        self.dp.add_handler(MessageHandler(Filters.text, self.echo))

        # log all errors
        self.dp.add_error_handler(self.error)
    
    def _list(self, update, context):
        global cur_dir
        lst = list(cur_dir.glob('**/*.jpg'))
        lst.extend(list(cur_dir.glob('**/*.png')))
        lst.extend(list(cur_dir.glob('**/*.bmp')))
        
        lst = [str(x) for x in lst]
        lst = "\n".join(lst)
        update.message.reply_text(lst)
    
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
        flist = list(cur_dir.glob('**/' + fpath[1]))
        if flist:
            ih = ImageHandler(str(flist[0]))
            ih.RotateImageFile(90)
            #tmp = str(cur_dir) + '/tmp.jpg'
            ih.SaveImageFile()
            context.bot.send_photo(chat_id=update.message.chat_id, photo=open(str(flist[0]), 'rb'))
```

## 3.2 Draw Sequence Diagram of the given program. 
```python
def load_stock(filename):
    file = open(filename, "r")
    stock_list = []
    for line in file:
        line = line.strip()
        item = line.split(",")
        item[1] = int(item[1])
        item[2] = int(item[2])
        stock_list.append(item)
    file.close()
    stock_list.sort()

    return stock_list

def store_stock(stock_list):
    file = open("stock.txt", "w")
    for line in stock_list:
        line[1] = str(line[1])
        line[2] = str(line[2])
        item = ",".join(line) + "\n"
        file.write(item)
    file.close()

def take_name(stock_list):
   while True:
       res = " "
       name = input("What you want to buy? >>>")
       for item in stock_list:
           if item[0] == name:
              break
       if item[0]  == name:
           break
       else:
           print ("Sorry, we do not have a stock for " + name + ".")
           res = input("Do you want to buy other item? (y/n)>>>")
           if res ==  "n" :
              break   
   if res == " ":
       return item
   else:
       return []
    
def take_quant(item):
   while True:
       res = " "
       try:
          qty = int(input("How many? >>>"))
          if qty > item[1]:
             print ("Sorry, we have only  %5d items." % item[2])
             res = input("Would you buy? (y/n)>>>")
             if res == "y":
                 qty = item[1]
          break    
       except:
          print ("Type in a number. >>>")
   if res == "y" or res == " ":
       return qty
   else:
       return 0

def take_input(stock_list):
    item = take_name(stock_list)
    if item != []:
       quant = take_quant(item)
    else:
       quant = 0
    return item, quant
            
def sell(stock_list, sales_hist):
    item, quant = take_input(stock_list)
    if item == []:
       return
    item[1] -= quant
    amount = item[2] * quant
    print ("item = ", item[0], ";  price = ", item[2], ";  quanity = ", quant, \
          ";  amount = ", amount)
    sales_hist.append((item[0], item[2], quant, amount))
    
def print_stock(stock_list):
    print ("\n", " " * 20 + "STOCK REPORT")
    print ("Name               price    quatity         amount")
    for item  in stock_list:
        print ("%-10s        %5d       %5d         %6d" % (item[0], item[2], item[1], \
              item[1] * item[2]))
        
        
def print_sales(sales_hist):
    print (" " * 20 + "SALES REPORT")
    print ("Name        price     quatity     amount")
    for item  in sales_hist:
        print ("%-10s  %5d     %5d     %6d" % (item[0], item[1], item[2], item[3]))
"""
What would you like to do?
   S: Sell item 
   P: Print stock
   R: Report sales
   E: Exit
Enter your choice (S, P, R, or E)>>
"""
def show_menu():
    print ("\n",  "What would you like to do?")
    print ("   S: Sell an item")
    print ("   P: Print stock")
    print ("   R: Report sales")
    print ("   E: Exit")
    return input ("Enter your choice (S, P, R, or E))>>>")

def input_error(s):
    print (s + "?" + "I beg your pardon.")
           
def main():                      
    stock_list = load_stock("stock.txt")
    sales_hist = []
    while True:
        s = show_menu()
        if s == "E":
           break
        elif s=="S":
            sell( stock_list, sales_hist)
        elif s =="P":
            print_stock(stock_list)
        elif s == "R":
            print_sales(sales_hist)
        else:
            input_error(s)
    store_stock(stock_list)

main()

```