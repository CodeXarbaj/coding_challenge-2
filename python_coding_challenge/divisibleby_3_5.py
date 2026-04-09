# Take number input
num = int(input("Enter number: "))

# Checking divisibility by 3 and 5
if num % 3 == 0 and num % 5 == 0:
    print("Yes divisible by 3 and 5")
else:
    print("Not divisible by 3 and 5")