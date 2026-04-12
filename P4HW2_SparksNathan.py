# Nathan Sparks
# 12 April 2026
# P4HW2
# Pay calculator with loops

# Request info from Employee
name = input("Enter employee's name or 'Done' to terminate: ")

# create accumulator variables for overtime pay, regular pay, gross pay, employee count
overtimepay_total = 0
regularpay_total = 0
grosspay_total = 0
employee_count = 0

while name != 'Done':
    #add employee count
    employee_count += 1
    #ask for employee info
    hours = float(input("How many hours did " +name+ " work this week? "))
    rate = float(input("What is " +name+ "'s pay rate? "))


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
    #add to accumulator variables
    overtimepay_total += overtime_pay
    regularpay_total += regular_pay
    grosspay_total += gross_pay

    # Display Results
    print()
    print("Employee Name:", name)
    print()
    print(f'{"Hours Worked":<15}{"Pay Rate":<12}{"OverTime":<12}{"OverTime Pay":<15}{"RegHour Pay":<15}{"Gross Pay":<12}')
    print("-" * 80)
    print(f'{hours:<15}{rate:<12}{overtime_hours:<12}${overtime_pay:<14.2f}${regular_pay:<14.2f}${gross_pay:<12.2f}')
    print()
    name = input("Enter employee's name or 'Done' to terminate: ")
print()
print("Total number of employees entered: ", employee_count)
print("Total amount paid for overtime: $", format(overtimepay_total, ',.2f'))
print("Total amount paid for regular hours: $", format(regularpay_total, ',.2f'))
print("Total amount paid in gross: $", format(grosspay_total, ',.2f'))