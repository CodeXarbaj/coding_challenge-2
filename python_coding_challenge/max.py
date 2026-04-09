# Given list 
lst = [5,8,2,6]

# Assume first element is max
max = lst[0]

# Loop through list 
for num in lst:
    if num > max:
        max = num   

# Print result
print(max)