from data.element import Element
from data.molecule import Molecule
from data.equation import Equation

# Elements: 
CARBON = Element("C")
OXYGEN = Element("O")
HYDROGEN = Element("H")

# Molecules: 
AIR = Molecule({OXYGEN: 2})
WATER = Molecule({HYDROGEN: 2, OXYGEN: 1})
CARBON_DIOXIDE = Molecule({CARBON: 1, OXYGEN: 2})
GLUCOSE = Molecule({CARBON: 6, HYDROGEN: 12, OXYGEN: 6})
DIATOMIC_HYDROGEN = Molecule({HYDROGEN: 2})
DIATOMIC_OXYGEN = Molecule({OXYGEN: 2})

# Equations: 
PHOTOSYNTHESIS = Equation(
	reactants = [WATER, CARBON_DIOXIDE],
	products = [AIR, GLUCOSE],
)
WATER_SYNTHESIS = Equation(
	reactants = [DIATOMIC_HYDROGEN, DIATOMIC_OXYGEN],
	products = [WATER],
)

if __name__ == "__main__": 
	print(PHOTOSYNTHESIS)
	PHOTOSYNTHESIS.balance()
	print(PHOTOSYNTHESIS)

	print(WATER_SYNTHESIS)
	WATER_SYNTHESIS.balance()
	print(WATER_SYNTHESIS)
