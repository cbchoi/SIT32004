import datetime
from functools import wraps

def check_asset(foo):
	@wraps(foo)
	def check_asset( self, *args, **kwargs ) :
		if self.amount - args[0] < 0:
			print("[Operation Not Allowed]")
		else:
			foo(self, *args, **kwargs)	

	return check_asset

def show_asset(foo):
	@wraps(foo)
	def show(self, *args, **kwargs ) :
		foo(self, *args, **kwargs)	
		print("Amount: {}".format(self.amount))
	return show

def log_asset(foo):
	@wraps(foo)
	def log( self, *args, **kwargs ) :
		foo(self, *args, **kwargs)	
		print("[{}] Op:{} Asset:{} Amount:{}".format(datetime.datetime.now(), foo.__name__,self.asset_name, self.amount))
	return log