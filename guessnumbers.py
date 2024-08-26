import random

print ("Welcome to guess the number game ")
maxnum = input ("Enter a value - ")

if maxnum.isdigit():
	maxnum = int(maxnum)
else:
	print ("Enter a number next time")
	quit()

if maxnum <= 0:
	print ("Enter a value greater than 0")
	quit()

randoms = random.randint(0, maxnum)
print (randoms)
points = 0

while True:
	guessed = input ("Make a guess ")
	points += 1
	if guessed.isdigit():
		guessed = int(guessed)
	else:
		print ("Enter a number next time")
		continue
	if guessed == randoms:
		print ("You have guessed it in", points, "guesses")
		break
	else:
		print ("Wrong..")

