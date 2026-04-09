
n = int(input("Enter number: "))
total = 0
# Calculate sum
while num > 0: ##using while loop for calculating sum of digit
    digit = n % 10
    total += digit
    n //= 10
# Print result
print(total)