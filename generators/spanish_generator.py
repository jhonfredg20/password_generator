import random


def generate_password():
	
	# Characters 
	uppercase = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "X", "Y", "W", "Z"]
	lowercase = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "m", "n", "o", "p", "q", "r", "s", "t", "u", "x", "y", "w", "z"]
	symbols = ["!", "#", "?", "/", "&", "%", "$", "*", "+", ".", "_", "-", ".", ";", ",", ":", "<", ">"]
	numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

	length = int(input("Ingresa el numero de caracteres que deseas que tenga tu contraseña: "))
	password = []

	uppercase_on = input("""¿Quieres que tu contraseña contenga mayúsculas?
Ingresa la letra S para aceptar y cualquier otra para negar: """)
	lowercase_on = input("""¿Quieres que tu contraseña contenga minúsculas?
Ingresa la letra S para aceptar y cualquier otra para negar:  """)
	symbols_on = input("""¿Quieres que tu contraseña contenga símbolos?
Ingresa la letra S para aceptar y cualquier otra para negar: """)
	numbers_on = input("""¿Quieres que tu contraseña contenga números?
Ingresa la letra S para aceptar y cualquier otra para negar: """)

	if uppercase_on.lower() == "s" and lowercase_on.lower() == "s" and symbols_on.lower() == "s" and numbers_on.lower() == "s":
		characters = uppercase + lowercase + symbols + numbers 	
		for i in range(length):
			random_character = random.choice(characters)
			password.append(random_character)

		password = "".join(password)
		return password  

	elif lowercase_on.lower() == "s" and symbols_on.lower() == "s" and numbers_on.lower() == "s":
		characters = lowercase + symbols + numbers 	
		for i in range(length):
			random_character = random.choice(characters)
			password.append(random_character)

		password = "".join(password)
		return password  

	elif uppercase_on.lower() == "s" and symbols_on.lower() == "s" and numbers_on.lower() == "s":
		characters = uppercase + symbols + numbers 	
		for i in range(length):
			random_character = random.choice(characters)
			password.append(random_character)

		password = "".join(password)
		return password  

	elif uppercase_on.lower() == "s" and lowercase_on.lower() == "s" and numbers_on.lower() == "s":
		characters = uppercase + lowercase + numbers 	
		for i in range(length):
			random_character = random.choice(characters)
			password.append(random_character)

		password = "".join(password)
		return password  
	elif uppercase_on.lower() == "s" and lowercase_on.lower() == "s" and symbols_on.lower() == "s":
		characters = uppercase + lowercase + symbols	
		for i in range(length):
			random_character = random.choice(characters)
			password.append(random_character)

		password = "".join(password)
		return password

	elif uppercase_on.lower() == "s" and lowercase_on.lower() == "s":
		characters = uppercase + lowercase  	
		for i in range(length):
			random_character = random.choice(characters)
			password.append(random_character)

		password = "".join(password)
		return password  

	elif uppercase_on.lower() == "s" and symbols_on.lower() == "s":
		characters = uppercase + symbols  	
		for i in range(length):
			random_character = random.choice(characters)
			password.append(random_character)

		password = "".join(password)
		return password  

	elif uppercase_on.lower() == "s" and numbers_on.lower() == "s":
		characters = uppercase + numbers 	
		for i in range(length):
			random_character = random.choice(characters)
			password.append(random_character)

		password = "".join(password)
		return password  

	elif lowercase_on.lower() == "s" and symbols_on.lower() == "s":
		characters = lowercase + symbols
		for i in range(length):
			random_character = random.choice(characters)
			password.append(random_character)

		password = "".join(password)
		return password  

	elif lowercase_on.lower() == "s" and numbers_on.lower() == "s":
		characters = lowercase + numbers 	
		for i in range(length):
			random_character = random.choice(characters)
			password.append(random_character)

		password = "".join(password)
		return password  

	elif symbols_on.lower() == "s" and numbers_on.lower() == "s":
		characters = symbols + numbers 	
		for i in range(length):
			random_character = random.choice(characters)
			password.append(random_character)

		password = "".join(password)
		return password  

	elif uppercase_on.lower() == "s":
		characters = uppercase	
		for i in range(length):
			random_character = random.choice(characters)
			password.append(random_character)

		password = "".join(password)
		return password  

	elif lowercase_on.lower() == "s":
		characters = lowercase 	
		for i in range(length):
			random_character = random.choice(characters)
			password.append(random_character)

		password = "".join(password)
		return password  

	elif symbols_on.lower() == "s":
		characters = symbols
		for i in range(length):
			random_character = random.choice(characters)
			password.append(random_character)

		password = "".join(password)
		return password  

	elif numbers_on.lower() == "s":
		characters = numbers 	
		for i in range(length):
			random_character = random.choice(characters)
			password.append(random_character)

		password = "".join(password)
		return password  

	else:
		return "Error, por favor intenta de nuevo."
