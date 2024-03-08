import random  # Imports random module

user_wins = 0  # Initializes user_wins variable to 0
computer_wins = 0  # Initializes computer_wins variable to 0
ties = 0  # Initializes ties variable to 0

options = ["rock", "paper", "scissors", "lizard", "spock"]  # Initializes options list with generic RPS options


while True:  # Starts loop
    user_input = input("Type Rock/Paper/Scissors/Lizard/Spock or Q to Quit: ").lower()  # Asks for user input
    if user_input == "q":  #  If user input is q
        break  # Break out of the loop

    if user_input not in options:  # If input is not in options list
        continue  #  Continue the loop, but don't do anything

    random_number = random.randint(0, 4)  # Generates a random number between 0 and 4
    computer_pick = options[random_number]  # Computer picks based on random number
    print(f"Computer Picked {computer_pick}.")

    # Checks for tie
    if user_input == computer_pick:
        print("It's a tie!")
        ties += 1
    #  *CONDITIONALS for winning scenarios*
    elif (user_input == "rock" and (computer_pick == "scissors" or computer_pick == "lizard"))\
            or (user_input == "paper" and (computer_pick == "rock" or computer_pick == "spock"))\
            or (user_input == "scissors" and (computer_pick == "paper" or computer_pick == "lizard"))\
            or (user_input == "lizard" and (computer_pick == "spock" or computer_pick == "paper"))\
            or (user_input == "spock" and (computer_pick == "rock" or computer_pick == "scissors")):
        print("You Won!")  # User Wins
        user_wins += 1  # Adds 1 to user_wins variable
    else:
        print("You Lost!")  # Any other condition results in a loss for the user
        computer_wins += 1

print(f"You won {user_wins} times!")
print(f"The computer won {computer_wins} times!")
print(f"You and the computer tied {ties} times!")
print("Goodbye!")
