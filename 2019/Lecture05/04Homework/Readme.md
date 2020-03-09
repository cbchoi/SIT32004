# Homework05 Revisiting a Store

Suppose that your neighbor opened a vegetable and fruit store. In order to provide a better service to customers, he has decided to use a computer program for his business. He offered you a summer internship at his store to develop this program, and you have happily accepted his offer. This program should handle three kinds of transactions: selling items, listing the current stock, and reporting all sales done during the day. 

* You should submit two programs
  - Store Management Program with SQLite
  - Store Management Program with MongoDB

* Refer the following program from SIT22001
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
def show_manu():
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
        s = show_manu()
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