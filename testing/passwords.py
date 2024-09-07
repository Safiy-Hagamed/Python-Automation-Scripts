user = input ("enter the main password: ")

def view():
	print("Hello worlds")


def add():
	name = input ("Account Name: ")
	passwd = input ("Password: ")
	with open("passwords.txt", 'a') as file:
		file.write (name+ " | " + passwd)

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
