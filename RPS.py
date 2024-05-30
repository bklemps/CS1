import random

choices = ["rock", "paper", "scissors"]

while True:
    user_choice = str.lower(input("Enter stop to end. Rock, paper, or scissors: "))
    computer_choice = random.choice(choices)

    if user_choice == "stop":
        break
    elif user_choice not in choices:
        print("Invalid")
    else:
        if user_choice == computer_choice:
            print("It's a tie!")
        elif user_choice == "rock" and computer_choice == "scissors":
            print("You win!")
        elif user_choice == "paper" and computer_choice == "rock":
            print("You win!")
        elif user_choice == "scissors" and computer_choice == "paper":
            print("You win!")
        else:
            print("Computer wins!")

