from functools import wraps
import datetime
def log_asset(foo):
	@wraps(foo)
	def log( self, *args, **kwargs ) :
		foo(self, *args, **kwargs)	
		print("[{}] Op:{} Asset:{} Amount:{}".format(datetime.datetime.now(), foo.__name__,self.asset_name, self.amount))
	return log

def check_asset(foo):
	@wraps(foo)
	def check_asset( self, *args, **kwargs ) :
		if self.amount - args[0] < 0:
			print("[Operation Not Allowed]")
		else:
			foo(self, *args, **kwargs)	

	return check_asset

class Asset(object):
	def __init__(self, asset_name, inital_money ):
		self.asset_name = asset_name
		self.amount = inital_money

	@log_asset
	@check_asset
	def transfer(self, amount, dst):
		#if self.assets - amount > 0:
		dst.income(amount)
		self.amount -= amount

		pass

	def income(self, amount):
		pass

	@log_asset
	@check_asset
	def expense(self, amount):
		#if self.assets - amount > 0:
		self.amount -= amount

		return amount

#	def log_asset(self, txt):
#		pass

	@log_asset
	def show_asset(self):
		print("Asset Name:{} Asset Amount:{}".format(self.asset_name, self.amount))
		pass

	def check_asset(self, asset_amount, amount):
		pass

class ManagementSystem(object):
	def __init__(self):
		self.assets = {}

	def register_asset(self, name, inital_money):
		if not name in self.assets:
			self.assets[name] = Asset(name, inital_money)
		else:
			print("Asset name already taken")
		pass

	def unregister_asset(self, name):
		self.assets.pop(name)
		pass

	def income(self, name, amount):
		pass

	def expense(self, name, amount):
		self.assets[name].expense(amount)

		pass

#	def log_management(self):
#		pass

	def list_asset(self):
		for k, v in self.assets.items():
			v.show_asset()

		pass

	def show_asset_status(self, name):
		pass


ms = ManagementSystem()

ms.register_asset("pocket", 100000)
ms.register_asset("pocket1", 100000)

#ms.unregister_asset("pocket1")
ms.expense("pocket", 50000)
ms.expense("pocket", 150000)
ms.list_asset()
