# Taking input string from user
s = input("Enter string = ")

# Initialize result with empty
result = ""

# Replace vowels with '*'
for ch in s:
    if ch.lower() in "aeiou":
        result += "*"
    else:
        result += ch

# Print result
print(result)