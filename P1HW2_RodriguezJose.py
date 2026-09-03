 # Jose Rodriguez
 # September 3, 2026
 # P1HW2
 # Budgeting and calculating expenses

# line 7 is the title
print("--------This program calculates and displays travel expenses--------")
# line 9 it gives you a space to enter your budget
print()
# line 11 it asks for the budget
base = int(input("Enter budget: "))
# line13 it gives you s space
print ()
# line 15 it asks for the travel destination
destination = input("Enter your travel destination:")
# line 17 it gives you a space
print ()
# line 19 it asks for the gas expenses
Gas = int(input("How much do you think you will spend on gas?: "))
# Line 21 it gives you a space
print ()
# line 23 it asks for the hotel expenses
food = int(input("Approximately, how much will you need for accommodation/hotel?: "))
# line 25 it gives you a space
print ()
# line 27 it asks for the food expenses, also you use int to make sure the input is a number and input to get the value from the user
food_expenses = int(input("Last, how much do you need for food?: "))

#line 30 it gives you another title but also rememeber the " " is used to make sure the text is a string and not a number
print("--------Travel Expenses--------")
# line 32 shows the location = destination but the blue is what you see and the destination is the value you input
print ("Location",destination)
# line 34 wors the same as line 32 but with the budget
print ("Initial Budget:", base)
# line 36 gives you a space
print()
# line 38,39 and 40 shows the expenses for gas, accommodation and food.
print ("Fuel:", Gas)
print ("Accommodation:", food)
print ("Food:", food_expenses)
# line 42 it is the sum of the expenses and it is subtracted from the budget to give you the remaining balance
Sum_results = base - Gas - food - food_expenses
# line 44 it shows the remaining balance after all the expenses are subtracted from the budget
print ("Remaining Balance:", Sum_results)
