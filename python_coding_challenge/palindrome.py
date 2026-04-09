# taking input from user
num = int(input("Enter number= "))

# Store original number in 'n'
n = num
r = 0

# Reverse number
while num > 0:
    digit = num % 10
    r = r * 10 + digit
    num //= 10

# Check palindrome
if n == r:
    print(n," is Palindrome")
else:
    print(n, "is Not Palindrome")