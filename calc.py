#  calculator 

import math

while True:
	ComplexityOfTheOperation = input("The complexity of the operation is basic/complex (B/C): ")
	
	if ComplexityOfTheOperation == 'B' or ComplexityOfTheOperation == 'b':
		Operation = input("Select the operation (+, -, *, /): ")
		FirstNumber = int(input("Input first number: "))
		SecondNumber = int(input("Input second number: "))

		if Operation == "+":
			print(FirstNumber + SecondNumber)

		elif Operation == "-":
			print(FirstNumber - SecondNumber)

		elif Operation == "*":
			print(FirstNumber * SecondNumber)

		elif Operation == "/":
			print(FirstNumber / SecondNumber)

	elif ComplexityOfTheOperation == 'C' or ComplexityOfTheOperation == 'c':
		Operation = input("Select the operation (!, sqrt): ")
		Number  = int(input("Input number: "))

		if Operation == '!':
			print(math.factorial(Number))

		elif Operation == 'sqrt':
			print(math.sqrt(Number))