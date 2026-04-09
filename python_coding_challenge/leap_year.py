##Take year input form user
year = int(input("Enter year: "))

# Checking leap year condition
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year," is Leap Year")
else:
    print(year, "is Not Leap Year")