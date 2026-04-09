# Given lists
l1 = [1,2,3,5]
l2 = [2,3,4,5]

# Result list
common = []

# Find common element in l1 and l2
for num in l1:
    if num in l2:
        common.append(num)

# Printing result
print(common)