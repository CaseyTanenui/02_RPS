#  From items in range of 0 to 5
# Print the % Of how many times you have chosen those items
# Most items = Most percentage 
# less items = Less percentage

game_summary = []

rounds_lost = 0 
rounds_drawn = 0 
rounds_played = 0

for item in range (0, 10):
  result = input ("Choose results: ")

  outcome = "Round {}: {}".format(item, result)

  if result == "lost":
    rounds_lost += 1
  elif result == "tie":
    rounds_drawn += 1

  game_summary.append(outcome)

rounds_won = rounds_played - rounds_lost - rounds_drawn 

# *** Calculate game stats ***
percent_win = rounds_won / rounds_played * 100
percent_lose = rounds_lost / rounds_played * 100 
percent_tie = rounds_drawn / rounds_played * 100 

print()
print("*** Game History ***")

for game in game_summary:
  print(game)

print()

# Displays games stats with % values to the nearest whole number 
print("***** Game Statistics *****")
print("Win: {}, ({:.0f}%) \nloss: {}, ({:.0f}%) \ntie: {}, ({:.0f}%)".format(rounds_won, percent_win, rounds_lost, percent_lose, rounds_drawn, percent_tie))
