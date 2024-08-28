import random

contents = ["rock", "paper", "scissors"]

useroption = input ("rock,paper,scissors or q to quit - ")
computerguess = random.randint(0, 2)

if useroption == "rock" and computerguess == "scissors":
	print ("You won!")
