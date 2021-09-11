#  calculator 

import math
from rich.console import Console
from rich.table import Table


console = Console() # I dont know what is it, but i must did it ;) 

table = Table(show_header=True, header_style="bold magenta")
table.add_column("Operation")
table.add_column("Name")
table.add_column("definition", justify="right")	

table.add_row("+", "addition", "[red]I dont know... Realy[/red]")
table.add_row("-", "subtraction", "[red]I dont know... Realy[/red]")
table.add_row("*", "multiplication", "The arithmetic action of repeating a given number by a term as many times as there are units in another given number, a factor.")
table.add_row("/", "division", "An arithmetic operation, by which it is recognized how many times one number is contained in another.")
table.add_row("!", "factorial", "Product of all natural numbers from 1 to a given natural number n")
table.add_row("sin", "sinus", "the ratio of the leg of the opposite angle to the hypotenuse")
table.add_row("cos", "cosine", "the ratio of the adjacent (close) leg to the hypotenuse")
table.add_row("tan", "tangent", "The ratio of the opposite (distant) leg to the adjacent (close) leg.")
table.add_row("D", "discriminant", "Her ego znaet :pile_of_poo: [RUS]")



while True:
	ComplexityOfTheOperation = input("The complexity of the operation is basic/complex/ultra (B/C/U) or help (h/help): ")
	
	if ComplexityOfTheOperation == 'h' or ComplexityOfTheOperation == 'help':
		console.print(table)


	elif ComplexityOfTheOperation == 'B' or ComplexityOfTheOperation == 'b':
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
		Operation = input("Select the operation (!, sqrt, sin, cos, tan): ")
		Number  = int(input("Input number: "))

		if Operation == '!':
			print(math.factorial(Number))

		elif Operation == 'sqrt':
			print(math.sqrt(Number))

		elif Operation == 'sin':
			print(math.sin(Number), "rad")

		elif Operation == 'cos':
			print(math.cos(Number), "rad")

		elif Operation == 'tan':
			print(math.tan(Number), "rad")


	elif ComplexityOfTheOperation == 'U' or ComplexityOfTheOperation == 'u':
		Operation = input("Select the operation (D): ")
		if Operation == "D":
			AForDiscriminant = int(input("Input A for discriminant: "))
			BForDiscriminant = int(input("Input B for discriminant: "))
			CForDiscriminant = int(input("Input C for discriminant: "))
			print(BForDiscriminant**2 - 4 * AForDiscriminant * CForDiscriminant)