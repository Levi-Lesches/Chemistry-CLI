import re

from .element import Element

# TODO: Implement Molecule.fromFormula

class Molecule:
	nested_regex = re.compile(r"\(([\w\(\)]+)\)(\d+)")
	regex = re.compile(r"([A-Z][a-z]?)(\d*)")

	"""
	A molecule made up of multiple elements.

	Properties
	- elements: {Element: int}
		A dictionary that maps elements to how many there are
	"""

	def __init__(self, elements, string = None): 
		self.elements = elements
		self.string = string

	def __str__(self): return self.string or "".join(
		f"{element}{count if count > 1 else ''}"
		for element, count in self.elements.items()
	)

	def parse(molecule: str): 
		"""Parses a molecular formula. Supports parentheses."""
		def _update_elements(element: Element, new_amount: int): 
			old_count = elements.get(element, 0)
			elements [element] = old_count + new_amount

		elements = {}
		molecule = molecule.strip()
		filtered_string = molecule
		# We need the match object to find the position of the match
		# .finditer gives the matches, while .findall gives tuples
		for match in Molecule.nested_regex.finditer(molecule):  
			nested_molecule = match.group(1)
			nested_molecule = Molecule.parse(nested_molecule)
			coefficient = int(match.group(2))
			filtered_string = molecule [:match.start()] + molecule [match.end():]
			for element, amount in nested_molecule.elements.items(): 
				_update_elements(element, amount * coefficient)

		for (element, amount) in Molecule.regex.findall(filtered_string): 
			amount = int(amount) if amount else 1
			_update_elements(element, amount)

		return Molecule(elements, string = molecule)
