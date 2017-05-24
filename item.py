import const

class Item(object):

	def __init__(self, id, name, description, is_mem, type, type_icon, price_info):
		self.id = id
		self.name = name
		self.description = description
		self.is_mem = is_mem
		self.type = type
		self.type_icon = type_icon
		self.price_info = price_info

		self.icon = const.GE_ICON + str(self.id)
		self.large_icon = const.GE_LARGE_ICON + str(self.id)

	def price(self):
		return self.price_info.price()