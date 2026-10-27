#Jose Rodriguez
#10/27/2026
#P4HW1
# The program will use a loop and collect score from the user.



'''Ask user to input the number of scores they would like to enter
Create a loop to collect the number of scores the user wants to enter
Evaluate if the score is valid, it should be between 0 and 100 . 
If it is not, notify the user and ask for a VALID score to be entered.'''


# Ask user how many scores they want to enter
num_scores = int(input("How many scores do you want to enter? "))

# Create empty list
scores = []
# Collect scores
for item in range(num_scores):

    score = float(input(f"Enter score #{item + 1}: "))

    # Validate score
    while score < 0 or score > 100:
        print()# This is use to add space between words.
        print("INVALID Score entered!!!!")
        print("Score should be between 0 and 100")

        score = float(input(f"Enter score #{item + 1} again: "))

    scores.append(score) # Here you are adding the score to the list after it has been validated.

# Find lowest score
lowest_score = min(scores)

# Create modified list
modified_list = scores.copy() # Here
modified_list.remove(lowest_score)

# Calculate average
scores_average = sum(modified_list) / len(modified_list)

# Determine grade
if scores_average >= 90:
    grade = "A"
elif scores_average >= 80:
    grade = "B"
elif scores_average >= 70:
    grade = "C"
elif scores_average >= 60:
    grade = "D"
else:
    grade = "F"
print()
# Display results
print("---------------Results---------------")
print(f"Lowest Score   : {lowest_score:.1f}")
print(f"Modified List  : {modified_list}")
print(f"Scores Average : {scores_average:.2f}")
print(f"Grade          : {grade}")
print("---------------------------------------")