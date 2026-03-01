# Nathan Sparks
# 28 Feb 26
# P1HW2
# Travel Budget

print("This program calculates and displays travel expenses")
print()
budget = int( input("Enter Budget: "))
dest = input("Enter your travel destination: ")
gas = int( input("How much do you think you will spend on gas? "))
Hotel = int( input("Approximately, how much will you need for accomodation/hotel? "))
food = int(input("Last, how much do you need for food? "))
print()
print("--------Travel Expenses--------")
print("Location:",dest)
print("Initial Budget:",budget)
print()
print("Fuel:",gas)
print("Accomodation:",Hotel)
print("Food:",food)
print()
print("Remaining Balance:",budget-gas-Hotel-food)