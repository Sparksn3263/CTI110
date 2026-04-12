# Nathan Sparks
# 5 April 2026
# P4LAB2
# Use loops to create multiplication table based on number given by user

run_again = 'yes'

while run_again != "no":

# ask user for number to run multiplication table

    user_int = int(input("Enter an integer: "))
    print()
    # display the multiplication table for the integer from user up to x12
    if user_int >= 0:
        for item in range (1, 12+1) :
            print(f"{user_int} * {item} = {user_int * item}")

    # print an error message if user inputs a negative number
    else:
        print("This program does not handle negative numbers.")

    print()

    run_again = input("Would you like to run the program again? ")
    print()

#Loop has broken. User entered 'no'
print("Exiting program...")

