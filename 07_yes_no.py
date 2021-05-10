# Yes No checker - V1 

# If user says 'yes', program continues..
# If user says 'no', display instructions..
def yes_no(question):
  valid  = False
  while not valid:
    response = input (question).lower()

    if response == "yes" or response == "y":
      response = "yes"
      return response

    elif response == "no" or response == "n":
      response = "no"
      return response

    else:
      print("Please answer yes/no")