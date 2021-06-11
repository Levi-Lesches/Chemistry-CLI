import math
from sympy import Matrix

from .element import Element
from .molecule import Molecule

class EquationSide: 
	"""
	One side of a chemical equation. 

	Properties
	- orderedTerms: [Molecule]
		A list of all the molecules in the order they appear.
	- elements: {Element}
		A set of all the elements on this side of the equation.
	- terms: {Molecule: int}
		A dictionary mapping of molecules to coefficients.
	"""

	def __init__(self, orderedTerms: [Molecule]): 
		self.orderedTerms = orderedTerms
		self.terms = { 
			molecule: 1
			for molecule in orderedTerms
		}
		self.elements = {
			element 
			for molecule in orderedTerms
			for element in molecule.elements.keys()
		}

	def __str__(self): 
		"""
		Prints the molecules with their coefficients, joined by a + sign.
		"""
		return " + ".join(
			f"{'' if coefficient in (None, 1) else coefficient}{molecule}"
			for molecule, coefficient in self.terms.items()
		)

	def parse(string): 
		"""Parses one side of a chemical equation"""
		return EquationSide([
			Molecule.parse(molecule)
			for molecule in string.split(" + ")
		])

	def get_element_counts(self, element: Element) -> [int]: 
		"""
		Returns how many of an element there are in each term.
		"""
		return [
			molecule.elements.get(element, 0) * coefficient
			for molecule, coefficient in self.terms.items()
		]

	def apply_coefficients(self, coefficients: [int]): 
		"""
		Transfers coefficients from a list into the terms property.
		"""
		for index in range(len(coefficients)):
			molecule = self.orderedTerms [index]
			self.terms [molecule] = coefficients [index]


class Equation: 
	"""
	A chemical equation representing a chemical reaction.
	
	Properties
	- reactants: EquationSide
		The reactants consumed by the reaction.
	- products: EquationSide
		The products produced by the reaction.
	"""

	def __init__(self, reactants: EquationSide, products: EquationSide):
		self.reactants = reactants
		self.products = products
		if not self._verify(): raise ValueError(f"Invalid equation: {self}")

	def __str__(self): return f"{self.reactants} --> {self.products}"

	def fromMolecules(reactants: [Molecule], products: [Molecule]): 
		"""Initializes an equation from the molecules on both sides"""
		return Equation(EquationSide(reactants), EquationSide(products))

	def parse(formula: str): 
		"""Parses a string representation of an equation"""
		left, _, right = formula.partition("-->")
		if not left or not right: 
			raise SyntaxError("Make sure your equation is of the form: H2 + O2 --> H2O")
		return Equation(
			EquationSide.parse(left), 
			EquationSide.parse(right)
		)

	def _verify(self): 
		return self.reactants.elements == self.products.elements

	def as_matrix(self): 
		"""
		Returns a matrix representation of this chemical reaction.

		Each row of the matrix represents an element, and each column represents 
		a molecule. The value of each cell is how many of the given element
		is in the given molecule. 
		"""
		return [
			[
				count 
				for side in (self.reactants, self.products)
				for count in side.get_element_counts(element)
			]
			for element in self.reactants.elements.union(self.products.elements)
		]

	def _normalize(nullspace: [int]) -> [int]: 
		"""
		Transforms a 1-d matrix of fractions into a list of integers.

		# The numbers are fractions. We have to multiply by the least common
		# multiple of their denominators to make them integers.
		"""
		denominators = [fraction.denominator() for fraction in nullspace] 
		lcm = math.lcm(*denominators)
		return [abs(num * lcm) for num in nullspace]  # left side is negative

	def balance(self): 
		"""
		Balances this chemical equation.

		Evaluates the nullspace vector of this equation's matrix form (see 
		[as_matrix]), and multiplies by the LCD to get positive integer results. 

		Then calls [EquationSide.apply_coefficients] on both sides to balance
		the reaction.
		"""

		# First, get the nullspace of the matrix form.
		matrix = Matrix(self.as_matrix())
		nullspace = matrix.nullspace(matrix) [0]
		coefficients = Equation._normalize(nullspace)

		# Finally, we apply the coefficients to the right sides of the equation.
		# We can do that by slicing the list of coefficients by the reactants. 
		numReactants = len(self.reactants.terms)
		self.reactants.apply_coefficients(coefficients [:numReactants]) 
		self.products.apply_coefficients(coefficients [numReactants:])

	def is_balanced(self): 
		"""
		Checks if this equation is balanced by comparing the elements on both sides.
		"""

		for element in self.reactants.elements: 
			amount_reactants = sum(self.reactants.get_element_counts(element))
			amount_products = sum(self.products.get_element_counts(element))
			if (amount_reactants != amount_products): return False
		else: return True
