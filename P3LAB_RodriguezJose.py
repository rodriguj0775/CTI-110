 # Jose Rodriguez
 # October 7 2026
 # P3LAB
 # This program will calculate efficient numbers of dollars,quaters,dimes,nickels, and pennies and we will be using the // function. 
 # The // function is used to divide and round down to the nearest whole number.


#Get value from user
change = float(input("Enter an amount of money: $"))

print(f"Change Amount: {change}")

#Converting the value to an integer
change = round(change * 100)

print(f"Change Amount: {change}")

#Determine how many coins are needed
num_dollars = change // 100
change = change - (num_dollars * 100)

num_quaters = change // 25
change = change - (num_quaters * 25)

num_dimes = change // 10
change = change - (num_dimes * 10)

num_nickels = change // 5
change = change - (num_nickels * 5)

num_pennies = change

#This section will print the number of coins needed but dont fogert print means to display the output to the user once your run the program.
if num_dollars > 0:
    if num_dollars == 1:
        print(f"{num_dollars} Dollar")
    else:
        print(f"{num_dollars} Dollars")

if num_quaters > 0:
    if num_quaters == 1:
        print(f"{num_quaters} Quarter")
    else:
        print(f"{num_quaters} Quarters")

if num_dimes > 0:
    if num_dimes == 1:
        print(f"{num_dimes} Dime")
    else:
        print(f"{num_dimes} Dimes")

if num_nickels > 0:
    if num_nickels == 1:
        print(f"{num_nickels} Nickel")
    else:
        print(f"{num_nickels} Nickels")

if num_pennies > 0:
    if num_pennies == 1:
        print(f"{num_pennies} Penny")
    else:
        print(f"{num_pennies} Pennies")



