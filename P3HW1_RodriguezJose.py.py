 #Jose Rodriguez
 # Octoober 7, 2026
 # P3HW1
 # Debugging and fixing errors in the code,
 # Use P2HW2 as reference


# This program takes a number grade , determines average and displays letter grade for average.

# Enter grades for six modules
# dont forget you can use the ' or the double " to put a string in the input function
# input vs float, input returns a string and float converts the string to a number
# use float when you want to do math, float is also use for decimal numbers, int is only for whole numbers
mod_1 = float(input('Enter grade for Module 1: '))
mod_2 = float(input('Enter grade for Module 2: '))
mod_3 = float(input('Enter grade for Module 3: '))
mod_4 = float(input('Enter grade for Module 4: '))
mod_5 = float(input('Enter grade for Module 5: '))
mod_6 = float(input('Enter grade for Module 6: '))

# add grades entered to a list
#mod 6 was missing, mod_2 was mod2 > it was missing ,
grades = [mod_1, mod_2, mod_3, mod_4, mod_5, mod_6]
# TO DO: determine lowest, highest , sum and average for grades

# grades was Grades and hight was using hight and not max, sum was using sum and not total, avg was missing the formula to calculate the average
low = min(grades)
high = max(grades)
total = sum(grades)
avg = total / len(grades)

# This area was missing everything and i just use the reference from P2HW2 to fix the code and make it work.

print(f'{"-" * 12} " Results " {"-" * 12}')

print(f'{"Lowest grade:":25s} {low:.2f}')
print(f'{"Highest grade:":25s} {high:.2f}')
print(f'{"Sum:":25s} {total:.2f}')
print(f'{"Average:":25s} {avg:.2f}')    

# determine letter grade for average
# I just copy the code and move it to the bottom of the codes
# so the final grade will be last as showing in Canvas example.
# I use the elif learned from previeous lesson, elif is used to check multiple conditions, if the first condition is not met, it will check the next condition and so on.
if avg >= 90:
	print('Your grade is: A')
elif avg >= 80:
	print('Your grade is: B')
elif avg >= 70:
	print('Your grade is: C')
elif avg >= 60:
	print('Your grade is: D')
else:
	print('Your grade is: F')


