# Nathan Sparks
# 23 Feb 26
# P1HW1
# Mathematical Expressions

# print the solution of any number raised to any power

print("-----Calculating Exponents-----\n")

base = int( input("Enter an integer as the base value: ") )
exponent = int( input("Enter an integer as the exponent: "))
print()
print(base,"Raised to the power of",exponent,"is",(base**exponent),"!!")
print()

# print the solution of addition and substraction from any starting number

print("-----Addition and Substraction-----\n")

start = int( input("Enter a starting integer: "))
add = int( input("Enter an integer to add: "))
sub = int( input("Enter an integer to substract: "))
print()
print(start,"+",add,"-",sub,"is equal to",(start+add-sub))
print()