import random

# Function go here 

# Will ask users how many rounds they would like to play 
# Checks to see if it is an integer more than 0
# If they type anything that is not asked for
# Print error 
def check_rounds():
  while True: 
    print()
    response = input("How many rounds would you like to play?: ")

    rounds_error = "Please type either <enter> or an integer that is more than 0"
    if response != "":
      try:
        response = int(response)

        if response <1:
          print(rounds_error)
          continue 

      except ValueError:
        print(rounds_error)
        continue

    return response 

# Asks users what they would like to play with out of the list
# Output the option they chose
def choice_checker(question, valid_list, error):
  
  valid = False
  while not valid:

    # Ask user for choice (and put choice in lower case)
    response = input(question).lower()

    # iterstes through list and if resonse is an item
    # in the list (or the first leter of an item), the 
    # full item name is returned

    for item in valid_list:
        if response == item[0] or response == item:
            return item

    # output error if item not in list 
    print(error)
    print()

# If user says "no"
# Show Instructions
def instructions():
    statement_generator("How to play", "⚔")
    print()
    print("Firstly, pick a Integer that is more than 0")
    print()
    print("Then for for each round, choose from the list of Rock, Paper or Scissors (or 'xxx' to quit)")
    print("If you wouldn't like to type the whole word, you can type 'r', 'p', or 's'")
    print()
    print("How you win the game, depends on:")
    print()
    print("If you choose rock, rock beats scissors")
    print("If you choose scissors, scissors beats paper")
    print("If you choose rock, rock beats paper")
    print()
    print("Have fun trying!..")
    print()
    return""

# If user says 'y' or 'yes', game continues
# If user says 'n' or 'no', display instructions
# If users don't reply with what was asked from them
# Output error
def yes_no(question):
    valid = False
    while not valid:
        response = input(question).lower()
        if response == "yes" or response == "y":
            response = "yes"
            return response

        elif response == "no" or response == "n":
            response = "no"
            return response

        else:
            print("Please answer either 'yes' or 'no'")
            print()

# This will decorate some of the words that will be shown on the screen
# So the game does not appear boring
def statement_generator(statement, decoration):

    sides = decoration * 3

    statement = "{} {} {}".format(sides, statement, sides)
    top_bottom = decoration * len(statement)

    print(top_bottom)
    print(statement)
    print(top_bottom)

    return ""


# The Main routine goes here 
print("Welcome to Rock, Paper, Scissors!")
print()
played_before = yes_no("Have you played Rock, Paper, Scissors before?: ")
print()

if played_before == "no":
    instructions()


# Lists of valid responses 
# Rock paper scissors and yes no.
yes_no_list = ["yes", "no"]
rps_list = ["rock", "paper", "scissors", "xxx"]

# Game History 
# Shows the user the game history
game_summary = [] 

# Ask user if they have played before 
# If 'yes', show instructions


#  ask user form the # of rounds then loop......
rounds_played = 0

# intialise lost / drawn counters
rounds_lost = 0 
rounds_drawn = 0

# Ask user for no of rounds, <enter> for infinite mode
# Pressing enter when the code asks you for # of rounds.
# Takes user to the Infinite mode.

rounds = check_rounds()

end_game = "no"
while end_game == "no":

  # Start of Game Play Loop 
  if rounds != "" and rounds_played == rounds - 1:
    end_game = "yes"
  # Rounds Heading 
  print()
  # Continuous rounds
  if rounds == "":
    heading = "Infinite Mode: Round {}".format(rounds_played +1)
  # Specific rounds
  else:
    heading = "Round {} of {}".format(rounds_played + 1,  rounds)
    print("Good Luck..")
    print()

  heading_decoration = "*"
  statement_generator(heading, heading_decoration)


  # Ask user for choice and check if it's valid 

  # Get computer Choice Checker 
  # Tells user that they have already picked their object
  # Tells the user what they have picked afterwards
  comp_choice = random.choice(rps_list[:-1])   
  print("I have chosen, it is your turn..")
  print()

  choose = choice_checker("Choose rock / paper / scissors (r/p/s):", rps_list, "Please choose from rock / paper / scissors (or xxx to quit)")

  print()
  comp_choice = random.choice(rps_list[:-1])   
  print("I chose", comp_choice)
  print()

  # If the code 'xxx' is typed
  # The game will end automatically
  if choose == "xxx":
        break 
  else:
    rounds_played += 1

  # Compare the choices 
  if comp_choice == choose:
      result = "Draw"
      result_decoration = "!"
      feedback = "You've Drawn"
      rounds_drawn += 1
  elif choose == "rock" and comp_choice == "scissors":
    result = "won"
  elif choose == "paper" and comp_choice == "rock":
    result = "won"
  elif choose == "scissors" and comp_choice == "paper":  
    result = "won"
  else:
    result = "lost" 
    result_decoration = "#"
    rounds_lost +=1

  # If user wins 
  # Decorate win 
  if result == "Won":
    result_decoration = "$"


    feedback ="{} vs {} - you {}".format(choose, comp_choice, result)
    statement_generator(feedback, result_decoration) 

    round_feedback = "Round {}: {}".format(rounds_played, feedback)

    game_summary.append(round_feedback)

  # Shows game statistics
  rounds_won = rounds_played - rounds_lost - rounds_drawn

  print("won {}, lost: {}, drawn: {}".format(rounds_won, rounds_lost, rounds_drawn))


  # End of Game Statements


  #  Claculates game stats 
  percent_win = rounds_won / rounds_played * 100
  percent_lose = rounds_lost / rounds_played * 100
  percent_tie = rounds_drawn / rounds_played * 100

  print()
  print("***** Game History *******")
  for game in game_summary:
    print(game)


  print()

  # display game stats with % values to the nearest whole number 
  print("***** Game Statistics *******")
  print("Win: {}, ({:.0f}%)\nLoss: {}, ({:.0f}%)\nTie: {}, ({:.0f}%)".format(rounds_won, percent_win, rounds_lost, percent_lose, rounds_drawn, percent_tie))
  print()
  # End of Game Statements 
  print()
  print('***** End Game Summary *****')
  print("Won: {} \t|\t Lost {} \t|\t Draw {}".format(rounds_won, rounds_lost, rounds_drawn))
  print()
  print("Well played!, Press <enter> to play again, or 'xxx' to quit...")  