def get_sigfigs(num: str, after_decimal = False) -> int: 
	"""
	Counts the number of significant digits for a given input.

	Significant figures indicate the certainty and precision of a number. 
	For example, 20.2 means "anywhere between 20.15 and 20.24". But 20.20 means
	"anywhere between 20.195 and 20.204". This new range is much tighter, even 
	though the two numbers are numerically equivalent. 

	Set after_decimal to true to get the sigfigs for after the decimal point.

	Rules for what counts as a significant figure: 
	- Any non-zero number is significant. 
	- Any number between significant figures is significant.
	- Any trailing zeros after the decimal is significant. 
	- Trailing zeros are only significant if there is a decimal. 

	See the tests for examples. 
	"""
	result = 0
	whole, _, decimal = num.partition(".")  # .split might give an error

	# Process the whole part of the number: 
	whole = whole.lstrip("0")  # leading zeros don't count  
	if not decimal: whole = whole.rstrip("0")
	result += len(whole)

	# Process the decimal part of the number
	if not whole and decimal.strip("0"): decimal = decimal.lstrip("0")
	result += len(decimal)

	if after_decimal: return len(decimal)
	else: return result

def set_sigfigs(num: float, sigfigs: int) -> str: 
	"""Returns the number formatted with the given sigfigs."""
	current_sigfigs = get_sigfigs(str(num))
	if current_sigfigs > sigfigs: return f"{num:.{sigfigs}g}"  # simple truncate
	elif current_sigfigs < sigfigs:  # pad with zeros at the end
		difference = sigfigs - current_sigfig
		return str(num) + "0" * difference
	else: return str(num)

def add_subtract_rule(num: float, operands: [str]) -> str:
	"""Truncates a number to an appropriate number of decimal places."""
	decimal_sigfigs = [
		get_sigfigs(operand, after_decimal = True)
		for operand in operands
	]

	return f"{num:.{min(decimal_sigfigs)}f}"

def multiply_divide_rule(num: float, operands: [str]) -> str:
	"""Truncates a number to an appropriate number of sigfigs."""
	sigfigs = min(get_sigfigs(operand) for operand in operands)
	return set_sigfigs(num, sigfigs)
