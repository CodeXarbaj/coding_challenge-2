# taking input string and character
s = input("Enter string = ")
ch = input("Enter character = ")

# Counter, initialize by zero
count = 0

# Loop through string for counting occurance
for c in s:
    if c == ch:
        count += 1

# Print result
print(count)