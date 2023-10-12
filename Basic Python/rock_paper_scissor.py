# this program contains simple introduction to python

import random # importing a library
# libraries are useful functions which are used without writing the code from scratch

def get_choices(): # function
    
    player_choice = input("Enter a choice (rock, paper, scissors): ")
    options = ["rock","paper","scissor"] # list
    computer_choice =  random.choice(options) # random funtion to select random choices from a given list
    
    choices = {"player": player_choice, "computer": computer_choice} # dictionary with key value pairs
    return choices # used to return the value to the function 

def check_win(player, computer):
    print(f"You chose {player} computer chose {computer}") # + can be used to concatenate two strings
    # f (f-strings) in the beginning of the "" can be used to combine strings
    
    if player == computer:
        return "It's a tie."
    
    # we restructured the code in order to keep the original functionality (Refactoring and nested-if)
    # otherwise too many if-else statements
    
    elif player == "rock":
        if computer == "scissor":
            return "You win!"
        else:
            return "You lose."
        
    elif player == "paper":
        if computer == "rock":
            return "You win!"
        else:
            return "You lose."
        
    elif player == "scissor":
        if computer == "paper":
            return "You win!"
        else:
            return "You lose."

choices = get_choices() # calling the get_choices () function to store the values
result = check_win(choices["player"],choices["computer"]) 
# choices[] (in this case) is used to access the value of a particular key in a dictionary
print(result) 

    
