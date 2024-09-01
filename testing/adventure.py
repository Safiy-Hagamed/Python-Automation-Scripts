name = input ("Enter your name: ")
print ("Welcome to the adventure", name)

answer = input ("you and your friend were going to an abandoned house for some youtube content. you came near the house and it looks scary what do you wanna do [go inside/ leave] ")

if answer == "go inside":
	answer1 = input ("you and your friend decided to get into the house. as soon as you enter the house the door locked [ try to find key/ run ] - ")
	if answer1 == "try to find key":
		answer2 = input ("your friend panicked and fell down on the floor and there is no signal on your mobile, you hear a wierd sound from a room [ approach the room/ scream for help ] - ")
		if answer2 == "approach the room":
			answer3 = input ("you opened the door and there is no one in the room, suddenly you heared someone running . you turned around and your friend is missing from the floor [ search for him/ open the door and escape - ")
			if answer3 == "search for him":
				print ("you found him good job. you won")
			elif answer3 == "open the door and escape":
				print ("you are a coward. you lose")
				quit()
			else:
				print ("not a valid option you lose")
		elif answer2 == "scream for help":
			print ("you started screaming and the ghost haunted you ")
		else:
			print ("not a valid option you lose")
	elif answer1 == "run":
		print ("the ghost haunted you and you are lost")
	else:
		print ("not a valid option you lose")
elif answer == "leave":
	print ("you and you friend scared by the house and left immediately")
else:
	print ("not an valid option you lose")
print ("thanks for playing", name)


