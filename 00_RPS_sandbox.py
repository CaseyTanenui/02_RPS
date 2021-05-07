age=int(input("how old are you? "))
if age<0:
  print("That is impossible! ")
elif age<=10:
  print("you are quite young ")
elif age<=40:
  print("you are an adult ")
elif age<=65:
  print("you are 'over the hill' ")
else:
  if age<=85:
    print("Congrats, you have a gold card! ")
