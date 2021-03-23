from generators import english_generator # Imports the module that allows us to generate passwords in English
from generators import spanish_generator # Imports the module that allows us to generate passwords in Spanish


def main():

	language = input("""Languages avalaible:
  English -> E
  Español -> S
Please select a language: """)

	if language.lower() == "e":
		password = english_generator.generate_password()
		print(f"Your new password is: {password}")
	elif language.lower() == "s":
		password = spanish_generator.generate_password()
		print(f"Tu nueva contraseña es: {password}")
	else:
		print("Error")


if __name__ == '__main__':
	main()