# Taking input from user
num = int(input("Enter number: "))

# Counter for counting num
count = 0

# Count digits using while lopp
while num > 0:
    count += 1
    num //= 10

# Print result 
print(count)