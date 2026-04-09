# Take input string
s = input("Enter string: ")

# Remove spaces
result = ""

for ch in s:        #loop for removing spaces
    if ch != " ":
        result += ch 

# Print result
print(result)