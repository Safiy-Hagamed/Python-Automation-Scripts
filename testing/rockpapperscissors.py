import random

userwon = 0
compwon = 0
contents = ["rock", "paper", "scissors"]


while True:
	useroption = input ("rock,paper,scissors or q to quit: ").lower()
	if useroption == "q":
		print ("your wins = ", userwon)
		print ("computer wins = ", compwon)
		print ("Goodbye, Thanks for playing")
		quit()

	# making a list so we can check if the user didnt typed incorrect it will start loop again
	if useroption not in contents:
		continue

	randomnumbers = random.randint(0, 2)
	computerguess = contents[randomnumbers]

	if useroption == "rock" and computerguess == "scissors":
		print ("You won.. computer picked", computerguess)
		userwon += 1
		continue
	elif useroption == "paper" and computerguess == "rock":
		print ("You won.. computer picked", computerguess)
		userwon += 1
		continue
	elif useroption == "scissors" and computerguess == "paper":
		print ("You won.. computer picked", computerguess)
		userwon += 1
		continue
	elif useroption == "rock" and computerguess == "rock":
		print ("its a tie.. computer picked", computerguess)
		continue
	elif useroption == "paper" and computerguess == "paper":
		print ("its a tie.. computer picked", computerguess)
		continue
	elif useroption == "scissors" and computerguess == "scissors":
		print ("its a tie.. computer picked", computerguess)
		continue
	else:
		print ("you lost.. computer picked", computerguess)
		compwon += 1
		continue


print ("your wins = ", userwon)
print ("computer wins = ", compwon)

print ("Goodbye, Thanks for playing")
