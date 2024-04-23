import random
print("Welcome to Rock, Paper, Scissors Game!")
print("You will be playing against the computer.")
print("Let's see who wins!")
while True:
	user_action = input("enter a choice (rock, paper, scissors): ")
	computer_action = random.choice(["rock", "paper", "scissors"])
	print("you chose " + user_action + ", computer chose " + computer_action)
	if computer_action == user_action:
		print("ohh no...both player selected " + user_action + " it's a tie!")
	elif user_action == "rock":
		if computer_action == "paper":
			print("ooopc...paper covers rock! you lose.")
		elif computer_action == "scissors":
			print("hurehh...Rock smashes scissors! you win!")
	elif user_action == "paper":
		if computer_action == "rock":
			print("hurehh...paper covers rock! you win!")
		elif computer_action == "scissors":
			print("ooopc...Scissors cut paper! you lose.")
	elif user_action == "scissors":
		if computer_action == "rock":
			print("ooopc...Rock smashes scissors! you lose.")
		elif computer_action == "paper":
			print("hurehh...Scissors cut paper! you win!")

	play_again = input("play again? (y/n): ")
	if play_again.lower() != "y":
		break
print("Thank you for playing Rock, Paper, Scissors!")
print("Hope you enjoyed the game!")