# Nathan Sparks
# 28 March 2026
# P3HW2
# Pay calculator

# Request info from Employee

name = input("Enter employee's name: ")
hours = float(input("Enter number of hours worked: "))
rate = float(input("Enter employee's pay rate: "))

# Calculate overtime pay
if hours > 40:
    # Calculate overtime
    overtime_hours = hours - 40
    # Calculate overtime pay
    overtime_pay = overtime_hours * (rate * 1.5)
    # Calculate salary for regular pay
    regular_pay = 40 * rate
    # Calculate Gross pay
    gross_pay = regular_pay + overtime_pay
else:
    overtime_pay = 0
    overtime_hours = 0
    regular_pay = hours * rate
    gross_pay = regular_pay

# Display Results
print("-" * 40)
print("Employee Name:", name)
print()
print(f'{"Hours Worked":<15}{"Pay Rate":<12}{"OverTime":<12}{"OverTime Pay":<15}{"RegHour Pay":<15}{"Gross Pay":<12}')
print("-" * 80)
print(f'{hours:<15}{rate:<12}{overtime_hours:<12}${overtime_pay:<14.2f}${regular_pay:<14.2f}${gross_pay:<12.2f}')
