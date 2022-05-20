import random

max_range = input("Enter a number: ")

if max_range.isdigit():
    max_range  = int(max_range)

    if  max_range <= 0:
        print("Enter a number greater than zero next time")
        quit()

else:
    print("Enter a number please")
    quit()

random_number = random.randint(0, max_range)
guesses = 0

while True:
    guesses += 1
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("guess should be number.")
        continue
    
    if user_guess == random_number:
        print("you got it!")
        break
    elif user_guess > random_number:
        print("you were above the number!")
    else:
        print("You were below the number!")

print("you got it in {} guesses".format(guesses))
     