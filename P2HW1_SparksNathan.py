# Nathan Sparks
# 11 March 26
# P2HW1
# Travel Budget

print("This program calculates and displays travel expenses")
print()
budget = int( input("Enter Budget: "))
print()
dest = input("Enter your travel destination: ")
print()
gas = int( input("How much do you think you will spend on gas? "))
print()
Hotel = int( input("Approximately, how much will you need for accomodation/hotel? "))
print()
food = int(input("Last, how much do you need for food? "))
print()
print("--------Travel Expenses--------")
print(f'{"Location:":20s}{dest}')

print(f'{"Initial Budget:":20s}${budget:.2f}')

print(f'{"Fuel:":20s}${gas:.2f}')

print(f'{"Accomodation:":20s}${Hotel:.2f}')

print(f'{"Food:":20s}${food:.2f}')

print("-" * 32)

print(f'{"Remaining Balance:":20s}${budget-gas-Hotel-food:.2f}')