# Instructions:

# Create a new Python file and call it main.py. Inside it you'll create your game.
# Create a list to store all possible options:
# "R" for "rock",
# "P" for "paper",
# "S" for "scissors".
# When the program is run, ask the user to pick an option between "R", "P" or "S"
# If user input is invalid (not amongst our options), print an error, and ask for their input again (should be a loop)
# Use the `choice` function from the inbuilt Python `random` module to make a choice for CPU player(computer).

# Check both player's moves:
# If there is a winner, print the winner, and the program ends.
# If it's a tie (the computer and player pick the same move), restart the game from step 3

import random

option_list = ["R", "P", "S"]
option = {
    'R':'Rock',
    'P': 'Paper',
    'S': 'Scissors'
}

game_on = True
while game_on:
    user_option = input('Select your game (R, P or S): ').upper()
    if user_option in option_list:
        CPU_game = random.choice(option_list)
        player = option[user_option]
        computer = option[CPU_game]
        print(f"Player({player}) : CPU({computer})")

        # validation
        if user_option == CPU_game:
            print('It is a tie')
        elif (user_option == 'P' and CPU_game == 'R') or (user_option == 'S' and CPU_game == 'P') or (user_option == 'S' and CPU_game == 'R'):
            print('Player Wins')
            game_on = False
        else:
            print('CPU Wins')
            game_on = False

    else:
        print("Sorry, Your input isn't valid, please select a valid input")