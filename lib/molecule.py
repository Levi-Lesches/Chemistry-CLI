from data.element import Element

# TODO: Implement Molecule.fromFormula

class Molecule: 
	"""
	A molecule made up of multiple elements.

	Properties
	- elements: {Element: int}
		A dictionary that maps elements to how many there are
	"""

	def __init__(self, elements): 
		self.elements = elements

	def __str__(self): return "".join(
		f"{element}{count if count > 1 else ''}"
		for element, count in self.elements.items()
	)
