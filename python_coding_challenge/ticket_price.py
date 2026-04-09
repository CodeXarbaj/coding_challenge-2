# Take day input from user
day = input("Enter day: ")

# Convert to lowercase 
day = day.lower()

# Check price based on day
if day == "sunday":
    print("100")
elif day == "monday":
    print("200")
elif day == "tuesday":
    print("300")
elif day == "wednesday":
    print("400")
elif day == "thursday":
    print("500")
elif day == "friday":
    print("60")
elif day == "saturday":
    print("1500")