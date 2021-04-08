# Functions go here
def choice_checker(valid_list, error,   question):

  error = "Please choose from Rock / Paper / Scissors (or xxx to quit)"

  valid = False 
  while not valid:

    # Ask user for choice (and put choice in lowercase)
    response = input(question).lower()

    # Iterates through list and if response is an item
    # In the list (or the first letter of the item), the full item name is returned 

    for item in valid_list:
      if response == item[0] or response == item:
        return item

    # Output an error if it is not in the list 
    print(error)
    print()  
# Main routine goes here  

# List for checking responses 
rps_lists = ["rock", "paper", "scissors", "xxx"]

# Looping for testing purposes 
user_choice = ""
while user_choice != "xxx":

  # Ask user for choice and check if it is valid 
  user_choice = choice_checker("Choose rock / paper / scissors (r/p/s):", rps_lists,"Please choose from rock, paper or scissors (or xxx to quit)")

  # Print out choice for comparrision purposes  
  print("You chose {}".format(user_choice))


# Lists of valid responces 
yes_no_lists = ["yes", "no"]
rps_lists = ["rock", "paper", "scissors", "xxx"]
