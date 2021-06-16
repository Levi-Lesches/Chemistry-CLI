if __package__ is None: 
	quit("Do not open this file directly. Use pytest")

from lib.sigfigs import get_sigfigs
from bin.sigfigs import evaluate

TESTS = {
	"1": 1, 
	"10": 1,
	"10.0": 3,
	"101": 3, 
	"10.1": 3,
	"10.01": 4,
	"10.010": 5,
	"10.000": 5,
	"0.0": 1, 
	"0.01": 1,
	"0.010": 2, 
}

ARITHMETIC_TESTS = {
	"1+1": "2",
	"1 + 1": "2",
	"1 - 1": "0",
	"1 * 1": "1",
	"1 / 1": "1",
	"1 + (1 + 1)": "3",
	"(1 + 1) + 1": "3",
	"(1 + 1) + (1 + 1)": "4",
	"1 + (3 + (1 + 1))": "6",
}

ARITHMETIC_SIGFIG_TESTS = {
	"1.23 + 1.234": "2.46",
	"1.100 - 1.10": "0.00",
	"1.120 * 1.12": "1.25",
	"1.00 / 1": "1",
	"1.23 + (1.234 + 1.23)": "3.69",  # Nice (¬‿¬)
	"(1.234 + 1.23) + 1": "3",
	"(1.2 + 1.34) + (1.45 + 1.00)": "5.0",
	"1.1 + (3.12 + (1.123 + 1.1234))": "6.5",
}


def test_sigfigs_counting(): 
	for test, count in TESTS.items(): 
		assert get_sigfigs(test) == count

def test_arithmetic(): 
	for test, result in ARITHMETIC_TESTS.items():
		assert evaluate(test) == result

def test_arithmetic_sigfigs(): 
	for test, result in ARITHMETIC_SIGFIG_TESTS.items():
		assert evaluate(test) == result, f"Miscalculated sigfigs for {test}"