# Take input string from user
s = input("Enter string: ")

# Reverse string logic
r = s[::-1]

# Check palindrome
if s == r:
    print(s," is palindrome")
else:
    print(s,"Not palindrome")