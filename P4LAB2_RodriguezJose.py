#Jose Rodriguez
#10/26/2026
#P4LAB2
# Use while loops and for loop together

# The '''is used to write a multi-line comment.
'''
Get integer from user
Determine if integer is positive or negative
if number is positive, display multiplication table
if number is negative, tell user program cannot accept it
Ask user to run again?
If yes, run program
If no, end program
'''


run_again = "yes" # Here you are telling the user that the program will run at least once. The while loop will continue to run until the user enters "no".

while run_again != "no":

    user_num = int(input("Enter an integer: "))

    if user_num >= 0: # Here you are checking if the number is positive or negative.
        #display multiplication for that value and range (1-12)
        for item in range(1, 13):
            print(f"{user_num} x {item} = {user_num * item}")
    else:
        print("This program does not handle negative values")

    run_again = input(" Would you like to run the program again?")

    #Loop has broken. User entered 'no'
    print("Program is ending...")

