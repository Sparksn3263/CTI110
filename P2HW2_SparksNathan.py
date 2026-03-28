# Nathan Sparks
# 12 March 2026
# P2HW2
# List Grades and Display averages

# Creating List of all grades

grades = []

# Grade inputs for each Module

mod_1 = float(input("Enter grade for Module 1: "))
grades.append(mod_1)

mod_2 = float(input("Enter grade for Module 2: "))
grades.append(mod_2)

mod_3 = float(input("Enter grade for Module 3: "))
grades.append(mod_3)

mod_4 = float(input("Enter grade for Module 4: "))
grades.append(mod_4)

mod_5 = float(input("Enter grade for Module 5: "))
grades.append(mod_5)

mod_6 = float(input("Enter grade for Module 6: "))
grades.append(mod_6)

print()

# Set variables for lowest; highest; sum; average grades

# lowest number in grades list
min_value = min(grades)

# highest numbber in grades list
max_value = max(grades)

# the total or sum of all grades in the list added together
total = sum(grades)

# the total number of grades in the list
num_items = len(grades)

# Display results(lowest; highest; sum; average)average="total" divided by (/) "num_items"

print("------------Results------------")

print(f'{"Lowest Grade:":20s}{min_value:.1f}')
print(f'{"Highest Grade:":20s}{max_value:.1f}')
print(f'{"Sum of Grades:":20s}{total:.1f}')
print(f'{"Average:":20s}{total/num_items:.1f}')

print("-" * 40)