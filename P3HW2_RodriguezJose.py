#Jose Rodriguez
 # Octoober 9, 2026
 # P3HW2
 # Payroll Calculator
 # The program will ask the user to enter work hours and pay rate for an employee. 

# request employee information
name = input("Enter employee name: ")
hours = float(input("Enter number of hours worked: "))
rate = float(input("Enter hourly pay rate: "))

# Evaluate overtime pay
if hours > 40:
    # Calcualte overtime
    overtime_hours = hours - 40
    # Calculate over pay
    overtime_pay = overtime_hours * (rate * 1.5)
    # Calculate salary for regular hours
    regular_pay = 40 * rate
    # Calculate Gross pay
    gross_pay = regular_pay + overtime_pay
else:
    overtime_pay = 0
    overtime_hours = 0
    regular_pay = hours * rate
    gross_pay = regular_pay

# Display results
print ('-'*30)
print("Employee Name:", name)
print(f"{'Hours Worked':<15}{'Pay Rate':<12}{'Overtime':<12}{'Overtime Pay':<15}{'Regular Hours Pay':<20}{'Gross Pay':<20}")

print ('-'*85)

print(f'{hours:<15}{rate:<12}{overtime_hours:<12}{overtime_pay:<15}${regular_pay:<15}${gross_pay:<15}')

#Before summiting I notice the video insturction is missing overtime hours and the $ signs in Regular Pay and Gross Pay. Canvas instructions ask for this.
