def calculator(a, b):

	operation = input('What operation do you want to carry out (add, subtract, multiply, divide) ').lower().strip()

	a = int(input('enter your first number'))
	b = int(input('enter the second number'))

	if operation == "add":
		return a + b
	elif operation == "subtract":
		return a - b
	elif operation == "multiply":
		return a * b
	try:
		elif operation == "divide":
			return a / b 
	except ZeroDivisionError:
		print('you have an error because you used zero as the denominator)
	else:
		return "Invalid operation"


def family():
  return 'hello fam'
