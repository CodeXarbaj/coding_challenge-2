# Take marks input from usr
marks = int(input("Enter marks: "))

# assign grade based on number
if marks >= 90:
    print("A")
elif marks >= 75:
    print("B")
elif marks >= 50:
    print("C")
else:
    print("Fail")