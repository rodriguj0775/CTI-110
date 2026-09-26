# Jose Rodriguez
 # September 26, 2026
 # P2HW1
 # Calculate and Display travel expenses using float
 # In this class, I have learned that when I type code incorrectly, the small window on the
 # top-right shows a red line >>> at the line where I made a mistake; this helps me a lot.

# This is the title, i replace the multiple input of the ----- by using f'{'-'*} using {'-'*12} repeats --------
print("This program calculates and displays travel expenses")
# it gives you a space to enter your budget
print()
#  Float will allow a whole number
base = float(input("Enter budget: "))
#  it gives you s space
print ()
#  it asks for the travel destination
destination = input("Enter your travel destination: ")
#  it gives you a space
print ()
#  it asks for the gas expenses
Gas = float(input("How much do you think you will spend on gas? "))
#  it gives you a space
print ()
#  it asks for the hotel expenses
food = float(input("Approximately, how much will you need for accommodation/hotel? "))
#  it gives you a space
print () 
#  it asks for the food expenses, also you use int to make sure the input is a number and input to get the value from the user
food_expenses = float(input("Last, how much do you need for food? "))
# I added a space here
print ()
# it gives you another title but also rememeber the " " is used to make sure the text is a string and not a number
print(f' {'-' * 12 } Travel Expenses {'-' * 12}')
# shows the location = destination but the blue is what you see and the destination is the value you input
print (f'{"Location:":20s} {destination}')
# f is for formating string = text and .2f gives you 2 decimal or add 4f and is 4 decimals
print (f"{"Initial Budget:":19s}  ${base:.2f}")
# I removed the print () so it wont be a space here
# I added the 20s for spaces
print (f"{"Fuel:":20s} ${Gas:.2f}")
print (f"{"Accommodation:":20s} ${food:.2f}")
print (f"{"Food:":20s} ${food_expenses:.2f}")
# it is the sum of the expenses and it is subtracted from the budget to give you the remaining balance
Sum_results = base - Gas - food - food_expenses
# Here I only use the () since no words are being used.
print ('-'*30)
print ()

print (f"{"Remaining Balance:":20s} ${Sum_results:.2f}")
# I had to run multiple times to see where i needed a space 
# I notice when I add a space on the run section it will be reflected> for example i add (type) a space in NYC and i had to remove it.