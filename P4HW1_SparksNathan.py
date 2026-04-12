# Nathan Sparks
# 10 April 2026
# P4HW1
# Receive grade input and dispay scores/average/grade


# Ask for mumber of grades user wishes to input

grades = int(input("How many scores to you want to enter? "))
print()

# Creating List of all grades
grades_list = []  

# for loop to ask user for each grade based on number of grades they specified

for scores in range (grades) :
    grade_inp = float(input(f"Enter score #{scores +1}: "))
    
    if grade_inp < 0 or grade_inp > 100 :
        print()
        print("INVALID Score entered!!!\nScore should be between 0 and 100")
        grade_inp = float(input(f"Enter score #{scores +1} again: "))
    if grade_inp >= 0 or grade_inp <= 100:
        #add score in range to list
        grades_list.append(grade_inp)
    
    
print()

# Set variables for lowest; highest; sum; average grades

# lowest number in grades list
min_value = min(grades_list)

# highest numbber in grades list
max_value = max(grades_list)

# the total or sum of all grades in the list added together
total = sum(grades_list)

# the total number of grades in the list
num_items = len(grades_list)

# the average of grade minus lowest grade
avg = (total/num_items)

# Display results(lowest; Modified list without lowest score; average score and grade


print("------------Results------------")

print(f'{"Lowest Score  : "}{min_value:.1f}')

#remove lowest score from list
grades_list.remove(min_value)


print("Modified List : " ,grades_list)
print(f'{"Scores Average: "}{total/num_items:.1f}')
if avg >= 90:
    print("Your grade is: A")

elif avg >= 80:
    print('Your grade is: B')
      
elif avg >= 70:
    print('Your grade is: C')
        
elif avg >= 60:
    print('Your grade is: D')
        
else:
    print('Your grade is: F')

print("-" * 40)
