print ("Welcome to One Piece quiz")
print ("If you win there will be reward at the end")
playing = input("Do you want to play? ")

if playing.lower() != "yes":
	quit()

print ("One piece quiz starts!!.... ")
score = 0

answer = input("What does luffy's wants to become? ")
if answer.lower() == "king of the pirates":
	print ("Correct..")
	score += 1
else:
	print ("Incorrect..")

answer = input("Who did luffy recruit first to his strawhat pirates group? ")
if answer.lower() == "zoro":
	print ("Correct..")
	score += 1
else:
	print ("Incorrect..")

answer = input("Who cooks food for the strawhat pirates? ")
if answer.lower() == "sanji":
	print ("Correct..")
	score += 1
else:
	print ("Incorrect..")

answer = input("Who is sogeking? ")
if answer.lower() == "ussop":
	print ("Correct..")
	score += 1
else:
	print ("Incorrect..")

print ("You got " + str(score) + " questions correct.")
print ("You got " + str((score/4) * 100) + "%.")
