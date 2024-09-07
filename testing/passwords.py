''' This code is for a studying and dont take this code seriously and store your important passwords in this code. '''
user = input ("enter the main password: ")

def view():
	with open('passwords.txt', 'r') as f:
		for line in f.readlines():
			data = line.rstrip()
			user, passw = data.split("|")
			print ("user: ", user, ",", "password: ", passw)
def add():
	name = input ("Account Name: ")
	passwd = input ("Password: ")

	with open('passwords.txt', 'a') as file:
		file.write (name+ "|" + passwd + "\n")

while True:
	choice = input ("would you like to [ view/add ] or q to quit - ").lower()
	if choice == "q":
		print ("Thanks for using this script")
		quit()
	elif choice == "view":
		view()
	elif choice == "add":
		add()
	else:
		print ("not an valid option..")
		continue
