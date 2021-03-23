import random


def generate_password():
	
	# Characters 
	uppercase = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "X", "Y", "W", "Z"]
	lowercase = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "m", "n", "o", "p", "q", "r", "s", "t", "u", "x", "y", "w", "z"]
	symbols = ["!", "#", "?", "/", "&", "%", "$", "*", "+", ".", "_", "-", ".", ";", ",", ":", "<", ">"]
	numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

	length = int(input("Enter the number of characters you want your password to have: "))
	password = []

	uppercase_on = input("""Would you like your password to contain capital letters?
Enter Y to accept and any other letter to deny: """)
	lowercase_on = input("""Would you like your password to contain tiny?
Enter Y to accept and any other letter to deny: """)
	symbols_on = input("""Would you like your password to contain symbols?
Enter Y to accept and any other letter to deny: """)
	numbers_on = input("""Would you like your password to contain numbers?
Enter Y to accept and any other letter to deny: """)

	if uppercase_on.lower() == "y" and lowercase_on.lower() == "y" and symbols_on.lower() == "y" and numbers_on.lower() == "y":
		characters = uppercase + lowercase + symbols + numbers 	
		for i in range(length):
			random_character = random.choice(characters)
			password.append(random_character)

		password = "".join(password)
		return password  

	elif lowercase_on.lower() == "y" and symbols_on.lower() == "y" and numbers_on.lower() == "y":
		characters = lowercase + symbols + numbers 	
		for i in range(length):
			random_character = random.choice(characters)
			password.append(random_character)

		password = "".join(password)
		return password  

	elif uppercase_on.lower() == "y" and symbols_on.lower() == "y" and numbers_on.lower() == "y":
		characters = uppercase + symbols + numbers 	
		for i in range(length):
			random_character = random.choice(characters)
			password.append(random_character)

		password = "".join(password)
		return password  

	elif uppercase_on.lower() == "y" and lowercase_on.lower() == "y" and numbers_on.lower() == "y":
		characters = uppercase + lowercase + numbers 	
		for i in range(length):
			random_character = random.choice(characters)
			password.append(random_character)

		password = "".join(password)
		return password  
	elif uppercase_on.lower() == "y" and lowercase_on.lower() == "y" and symbols_on.lower() == "y":
		characters = uppercase + lowercase + symbols	
		for i in range(length):
			random_character = random.choice(characters)
			password.append(random_character)

		password = "".join(password)
		return password

	elif uppercase_on.lower() == "y" and lowercase_on.lower() == "y":
		characters = uppercase + lowercase  	
		for i in range(length):
			random_character = random.choice(characters)
			password.append(random_character)

		password = "".join(password)
		return password  

	elif uppercase_on.lower() == "y" and symbols_on.lower() == "y":
		characters = uppercase + symbols  	
		for i in range(length):
			random_character = random.choice(characters)
			password.append(random_character)

		password = "".join(password)
		return password  

	elif uppercase_on.lower() == "y" and numbers_on.lower() == "y":
		characters = uppercase + numbers 	
		for i in range(length):
			random_character = random.choice(characters)
			password.append(random_character)

		password = "".join(password)
		return password  

	elif lowercase_on.lower() == "y" and symbols_on.lower() == "y":
		characters = lowercase + symbols
		for i in range(length):
			random_character = random.choice(characters)
			password.append(random_character)

		password = "".join(password)
		return password  

	elif lowercase_on.lower() == "y" and numbers_on.lower() == "y":
		characters = lowercase + numbers 	
		for i in range(length):
			random_character = random.choice(characters)
			password.append(random_character)

		password = "".join(password)
		return password  

	elif symbols_on.lower() == "y" and numbers_on.lower() == "y":
		characters = symbols + numbers 	
		for i in range(length):
			random_character = random.choice(characters)
			password.append(random_character)

		password = "".join(password)
		return password  

	elif uppercase_on.lower() == "y":
		characters = uppercase	
		for i in range(length):
			random_character = random.choice(characters)
			password.append(random_character)

		password = "".join(password)
		return password  

	elif lowercase_on.lower() == "y":
		characters = lowercase 	
		for i in range(length):
			random_character = random.choice(characters)
			password.append(random_character)

		password = "".join(password)
		return password  

	elif symbols_on.lower() == "y":
		characters = symbols
		for i in range(length):
			random_character = random.choice(characters)
			password.append(random_character)

		password = "".join(password)
		return password  

	elif numbers_on.lower() == "y":
		characters = numbers 	
		for i in range(length):
			random_character = random.choice(characters)
			password.append(random_character)

		password = "".join(password)
		return password  

	else:
		return "Error, please try again."