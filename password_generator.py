#password generator
import random
import string
import sys

print("Password generetor - the program will generate random\n8 characters password of different stregth.\n")
def passw():
	sec = str(input("How strong dou you want your password to be? \nChoose between weak, medium or strong: ")).lower()
	if sec == 'weak':
		letters = string.ascii_letters
		passw = ''.join(random.choice(letters) for i in range(8))
		print("Your password is:", passw)
	elif sec == 'medium':
		letters = string.ascii_letters
		numbers = string.digits
		passw = ''.join(random.choice(letters + numbers) for i in range(8))
		print("Your password is:", passw)
	elif sec == 'strong':
		letters = string.ascii_letters
		numbers = string.digits
		punct = string.punctuation
		passw = ''.join(random.choice(letters + numbers + punct) for i in range(8))
		print("Your password is:", passw)
passw()
exit = str(input("Do you want to generate another password[y/n]?: ")).lower()
while exit == 'y':
	passw()
	exit = str(input("Do you want to generate another password[y/n]?: ")).lower()
	if exit == 'n':
		print("Exiting program")
		sys.exit()
