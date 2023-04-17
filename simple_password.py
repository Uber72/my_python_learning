password = "core"
# For loop gives three tries before ending program.
count = int(3)


for x in range(0, count, 1):
  
  question = input("What is the password? ")
 
  if str(question) == str(password):
    print("Welcome, John")

    if str(question) == str(password):
      break  
  
  else:
    print("Incorrect password.")

# v.1 I see the flaw in my program. It does the loop with out a break when the correct password is put in.
# v.1.2 I Added a break condition to exit program after question matches password.

