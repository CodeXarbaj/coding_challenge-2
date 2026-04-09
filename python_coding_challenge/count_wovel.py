# Taking input string from user
s = input("Enter string = ")

# Initialize counter to 0 
c = 0

# using loop through string
for ch in s.lower():
    if ch in "aeiou":   # Check vowel using if
        c += 1

# printing result
print(c)