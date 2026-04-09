# Taking input from user
num = int(input("Enter number: "))
# Initialize reverse variable 'r' with 0
r = 0
# Reverse logic 
while num > 0:
    digit = num % 10        # Get last digit
    r = rev * 10 + digit  # Building reverse
    num //= 10              # Remove last digit from number

# Printing result
print(r)