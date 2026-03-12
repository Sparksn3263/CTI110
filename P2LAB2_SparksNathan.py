# Nathan Sparks
# 7 March 2026
# P2LAB2
# Vehicle MPG dictionary

# Dictionary - Vehicle : MPG
vehicles = {'Camaro':18.21, 'Prius':52.36, 'Model S':110, 'Silverado':26}

# Keys
car_keys = vehicles.keys()

print(car_keys)
print()
      
# Get a car from user
car_name = input("Enter a vehicle to see it's mpg: ")
print()

# Get mpg for the given car
car_mpg = vehicles[car_name]

print(f"The {car_name} gets {car_mpg} miles per gallon.")
print()

# Get miles from user
miles_driven = float(input(f"How many miles will you drive the {car_name}? "))
print()

# Calculate gallons needed given the miles driven
gallons_needed = miles_driven / car_mpg

# Display results

print(f"{gallons_needed:.2f} gallon(s) of gas are needed to drive the {car_name} {miles_driven} miles.")
