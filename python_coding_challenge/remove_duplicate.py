# given list
lst = [1, 1, 2, 3]

# new list for unique elements,now it's empty
result = []

# Loop through list
for num in lst:
    if num not in result:   # Check duplicate values
        result.append(num)   #append() use for adding in result

# Print result
print(result)