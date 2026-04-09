# take age input from th user
age = int(input("Enter age: "))

# checking age  
if age < 18:
    print("Minor")
elif age < 60:
    print("Adult")
else:
    print("Senior")