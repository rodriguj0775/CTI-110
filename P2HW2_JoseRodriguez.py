# Jose Rodriguez
 # September 26, 2026
 # P2HW2
 # This is a grade calculation for Modules 1 through 6 

# This section of the code prompts the user to input grades
Module1 = float(input("Enter grade for Module 1: "))
Module2 = float(input("Enter grade for Module 2: "))
Module3 = float(input("Enter grade for Module 3: "))
Module4 = float(input("Enter grade for Module 4: "))
Module5 = float(input("Enter grade for Module 5: "))
Module6 = float(input("Enter grade for Module 6: "))

# This section lists the grades
Grades = [Module1, Module2, Module3, Module4, Module5, Module6]
# This is section calculates the lowest, highest, sum, and average of the grades
lowest_grade = min(Grades)
highest_grade = max(Grades)
sum_of_grades = sum(Grades)
average_grade = sum_of_grades / len(Grades)

# This section i added the '-' *12 to put the - 12 times before and after the word "Results" so i dont have to hit space 12 times before and after the word "Results"
print(f'{'-' * 12} " Results " {'-' * 12}')
# Here I used the f to format the string and .2f to round to 2 decimal places
print(f'{"Lowest grade:":25s} {lowest_grade:.2f}')
print(f'{"Highest grade:":25s} {highest_grade:.2f}')
print(f'{"Sum of grades:":25s} {sum_of_grades:.2f}')
print(f'{"Average grade:":25s} {average_grade:.2f}')
# Here I used the '-' * 50 to put the - 50 times after the results so i dont have to hit space 50 times after the results
print('-' * 50)