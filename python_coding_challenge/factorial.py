# Take input from user
n = int(input("Enter number = "))

# Initialize factorial variable by 1
fact = 1

# Calculate factorial
for i in range(1, n+1):
    fact *= i   # Multiply

# Print result of calculated factorial
print(fact)