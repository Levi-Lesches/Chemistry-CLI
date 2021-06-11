from lib.equation import Equation

try: 
	equation = Equation.parse(input("Enter a chemical equation to balance: "))
except Exception as error: 
	print(f"ERROR: {error.msg}")
	quit()

equation.balance()
assert equation.is_balanced(), f"Could not balance: {equation}"
print(equation)
