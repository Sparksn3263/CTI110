# Nathan Sparks
# 7 March 2026
# P2LAB1
# Calculate diameter, Circumference, area of a circle

# Import math module to use the constant, math.pi
import math

# Get radius from user
radius = float(input("What is the radius of the circle? "))
print()

# Calculate diameter
diameter = 2 * radius

# Display diameter with 1 decimal point
print(f"The diameter of the circle is {diameter:.1f}\n")

# Calcuate circumference with 2 decimal places
circumference = 2 * math.pi * radius

print(f"The circumference of the circle is {circumference:.2f}\n")

# calculate the area
area = math.pi * radius**2

# Display area with 3 decimal places
print(f"The area of the circle is {area:.3f}")

