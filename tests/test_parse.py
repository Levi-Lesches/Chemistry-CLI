if __package__ is None: 
	quit("Do not open this file directly. Use pytest")

from lib.molecule import Molecule
from lib.element import Element
from lib.equation import EquationSide, Equation
from unittest import TestCase

from .test_balance import TESTS as EQUATION_TESTS

H = Element("H")
O = Element("O")
Zn = Element("Zn")
Cl = Element("Cl")
Al = Element("Al")
S = Element("S")

MOLECULE_TESTS = {
	"H": {H: 1},  # simple element
	"H2": {H: 2},  # still one element, but with a subscript
	"H2O": {H: 2, O: 1},  # more than one element
	"2H2O": {H: 2, O: 1},  # ignore coefficients
	"ZnCl2": {Zn: 1, Cl: 2},  # Uppercase and lowercase
	"Al2(SO4)H": {Al: 2, S: 1, O: 4, H: 1},  # parentheses
	"Al2(SO4)3": {Al: 2, S: 3, O: 12},  # parens with subscript
}

def test_molecule(): 
	for test, elements in MOLECULE_TESTS.items(): 
		molecule = Molecule.parse(test)
		TestCase().assertDictEqual(molecule.elements, elements)

def test_element(): 
	assert H == Element("H"), "Can't compare two elements"

def test_equation_side(): 
	string = "H2O + O2"
	assert str(EquationSide.parse(string)) == string

def test_equation(): 
	for test in EQUATION_TESTS: 
		assert str(Equation.parse(test)) == test
