import random

user_wins = 0
computer_wins = 0

options = ["rock", "paper", "scissors"]

while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quit.").lower()
    if user_input == "q":
        break

    if user_input not in ["rock", "paper", "scissors"]:
        print("Enter a valid input!!")
        continue

    random_num = random.randint(0, 2)
    #rock: 0, paper: 1, scissors: 2
    computer_pick = options[random_num]
    print("Computer picked: ", computer_pick + ".")

    if user_input == "rock" and computer_pick == "scissors":
        print("you won!")
        user_wins += 1
    elif user_input == "paper" and computer_pick == "rock":
        print("you won!")
        user_wins += 1
    elif user_input == "scissors" and computer_pick == "paper":
        print("you won!")
        user_wins += 1
    else:
        print("You lost!")
        computer_wins += 1

print("You won {} times.".format(user_wins))
print("The computer won {} times".format(computer_wins))
print("Thanks for playing!!")