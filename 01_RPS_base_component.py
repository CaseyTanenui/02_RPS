import random

# Functions go here 
def check_rounds():
  while True:
    response = input("How many rounds: ")

    round_error = "Please type either <enter> or an integer that is more than 0"
    
    if response != "":
      try:
        response = int(response)

        if response < 1:
          print(round_error)
          continue
      
      except ValueError:
        print(round_error)
        continue

    return response
    
# Main routine goes here 

# List of valid responses 
yes_no_lists = ["yes", "no"]
rps_lists = ["rock", "paper", "scissors", "xxx"]

# Ask user if they have played before
# if 'yes', show instructions 

# Ask user for # of rounds, then loop

# Ask user if they would like to see their game history
# If 'yes', show game history

# Show game statistics