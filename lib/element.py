class Element: 
	"""
	An element of the periodic table. 

	Properties
	- symbol: str
		The atomic symbol for this element
	"""

	def __init__(self, symbol): 
		self.symbol = symbol

	def __str__(self): return self.symbol
