# given dictionary
students = {"Amit": 80, "Bhanu": 95, "Chikara": 78}

# Assume first student max
topstudent = ""
maxmark = 0

# Find highest marks
for name in students:
    if students[name] > maxmarks:
        maxmarks = students[name]
        topstudent = name

# Print result
print(topstudent)