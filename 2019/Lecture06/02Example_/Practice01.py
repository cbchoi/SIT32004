
from Practice01.decorator import *

class Asset(object):
	def __init__(self, asset_name="default", inital_money = 0):
		self.asset_name = asset_name
		self.amount = inital_money

	@check_asset
	@show_asset
	def transfer(self, amount, dst):
		self.amount -= amount
		dst.income(amount)

	@log_asset
	def income(self, amount):
		self.amount += amount

pocket1 = Asset("pocket", 100)
pocket2 = Asset("bank", 100)
pocket1.transfer(10, pocket2)