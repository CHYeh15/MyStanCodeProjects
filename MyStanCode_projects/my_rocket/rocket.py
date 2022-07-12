"""
File: rocket.py
Name: Kevin
-----------------------
This program should implement a console program
that draws ASCII art - a rocket.
The size of rocket is determined by a constant
defined as SIZE at top of the file.
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""

# This constant determines rocket size.
SIZE = int(input('Input Size:'))
size1 = 2 * SIZE + 2  # Determine the boundary
size2 = (2 * SIZE + 2) / 2


def main():
	"""
	Generate the every parts of the rocket and combine them
	"""
	head()  # Rocket head
	belt()  # Rocket link
	upper()  # Rocket upper body
	lower()  # Rocket lower body
	belt()  # Rocket link
	head()  # Rocket head


def head():
	"""
	Build the head of the rocket.
	"""
	for i in range(SIZE):
		for j in range(size1):
			if (j+1) <= size2:
				if (j+1)//(size2-i) >= 1:
					print('/', end='')
				else:
					print(' ', end='')
			elif (j+1) > size2:
				if (size1-j)//(size2-i) >= 1:
					print('\\', end='')
				else:
					print(' ', end='')
		print("")


def belt():
	"""
	Build the belt of the rocket.
	"""
	for i in range(size1):
		if i % size1 == 0:
			print('+', end='')
		elif (i+1) % size1 == 0:
			print('+', end='')
		else:
			print('=', end='')
	print("")


def upper():
	"""
	Build the upper body of the rocket.
	"""
	for i in range(SIZE):
		for j in range(size1):
			if (j+1) <= size2:
				if (j+1)//(size2-i) >= 1:
					if (j+1) % (size2-i) == 0:
						print('/', end='')
					else:
						print('\\', end='')
				elif j % size1 == 0:
					print('|', end='')
				else:
					print('.', end='')
			elif (j+1) > size2:
				if (size1-j)//(size2-i) >= 1:
					if (size1-j) % (size2 - i) == 0:
						print('\\', end='')
					else:
						print('/', end='')
				elif (j+1) % size1 == 0:
					print('|', end='')
				else:
					print('.', end='')
		print("")


def lower():
	"""
	Build the lower body of the rocket.
	"""
	for i in range(SIZE):
		i = SIZE-1-i
		for j in range(size1):
			if (j+1) <= size2:
				if (j+1)//(size2-i) >= 1:
					if (j+1) % (size2-i) == 0:
						print('\\', end='')
					else:
						print('/', end='')
				elif j % size1 == 0:
					print('|', end='')
				else:
					print('.', end='')
			elif (j+1) > size2:
				if (size1-j)//(size2-i) >= 1:
					if (size1-j) % (size2 - i) == 0:
						print('/', end='')
					else:
						print('\\', end='')
				elif (j+1) % size1 == 0:
					print('|', end='')
				else:
					print('.', end='')
		print("")


###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
	main()