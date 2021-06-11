from lib.equation import Equation

try: 
	equation = Equation.parse(input("Enter a chemical equation to balance: "))
except ValueError as error: 
	print("Invalid equation. Make sure each element is represented on both sides.")
	quit()

equation.balance()
assert equation.is_balanced(), f"Could not balance: {equation}"
print(equation)
