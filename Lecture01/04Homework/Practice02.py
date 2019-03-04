from process_data import *

years = range(1994, 2010)
exchange_rate = []

for yr in years:
	process_data("data/", yr, exchange_rate)

print(exchange_rate)