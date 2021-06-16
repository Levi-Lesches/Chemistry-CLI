from lib.sigfigs import *

OPERATORS = {"+", "-", "/", "*"}
OPERATIONS = {
	"+": lambda a, b: a + b,
	"-": lambda a, b: a - b,
	"/": lambda a, b: a / b,
	"*": lambda a, b: a * b,
}
SIGFIG_RULES = {
	"+": add_subtract_rule,
	"-": add_subtract_rule,
	"*": multiply_divide_rule,
	"/": multiply_divide_rule,
}

def get_close_paren(string: str, start: int) -> int:
	"""
	Returns the index of the closing parenthesis of the index in the string.
	"""
	count = 0
	for index in range(start, len(string)):  
		letter = string [index]
		if letter == "(": count += 1
		elif letter == ")": count -= 1
		if count == 0: return index

def tokenize(expression: str) -> (str, str, str): 
	"""Splits an expression into its left and right sides, and the operator."""
	index = 0
	left, right, operator = None, None, None
	while index < len(expression): 
		letter = expression [index]
		if letter == "(": 
			index = get_close_paren(expression, index) + 1
		elif letter in OPERATORS: 
			operator = letter
			left = expression [:index]
			right = expression [index + 1:]
			break
		else: index += 1
	if operator is None:  # expression is surrounded by parenthesis
		return tokenize(expression [1:-1])  # do NOT use .strip

	return left, operator, right

def evaluate(expression: str) -> str: 
	"""
	Evaluates an expression with the appropriate number of sigfigs.
	"""
	# Parse the expression recursively.
	left, operator, right = tokenize(expression)
	operands = []
	for sub_expression in (left, right): 
		sub_expression = sub_expression.strip()
		if "(" not in sub_expression:  # simple expression -- base case
			operands.append(sub_expression)
		else:  # nested expression -- recursive case
			operands.append(evaluate(sub_expression))

	# Apply operator to the operands
	operation = OPERATIONS [operator]
	result = operation(*map(float, operands))

	# Apply the correct number of sigfigs to the result.
	sigfig_rule = SIGFIG_RULES [operator]
	result = sigfig_rule(result, operands)

	return result

if __name__ == "__main__": 
	print("Enter 1 to count sigfigs, or 2 to evaluate an arithmetic expression")
	choice = int(input())
	if choice == 1: 
		num = input("Enter a number: ")  # do NOT use float() here
		print(f"That number has {get_sigfigs(num)} significant figures")
	elif choice == 2: 
		print("NOTE: Order of operations are not implemented. Use parentheses if needed")
		print("NOTE: All operators are limited to two operands. Use parentheses when needed")
		print("  Example: 1 + (2 + 3) instead of 1 + 2 + 3")
		print()
		expression = input("Enter an expression: ")
		print()
		print(evaluate(expression))
	else: 
		print("Only options 1 or 2 are supported")