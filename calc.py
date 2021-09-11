#  calculator 

while True:
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